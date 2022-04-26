# from syllable import count_ngram


# file_names = []
# for i in range(0,22):
#     file_names.append('../../data/hi/hi_{:02d}.txt'.format(i))

# count_ngram(2,file_names, 'Ques3/syllable/bigram_syll.txt')


# just for test purpose
from syllable import count_ngram
file_names = []
for i in range(0,1):
    file_names.append('test.txt')

count_ngram(2,file_names, 'output2.txt')