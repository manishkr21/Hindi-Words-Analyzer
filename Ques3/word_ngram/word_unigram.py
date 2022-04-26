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

# for Unigrams
for i in range(0,22):
    freq_dict = {}
    temp = {}
    with open('data/hi/hi_{:02d}.txt'.format(i), encoding='UTF-8',errors = 'ignore') as file:
        for i,line in enumerate(file):
            for punc in hi_punc:
                line = line.replace(punc,'')
            words = line.split()
            for ind in range(0,len(words)):

                if not type(ind) == range:

                    if words[ind] not in freq_dict.keys():
                            freq_dict[words[ind]] = 1
                    else:
                            freq_dict[words[ind]] += 1

            if i%1000000 == 0:
                print(datetime.now(),i)
        temp = sorted(freq_dict.items(), key = lambda x:(x[1]),reverse = True )

    uni_freq_list = temp[0:2500]

uni_freq_dict = {}

for i in range(len(uni_freq_list)):
    if uni_freq_list[i][0] not in uni_freq_dict.keys():
        uni_freq_dict[uni_freq_list[i][0]] = uni_freq_list[i][1]
    else:
        uni_freq_dict[uni_freq_list[i][0]] += uni_freq_list[i][1]  

uni_freq_dict = sorted(uni_freq_dict.items(), key = lambda x:(x[1]),reverse = True )


with open('Ques3/word_ngram/word_unigram.txt', 'w') as of:
    for word, freq in uni_freq_dict:
        of.write('{} - {}\n'.format(word, freq))



