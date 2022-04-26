from gensim.models import Word2Vec   #to load the model 
import math
import pandas as pd
import numpy as np
import gc
import pickle
# Import writer class from csv module
from csv import writer

words_gt = []
# to make the list of list which contain the list of word pair with ground truth
with open('Word similarity/hindi.txt', encoding = 'utf-8', errors = 'ignore') as file:
    words_gt = [word.strip().split(',') for word in file if word.strip() != '']

gt_list1 = []
gt_list2 = []
gt_list1 = [word[0].strip() for word in words_gt]
gt_list2 = [word[1].strip() for word in words_gt]



unique_word_dict1 = set([word for word in gt_list1])
unique_word_dict2 =set([word for word in gt_list2])
unique_word_dict = unique_word_dict1.union(unique_word_dict2)
# len(unique_word_dict)

arr_dict = {}
path_glove = ["hi/50/glove/hi-d50-glove.txt", "hi/100/glove/hi-d100-glove.txt", "hi/200/glove/hi-d200-glove.txt","hi/300/glove/hi-d300-glove.txt"]
name = ['50','100','200','300']
for p,n in zip(path_glove, name):
    print(p)
    with open(p, errors= 'ignore', encoding = 'UTF-8') as file:
        line = file.readlines()
        for element in line:
            if element.strip() and element.split()[0] in unique_word_dict:
                arr_dict[element.split()[0]] = [float(e) for e in element.strip().split(' ')[1:]]
    
        del line
        gc.collect()
    

    pickle.dump(arr_dict, open('Ques1/glove_vector_{0}.dat'.format(n),'wb'))


      


