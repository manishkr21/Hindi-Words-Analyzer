from datetime import datetime
import pickle


hi_indvowels = {'ऄ','अ','आ','इ','ई','उ','ऊ','ऋ','ऌ','ऍ','ऎ','ए','ऐ','ऑ','ऒ','ओ','औ','अं','अः'}

hi_depvowels = {'ा','ि','ी','ु','ू','ृ','ॄ','ॅ','ॆ','े','ै','ॉ','ॊ','ो','ौ','ं','ऀ', 'ँ', 'ं', 'ः', '़', 'ऽ', '्', 'ॎ', 'ॏ', 'ॐ', '॑', '॒', '॓', '॔', 'ॕ'}
hi_consonants = {'क','ख','ग','घ','ड','ङ','च','छ','ज','झ','ञ','ट','ठ','ड','ढ','ण','त','थ','द',
                    'ध','न','ऩ','प','फ','ब','भ','म','य','र','ऱ','ल','ळ','ऴ','व','श','ष','स','ह','क्ष','त्र','ज्ञ'}
hi_numerals = {'०','१','२','३','४','५','६','७','८','९','.'}
hi_depvow_mapping = {'ा':'आ','ि':'इ','ी':'ई','ु':'उ','ू':'ऊ',
                    'ृ':'ऋ','ॄ':'ॠ','ॅ':'ऍ','ॆ':'ऎ','े':'ए','ै':'ऐ','ॉ':'ऑ','ॊ':'ऒ','ो':'ओ','ौ':'औ'}

hi_punc = {'।','|',',','॥',':',';','–',')','(','…','_','०',':-','!','?','“','”',',,','S','.',"'",'’'}
halant = '्'



# for trigrams

for i in range(0,22):
    freq_dict = {}
    temp = {}
    with open('data/hi/hi_{:02d}.txt'.format(i), encoding='UTF-8',errors = 'ignore') as file:
        for i,line in enumerate(file):
            for punc in hi_punc:
                line = line.replace(punc,'')
            words = line.split()
            for ind in range(0,len(words)-2):

                if (words[ind],words[ind+1],words[ind+2]) not in freq_dict.keys():
                        freq_dict[(words[ind],words[ind+1],words[ind+2])] = 1
                else:
                        freq_dict[(words[ind],words[ind+1],words[ind+2])] += 1

            if i%1000000 == 0:
                print(datetime.now(),i)
        temp = sorted(freq_dict.items(), key = lambda x:(x[1]),reverse = True )

    tri_freq_list = temp[0:2500]

tri_freq_dict = {}

for i in range(len(tri_freq_list)):
    if tri_freq_list[i][0] not in tri_freq_dict.keys():
        tri_freq_dict[tri_freq_list[i][0]] = tri_freq_list[i][1]
    else:
        tri_freq_dict[tri_freq_list[i][0]] += tri_freq_list[i][1]  

tri_freq_dict = sorted(tri_freq_dict.items(), key = lambda x:(x[1]),reverse = True )

# pickle.dump(tri_freq_dict[0:100],open('word_trigram_dict.dat','wb'))

with open('Ques3/word_ngram/word_trigram.txt', 'w') as of:
    for word, freq in tri_freq_dict:
        of.write('{} - {}\n'.format(word, freq))


