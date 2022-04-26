from datetime import datetime
import pickle
import gc

# sets of the hindi letters
hi_indvowels = {'ऄ','अ','आ','इ','ई','उ','ऊ','ऋ','ऌ','ऍ','ऎ','ए','ऐ','ऑ','ऒ','ओ','औ','अं','अः'}

hi_depvowels = {'ा','ि','ी','ु','ू','ृ','ॄ','ॅ','ॆ','े','ै','ॉ','ॊ','ो','ौ','ं','ऀ', 'ँ', 'ं', 'ः', '़', 'ऽ', '्', 'ॎ', 'ॏ', 'ॐ', '॑', '॒', '॓', '॔', 'ॕ'}
hi_consonants = {'क','ख','ग','घ','ड','ङ','च','छ','ज','झ','ञ','ट','ठ','ड','ढ','ण','त','थ','द',
                    'ध','न','ऩ','प','फ','ब','भ','म','य','र','ऱ','ल','ळ','ऴ','व','श','ष','स','ह','क्ष','त्र','ज्ञ'}
hi_numerals = {'०','१','२','३','४','५','६','७','८','९','.'}
hi_depvow_mapping = {'ा':'आ','ि':'इ','ी':'ई','ु':'उ','ू':'ऊ',
                    'ृ':'ऋ','ॄ':'ॠ','ॅ':'ऍ','ॆ':'ऎ','े':'ए','ै':'ऐ','ॉ':'ऑ','ॊ':'ऒ','ो':'ओ','ौ':'औ'}

hi_punc = {'।','|',',','॥',':',';','–',')','(','…','_','०',':-','!','?','“','”',',,','S','.',"'",'’','0','1','2','3','4','5','6','6','7','8','9','-','a','b','c','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','‘','"','%','—','१','>','à',']', '२','#',''}
halant = '्'


# to generate the bigrams
preprocess_list = []
aa_char = 'अ#'
bi_freq_list = []
for i in range(0,22):    # files are splitted i.e. in 22 parts so give according to that 
    temp_list = []
    temp = {}
    # opening the files with UTF encoding and ignore the errors
    # with open('data/hi/hi_{:02d}.txt'.format(i), encoding='UTF-8',errors = 'ignore') as file:
    with open('test.txt', encoding='UTF-8',errors = 'ignore') as file:
        for i,this_line in enumerate(file):
            for punc in (hi_punc):
                this_line = this_line.replace(punc,'')    # remove the punchuations
            line = [ltr for ltr in this_line]             # convert the string into list

            ind = 0
            while ind < len(line)-1:        # iterate untill line length become one less than its actual length
            
                if line[ind+1] == '्':       # if halant comes then remove it and add it to line[ind] indices
                    line.pop(ind+1)
                    line[ind] = line[ind]+'्'
                if (line[ind] in hi_consonants) and (line[ind+1] in hi_depvowels) and (line[ind+1] != '्'):     # rule when next indices is matra not halant
                    line[ind] = line[ind]+'्'
                if (line[ind] in hi_consonants) and (line[ind+1] in (hi_consonants.union(hi_indvowels))) and (line[ind+1] != '्'):  # rule when next indices is consonant and vowels
                    line[ind] = line[ind]+'्'
                    line.insert(ind+1,aa_char)  

                if (line[ind],line[ind+1]) not in temp.keys():      # making dictionary of result, i.e top character bigram
                    temp[(line[ind],line[ind+1])] = 1
                else:
                    temp[(line[ind],line[ind+1])] += 1     
                
                ind += 1

            if i%1000000 == 0:
                print(datetime.now(),i)
            
        # file.close()
        gc.collect()

    bi_freq_list = sorted(temp.items(), key = lambda x:(x[1]),reverse = True )
    bi_freq_list = bi_freq_list[0:2500]        # take top 2500 bigram of each files 

bi_freq_dict = {}
# merge current file top 2500 to previous accumulated top 2500
for i in range(len(bi_freq_list)):
    if bi_freq_list[i][0] not in bi_freq_dict.keys():
        bi_freq_dict[bi_freq_list[i][0]] = bi_freq_list[i][1]
    else:
        bi_freq_dict[bi_freq_list[i][0]] += bi_freq_list[i][1]  

bi_freq_dict = sorted(bi_freq_dict.items(), key = lambda x:(x[1]),reverse = True )

bi_freq_dict = bi_freq_dict[0:100]     # finally consider only top 100 

# with open('Ques3/char_ngram/char_bigram.txt', 'w') as of:    # save the file in txt format
with open('output2.txt', 'w') as of: 
    for word, freq in bi_freq_dict:
        of.write('{} - {}\n'.format(word, freq))