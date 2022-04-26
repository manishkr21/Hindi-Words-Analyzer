from datetime import datetime
import pickle
import gc

# sets of hindi letters
hi_indvowels = {'ऄ','अ','आ','इ','ई','उ','ऊ','ऋ','ऌ','ऍ','ऎ','ए','ऐ','ऑ','ऒ','ओ','औ','अं','अः'}

hi_depvowels = {'ा','ि','ी','ु','ू','ृ','ॄ','ॅ','ॆ','े','ै','ॉ','ॊ','ो','ौ','ं','ऀ', 'ँ', 'ं', 'ः', '़', 'ऽ', '्', 'ॎ', 'ॏ', 'ॐ', '॑', '॒', '॓', '॔', 'ॕ'}
hi_consonants = {'क','ख','ग','घ','ड','ङ','च','छ','ज','झ','ञ','ट','ठ','ड','ढ','ण','त','थ','द',
                    'ध','न','ऩ','प','फ','ब','भ','म','य','र','ऱ','ल','ळ','ऴ','व','श','ष','स','ह','क्ष','त्र','ज्ञ'}
hi_numerals = {'०','१','२','३','४','५','६','७','८','९','.'}
hi_depvow_mapping = {'ा':'आ','ि':'इ','ी':'ई','ु':'उ','ू':'ऊ',
                    'ृ':'ऋ','ॄ':'ॠ','ॅ':'ऍ','ॆ':'ऎ','े':'ए','ै':'ऐ','ॉ':'ऑ','ॊ':'ऒ','ो':'ओ','ौ':'औ'}

hi_punc = {'।','|',',','॥',':',';','–',')','(','…','_','०',':-','!','?','“','”',',,','S','.',"'",'’','0','1','2','3','4','5','6','6','7','8','9','-','a','b','c','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','‘','"','%','—','१','>','à',']', '२','#',''}
halant = '्'


# to generate the unigrams
preprocess_list = []
aa_char = 'अ#'
uni_freq_list = []
for i in range(0,22):   # due to 22 files split
    temp_list = []
    temp = {}
    # open file in UTF-8 encoding and ignore the errors
    # with open('data/hi/hi_{:02d}.txt'.format(i), encoding='UTF-8',errors = 'ignore') as file:
    with open('test.txt'.format(i), encoding='UTF-8',errors = 'ignore') as file:
        for i,this_line in enumerate(file):
            for punc in (hi_punc):
                this_line = this_line.replace(punc,'')    # remove the punctuations
            line = [ltr for ltr in this_line]              # convert strings of line into list of characters

            ind = 0
            while ind < len(line)-1:
                # rule to consider the halant
                if line[ind+1] == '्':
                    line.pop(ind+1)
                    line[ind] = line[ind]+'्'
                if (line[ind] in hi_consonants) and (line[ind+1] in hi_depvowels) and (line[ind+1] != '्'):
                    line[ind] = line[ind]+'्'
                if (line[ind] in hi_consonants) and (line[ind+1] in (hi_consonants.union(hi_indvowels))) and (line[ind+1] != '्'):
                    line[ind] = line[ind]+'्'
                    line.insert(ind+1,aa_char)  

                if line[ind] not in temp.keys():
                    temp[line[ind]] = 1
                else:
                    temp[line[ind]] += 1     
                
                ind += 1
            # will print time at every million
            if i%1000000 == 0:
                print(datetime.now(),i)
            
        # file.close()
        gc.collect()

    uni_freq_list = sorted(temp.items(), key = lambda x:(x[1]),reverse = True )
    uni_freq_list = uni_freq_list[0:2500] # take top 2500 at each files

uni_freq_dict = {}

# merge the current top 2500 unigrams to previous accumulated 2500 unigrams 
for i in range(len(uni_freq_list)):
    if uni_freq_list[i][0] not in uni_freq_dict.keys():
        uni_freq_dict[uni_freq_list[i][0]] = uni_freq_list[i][1]
    else:
        uni_freq_dict[uni_freq_list[i][0]] += uni_freq_list[i][1]  

uni_freq_dict = sorted(uni_freq_dict.items(), key = lambda x:(x[1]),reverse = True )

# take only top 100 among all the files
uni_freq_dict = uni_freq_dict[0:100]

# print them into txt file
# with open('Ques3/char_ngram/char_unigram.txt', 'w') as of:
with open('output.txt', 'w') as of:
    for word, freq in uni_freq_dict:
        of.write('{} - {}\n'.format(word, freq))
        
