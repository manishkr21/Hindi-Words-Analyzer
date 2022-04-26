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

# to generate the quadrigrams
preprocess_list = []
aa_char = 'अ#'
quadri_freq_list = []
for i in range(0,22):    # files are split into 22 parts
    temp_list = []
    temp = {}
    # with open('data/hi/hi_{:02d}.txt'.format(i), encoding='UTF-8',errors = 'ignore') as file:
    with open('test.txt', encoding='UTF-8',errors = 'ignore') as file:
        for i,this_line in enumerate(file):
            for punc in (hi_punc):
                this_line = this_line.replace(punc,'') # remove the punctuation
            line = [ltr for ltr in this_line]

            ind = 0
            while ind < len(line)-4:
                # some rules to considers
                if line[ind+1] == '्':
                    line.pop(ind+1)
                    line[ind] = line[ind]+'्'
                if (line[ind] in hi_consonants) and (line[ind+1] in hi_depvowels) and (line[ind+1] != '्'):
                    line[ind] = line[ind]+'्'
                if (line[ind] in hi_consonants) and (line[ind+1] in (hi_consonants.union(hi_indvowels))) and (line[ind+1] != '्'):
                    line[ind] = line[ind]+'्'
                    line.insert(ind+1,aa_char)  

                # dictionary to take key and value pair of quadrigram to its frequency
                if (line[ind],line[ind+1],line[ind+2],line[ind+3]) not in temp.keys():
                    temp[(line[ind],line[ind+1],line[ind+2],line[ind+3])] = 1
                else:
                    temp[(line[ind],line[ind+1],line[ind+2],line[ind+3])] += 1     
                
                ind += 1
            
            #print date and time to each millions
            if i%1000000 == 0:
                print(datetime.now(),i)
            
        # file.close()
        gc.collect()

    quadri_freq_list = sorted(temp.items(), key = lambda x:(x[1]),reverse = True )    
    quadri_freq_list = quadri_freq_list[0:2500]   # consider only top 2500 of each file

quadri_freq_dict = {}
# merge current 2500 to previous accumulated 2500 quadrigrams
for i in range(len(quadri_freq_list)):
    if quadri_freq_list[i][0] not in quadri_freq_dict.keys():
        quadri_freq_dict[quadri_freq_list[i][0]] = quadri_freq_list[i][1]
    else:
        quadri_freq_dict[quadri_freq_list[i][0]] += quadri_freq_list[i][1]  

quadri_freq_dict = sorted(quadri_freq_dict.items(), key = lambda x:(x[1]),reverse = True )

# take only top 100 
quadri_freq_dict = quadri_freq_dict[0:100]

# save them into txt file
# with open('Ques3/char_ngram/char_quadrigram.txt', 'w') as of:
with open('output4.txt', 'w') as of:
    for word, freq in quadri_freq_dict:
        of.write('{} - {}\n'.format(word, freq))
