#!/usr/bin/env python


# install the required modules as listed below
# pip install transformers seqeval[gpu] sentencepiece protobuf'
# pip install pandas'
# pip install torch'




import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
import torch
from torch.utils.data import Dataset, DataLoader



from transformers import AutoModel, AutoTokenizer, AutoModelForTokenClassification




from torch import cuda
device = 'cuda' if cuda.is_available() else 'cpu'
# print(device)



tokenizer = AutoTokenizer.from_pretrained('ai4bharat/indic-bert', keep_accents=True)



def extract_data_from_conll(file_name):
    train_list=[[]]
    train_tag_list = [[]]
  
    with open('Ques2/hindi_ner/{0}'.format(file_name),"r") as input:
        for l in input:
            if not l.startswith("#"):

                if l.strip()=="":

                    if len(train_list[-1])>0:
                        train_list.append([])
                        train_tag_list.append([])
                else:

                    train_list[-1].append(l.split()[0])
                    train_tag_list[-1].append(l.split()[3])
    train_list=[ " ".join(row) for row in train_list ]
    train_tag_list=[ " ".join(row) for row in train_tag_list ]
    return [{"sentence": x, "tags": y.split()} for x, y in zip(train_list[:-1], train_tag_list[:-1])]



train_ds = extract_data_from_conll('hi_train.conll')
test_ds = extract_data_from_conll('hi_dev.conll')




distinct_tags = set()
for s in train_ds:
  distinct_tags.update(s['tags'])




tags_to_ids = {tag: id for id, tag in enumerate(distinct_tags)}
ids_to_tags = {id: tag for id, tag in enumerate(distinct_tags)}




MAX_LENGTH = 128
BATCH_SIZE = 4
VALID_BS = 2
MY_EPOCHS = 6
RATE_TO_LEARN = 1e-05
MAXIMUM_GRAD_NORM = 10



class HiDataset(Dataset):
  def __init__(self, dataset, tokenizer, MAX_LENGTH):
    self.len = len(dataset)
    self.data = dataset
    self.tokenizer = tokenizer
    self.MAX_LENGTH = MAX_LENGTH

  def __getitem__(self, index):
    sentence = self.data[index]['sentence'].strip().split()
    tags = self.data[index]['tags']
    encoding = self.tokenizer(sentence,
                              is_split_into_words=True,
                              return_offsets_mapping=True,
                              padding='max_length',
                              truncation=True,
                              max_length=self.MAX_LENGTH)
    
    tag_ids = [tags_to_ids[tag] for tag in tags]

    word_ids = encoding.word_ids()
    encoded_tags = []
    prev_id = -1
    for word_id in word_ids:
      if word_id is None:
        encoded_tags.append(-100)
      else:
        encoded_tags.append(tag_ids[word_id])
      prev_id = word_id
  
    item = {key: torch.as_tensor(val) for key, val in encoding.items()}
    item['labels'] = torch.as_tensor(encoded_tags)

    return item

  def __len__(self):
    return self.len


training_set = HiDataset(train_ds, tokenizer, MAX_LENGTH)
testing_set = HiDataset(test_ds, tokenizer, MAX_LENGTH)

training_parameters = {
    'batch_size': BATCH_SIZE,
    'shuffle': True,
    'num_workers': 0
}

test_parameters = {
    'batch_size': VALID_BS,
    'shuffle': True,
    'num_workers': 0
}

training_loader = DataLoader(training_set, **training_parameters)
testing_loader = DataLoader(testing_set, **test_parameters)




model = AutoModelForTokenClassification.from_pretrained('ai4bharat/indic-bert', num_labels=len(tags_to_ids))
model.to(device)




optimizer = torch.optim.Adam(params=model.parameters(), lr=RATE_TO_LEARN)




# Defining the training function on the 80% of the dataset for tuning the bert model
def train(epoch):
    tr_loss, tr_accuracy = 0, 0
    nb_tr_examples, nb_tr_steps = 0, 0
    tr_preds, tr_labels = [], []
    # put model in training mode
    model.train()
    
    for idx, batch in enumerate(training_loader):
        
        ids = batch['input_ids'].to(device, dtype = torch.long)
        mask = batch['attention_mask'].to(device, dtype = torch.long)
        labels = batch['labels'].to(device, dtype = torch.long)

        loss, tr_logits = model(input_ids=ids, attention_mask=mask, labels=labels).values()
        tr_loss += loss.item()
        nb_tr_steps += 1
        nb_tr_examples += labels.size(0)
        
        if idx % 100==0:
            loss_step = tr_loss/nb_tr_steps
            print(f"Training loss per 100 training steps: {loss_step}")
           
        # compute training accuracy
        flattened_targets = labels.view(-1) # shape (batch_size * seq_len,)
        active_logits = tr_logits.view(-1, model.num_labels) # shape (batch_size * seq_len, num_labels)
        flattened_predictions = torch.argmax(active_logits, axis=1) # shape (batch_size * seq_len,)
        
        # only compute accuracy at active labels
        active_accuracy = labels.view(-1) != -100 # shape (batch_size, seq_len)
        #active_labels = torch.where(active_accuracy, labels.view(-1), torch.tensor(-100).type_as(labels))
        
        labels = torch.masked_select(flattened_targets, active_accuracy)
        predictions = torch.masked_select(flattened_predictions, active_accuracy)
        
        tr_labels.extend(labels)
        tr_preds.extend(predictions)

#         tmp_tr_accuracy = accuracy_score(labels.cpu().numpy(), predictions.cpu().numpy())
        tr_accuracy += accuracy_score(labels.cpu().numpy(), predictions.cpu().numpy())
    
        # gradient clipping
        torch.nn.utils.clip_grad_norm_(parameters=model.parameters(), max_norm=MAXIMUM_GRAD_NORM)
        
        # backward pass
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    epoch_loss = tr_loss / nb_tr_steps
    tr_accuracy = tr_accuracy / nb_tr_steps
    print(f"Training loss epoch: {epoch_loss}")
    print(f"Training accuracy epoch: {tr_accuracy}")




for epoch in range(MY_EPOCHS):
    print(f"Training epoch: {epoch + 1}")
    train(epoch)



def valid(model, testing_loader):
    # put model in evaluation mode
    model.eval()
    
    eval_loss, eval_accuracy = 0, 0
    nb_eval_examples, nb_eval_steps = 0, 0
    eval_preds, eval_labels = [], []
    
    with torch.no_grad():
        for idx, batch in enumerate(testing_loader):
            
            ids = batch['input_ids'].to(device, dtype = torch.long)
            mask = batch['attention_mask'].to(device, dtype = torch.long)
            labels = batch['labels'].to(device, dtype = torch.long)
            
            loss, eval_logits = model(input_ids=ids, attention_mask=mask, labels=labels).values()
            
            eval_loss += loss.item()

            nb_eval_steps += 1
            nb_eval_examples += labels.size(0)
        
            if idx % 100==0:
                loss_step = eval_loss/nb_eval_steps
                print(f"Validation loss per 100 evaluation steps: {loss_step}")
              
            # compute evaluation accuracy
            flattened_targets = labels.view(-1) # shape (batch_size * seq_len,)
            active_logits = eval_logits.view(-1, model.num_labels) # shape (batch_size * seq_len, num_labels)
            flattened_predictions = torch.argmax(active_logits, axis=1) # shape (batch_size * seq_len,)
            
            # only compute accuracy at active labels
            active_accuracy = labels.view(-1) != -100 # shape (batch_size, seq_len)
        
            labels = torch.masked_select(flattened_targets, active_accuracy)
            predictions = torch.masked_select(flattened_predictions, active_accuracy)
            
            eval_labels.extend(labels)
            eval_preds.extend(predictions)
            
            tmp_eval_accuracy = accuracy_score(labels.cpu().numpy(), predictions.cpu().numpy())
            eval_accuracy += tmp_eval_accuracy

    labels = [ids_to_tags[id.item()] for id in eval_labels]
    predictions = [ids_to_tags[id.item()] for id in eval_preds]
    
    eval_loss = eval_loss / nb_eval_steps
    eval_accuracy = eval_accuracy / nb_eval_steps
    print(f"Validation Loss: {eval_loss}")
    print(f"Validation Accuracy: {eval_accuracy}")

    return labels, predictions


labels, predictions = valid(model, testing_loader)




from sklearn.metrics import classification_report

print(classification_report(labels, predictions))



