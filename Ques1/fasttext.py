# importing the required libraries
import os
import pickle  
from gensim.models import Word2Vec   #to load the model 
import pandas as pd
import numpy as np
import gc

words_gt = []
# to make the list of list which contain the list of word pair with ground truth
with open('Word similarity/hindi.txt', encoding = 'utf-8', errors = 'ignore') as file:
    words_gt = [word.strip().split(',') for word in file if word.strip() != '']


gt_list1 = []
gt_list2 = []
gt = []
gt_list1 = [word[0].strip() for word in words_gt]
gt_list2 = [word[1].strip() for word in words_gt]
gt = [word[2].strip() for word in words_gt]

def find_cos_sim(list1, list2):     # takes two list return their cosine similarity after converting them into vector
    vector1 = np.array(list1)
    vector2 = np.array(list2)
    normalized_v1 = vector1 / np.sqrt(np.sum(vector1**2))
    normalized_v2 = vector2 / np.sqrt(np.sum(vector2**2))
    cosine_sim = np.dot(normalized_v1 , normalized_v2 )
    return cosine_sim

aaccuracy_for_fasttext = pd.DataFrame(columns = ['0.4', '0.5', '0.6', '0.7','0.8'], index = ['50', '100', '200','300'])
path_fasttext = ["hi/50/fasttext/hi-d50-m2-fasttext.model", "hi/100/fasttext/hi-d100-m2-fasttext.model", "hi/200/fasttext/hi-d200-m2-fasttext.model", "hi/300/fasttext/hi-d300-m2-fasttext.model"]
dim_for_fasttext = ['50', '100', '200', '300']
threshold = ['0.4', '0.5', '0.6', '0.7', '0.8']
cosim_of_fasttext = {}


for dim,p in zip(dim_for_fasttext,path_fasttext):

    model_of_fasttext = Word2Vec.load(p)
    if dim not in cosim_of_fasttext:
        cosim_of_fasttext[dim] = {}

    for ind in threshold:

        # true_pos = 0
        # true_neg = 0
        if ind not in cosim_of_fasttext[dim]:

            cosim_of_fasttext[dim][ind] = {}

        for i in range(len(gt_list1)):

            # cosim_of_cbow[ind][dim] = find_cos_sim(model_of_cbow.wv[gt_list1[i]], model_of_cbow.wv[gt_list2[i]])
            cosim_of_fasttext[dim][ind][(gt_list1[i],gt_list2[i],gt[i])] = find_cos_sim(model_of_fasttext.wv[gt_list1[i]], model_of_fasttext.wv[gt_list2[i]])

    del model_of_fasttext
    gc.collect()

pickle.dump(cosim_of_fasttext, open('Ques1/cosim_of_fasttext.dat','wb'))



