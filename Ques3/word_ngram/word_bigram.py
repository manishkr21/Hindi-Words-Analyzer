from datetime import datetime
import pickle


hi_indvowels = ['ऄ','अ','आ','इ','ई','उ','ऊ','ऋ','ऌ','ऍ','ऎ','ए','ऐ','ऑ','ऒ','ओ','औ','अं','अः']
hi_signs = ['0x900','0x901','0x902','0x903','0x93C','0x93D','0x94D','0x94E','0x94F','0x950','0x951','0x952','0x953','0x954','0x955']
hi_depvowels = ['ा','ि','ी','ु','ू','ृ','ॄ','ॅ','ॆ','े','ै','ॉ','ॊ','ो','ौ']
hi_consonants = ['क','ख','ग','घ','ङ','च','छ','ज','झ','ञ','ट','ठ','ड','ढ','ण','त','थ','द',
                    'ध','न','ऩ','प','फ','ब','भ','म','य','र','ऱ','ल','ळ','ऴ','व','श','ष','स','ह','क्ष','त्र','ज्ञ']
hi_numerals = ['०','१','२','३','४','५','६','७','८','९','.']
hi_depvow_mapping = {'ा':'आ','ि':'इ','ी':'ई','ु':'उ','ू':'ऊ',
                    'ृ':'ऋ','ॄ':'ॠ','ॅ':'ऍ','ॆ':'ऎ','े':'ए','ै':'ऐ','ॉ':'ऑ','ॊ':'ऒ','ो':'ओ','ौ':'औ'}
hi_punc = ['।','|',',','॥',':',';','–',')','(','…','_','०',':-','!','?','“','”',',,','S','.',"'",'’']

# for bigrams
for i in range(0,22):
    freq_dict = {}
    temp = {}
    with open('data/hi/hi_{:02d}.txt'.format(i), encoding='UTF-8',errors = 'ignore') as file:
        for i,line in enumerate(file):
            for punc in hi_punc:
                line = line.replace(punc,'')
            words = line.split()
            for ind in range(0,len(words)-1):

                if not type(ind) == range:

                    if (words[ind],words[ind+1]) not in freq_dict.keys():
                            freq_dict[(words[ind],words[ind+1])] = 1
                    else:
                            freq_dict[(words[ind],words[ind+1])] += 1

            if i%1000000 == 0:
                print(datetime.now(),i)
        temp = sorted(freq_dict.items(), key = lambda x:(x[1]),reverse = True )

    bi_freq_list = temp[0:2500]

bi_freq_dict = {}

for i in range(len(bi_freq_list)):
    if bi_freq_list[i][0] not in bi_freq_dict.keys():
        bi_freq_dict[bi_freq_list[i][0]] = bi_freq_list[i][1]
    else:
        bi_freq_dict[bi_freq_list[i][0]] += bi_freq_list[i][1]  

bi_freq_dict = sorted(bi_freq_dict.items(), key = lambda x:(x[1]),reverse = True )

# pickle.dump(bi_freq_dict[0:100],open('word_bigram_dict.dat','wb'))

with open('Ques3/word_ngram/word_bigram.txt', 'w') as of:
    for word, freq in bi_freq_dict:
        of.write('{} - {}\n'.format(word, freq))

