# importing required modules
import matplotlib.pyplot as plt
import numpy as np
import pickle
from matplotlib.pyplot import figure

char_freq_list_u = []
num = ['0','1','2','3','4','5','6','7','8','9']


# for char unigram

#open file and took those words whose first letter is number
with open('Ques3/char_ngram/char_unigram.txt') as f:
    for line in f:
        temp = ''
        for word in line.split():
            if word[0] in num:
                char_freq_list_u.append(int(word))
                
x_dim = [int(ind) for ind in range(1,102)]
# len(x_dim)
# len(char_freq_list)
figure(figsize=(14, 8), dpi=120)
plt.plot(x_dim, char_freq_list_u)   # plotting the graph
plt.ylabel('frequency')           # give x_dim label
plt.xlabel(' Ranking for char unigram')   # give y_dim label
plt.savefig('Ques3/zipfian/char_unigram.png')   # save file


# for char bigram
char_freq_list_b = []
 

#open file and took those words whose first letter is number
with open('Ques3/char_ngram/char_bigram.txt') as f:
    for line in f:
        temp = ''
        for word in line.split():
            if word[0] in num:
                char_freq_list_b.append(int(word))
                
x_dim = [int(ind) for ind in range(1,101)]
# len(x_dim)
# len(char_freq_list_b)
figure(figsize=(14, 8), dpi=120)
plt.plot(x_dim, char_freq_list_b)   # plotting the graph
plt.ylabel('frequency')           # give x_dim label
plt.xlabel(' Ranking for char bigram')   # give y_dim label
plt.savefig('Ques3/zipfian/char_bigram.png')   # save file


# for char trigram

char_freq_list_t = []
 

#open file and took those words whose first letter is number
with open('Ques3/char_ngram/char_trigram.txt') as f:
    for line in f:
        temp = ''
        for word in line.split():
            if word[0] in num:
                char_freq_list_t.append(int(word))
                
x_dim = [int(ind) for ind in range(1,101)]
# len(x_dim)
# len(char_freq_list_b)
figure(figsize=(14, 8), dpi=120)
plt.plot(x_dim, char_freq_list_t)   # plotting the graph
plt.ylabel('frequency')           # give x_dim label
plt.xlabel(' Ranking for char trigram')   # give y_dim label
plt.savefig('Ques3/zipfian/char_trigram.png')   # save file



# for char quadrigram
char_freq_list_q = []
 

#open file and took those words whose first letter is number
with open('Ques3/char_ngram/char_quadrigram.txt') as f:
    for line in f:
        temp = ''
        for word in line.split():
            if word[0] in num:
                char_freq_list_q.append(int(word))
                
x_dim = [int(ind) for ind in range(1,101)]
# len(x_dim)
# len(char_freq_list_b)
figure(figsize=(14, 8), dpi=120)
plt.plot(x_dim, char_freq_list_q)   # plotting the graph
plt.ylabel('frequency')           # give x_dim label
plt.xlabel(' Ranking for char quadrigram')   # give y_dim label
plt.savefig('Ques3/zipfian/char_quadrigram.png')   # save file


# for word unigram
word_freq_list_u = []
 

#open file and took those words whose first letter is number
with open('Ques3/word_ngram/word_unigram.txt') as f:
    for line in f:
        temp = ''
        for word in line.split():
            if word[0] in num:
                word_freq_list_u.append(int(word))
                
x_dim = [int(ind) for ind in range(1,101)]
# len(x_dim)
# len(char_freq_list_b)
figure(figsize=(14, 8), dpi=120)
plt.plot(x_dim, word_freq_list_u)   # plotting the graph
plt.ylabel('frequency')           # give x_dim label
plt.xlabel(' Ranking for word unigram')   # give y_dim label
plt.savefig('Ques3/zipfian/word_unigram.png')   # save file


# for word bigram

word_freq_list_b = []
 

#open file and took those words whose first letter is number
with open('Ques3/word_ngram/word_bigram.txt') as f:
    for line in f:
        temp = ''
        for word in line.split():
            if word[0] in num:
                word_freq_list_b.append(int(word))
                
x_dim = [int(ind) for ind in range(1,101)]
# len(x_dim)
# len(word_freq_list_b)
figure(figsize=(14, 8), dpi=120)
plt.plot(x_dim, word_freq_list_b)   # plotting the graph
plt.ylabel('frequency')           # give x_dim label
plt.xlabel(' Ranking for word bigram')   # give y_dim label
plt.savefig('Ques3/zipfian/word_bigram.png')   # save file


# for word trigram

word_freq_list_t = []
 

#open file and took those words whose first letter is number
with open('Ques3/word_ngram/word_bigram.txt') as f:
    for line in f:
        temp = ''
        for word in line.split():
            if word[0] in num:
                word_freq_list_t.append(int(word))
                
x_dim = [int(ind) for ind in range(1,101)]
# len(x_dim)
# len(word_freq_list_b)
figure(figsize=(14, 8), dpi=120)
plt.plot(x_dim, word_freq_list_t)   # plotting the graph
plt.ylabel('frequency')           # give x_dim label
plt.xlabel(' Ranking for word trigram')   # give y_dim label
plt.savefig('Ques3/zipfian/word_trigram.png')   # save file



# for syllable unigram
syllable_freq_list_u = []
 

#open file and took those words whose first letter is number
with open('Ques3/syllable/unigram_syll.txt') as f:
    for line in f:
        temp = ''
        for word in line.split():
            if word[0] in num:
                syllable_freq_list_u.append(int(word))
                
x_dim = [int(ind) for ind in range(1,101)]
# len(x_dim)
# len(word_freq_list_b)
figure(figsize=(14, 8), dpi=120)
plt.plot(x_dim, syllable_freq_list_u)   # plotting the graph
plt.ylabel('frequency')           # give x_dim label
plt.xlabel(' Ranking for syllable unigram')   # give y_dim label
plt.savefig('Ques3/zipfian/syllable_unigram.png')   # save file


# for syllable bigram

syllable_freq_list_b = []
 

#open file and took those words whose first letter is number
with open('Ques3/syllable/bigram_syll.txt') as f:
    for line in f:
        temp = ''
        for word in line.split():
            if word[0] in num:
                syllable_freq_list_b.append(int(word))
                
x_dim = [int(ind) for ind in range(1,101)]
# len(x_dim)
# len(word_freq_list_b)
figure(figsize=(14, 8), dpi=120)
plt.plot(x_dim, syllable_freq_list_b)   # plotting the graph
plt.ylabel('frequency')           # give x_dim label
plt.xlabel(' Ranking for syllable bigram')   # give y_dim label
plt.savefig('Ques3/zipfian/syllable_bigram.png')   # save file



# for syllable trigram

syllable_freq_list_t = []
 

#open file and took those words whose first letter is number
with open('Ques3/syllable/trigram_syll.txt') as f:
    for line in f:
        temp = ''
        for word in line.split():
            if word[0] in num:
                syllable_freq_list_t.append(int(word))
                
x_dim = [int(ind) for ind in range(1,101)]
# len(x_dim)
# len(word_freq_list_b)
figure(figsize=(14, 8), dpi=120)
plt.plot(x_dim, syllable_freq_list_t)   # plotting the graph
plt.ylabel('frequency')           # give x_dim label
plt.xlabel(' Ranking for syllable trigram')   # give y_dim label
plt.savefig('Ques3/zipfian/syllable_trigram.png')   # save file


