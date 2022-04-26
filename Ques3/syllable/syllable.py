from collections import deque, defaultdict
from datetime import datetime
import pickle

hi_indvowels = {'ऄ','अ','आ','इ','ई','उ','ऊ','ऋ','ऌ','ऍ','ऎ','ए','ऐ','ऑ','ऒ','ओ','औ','अं','अः'}

hi_depvowels = {'ा','ि','ी','ु','ू','ृ','ॄ','ॅ','ॆ','े','ै','ॉ','ॊ','ो','ौ','ं','ं','ऀ', 'ँ', 'ं', 'ः', '़', 'ऽ', '्', 'ॎ', 'ॏ', 'ॐ', '॑', '॒', '॓', '॔', 'ॕ'}
hi_consonants = {'क','ख','ग','घ','ड','ङ','च','छ','ज','झ','ञ','ट','ठ','ड','ढ','ण','त','थ','द',
                    'ध','न','ऩ','प','फ','ब','भ','म','य','र','ऱ','ल','ळ','ऴ','व','श','ष','स','ह','क्ष','त्र','ज्ञ'}
hi_numerals = {'०','१','२','३','४','५','६','७','८','९','.'}
hi_depvow_mapping = {'ा':'आ','ि':'इ','ी':'ई','ु':'उ','ू':'ऊ',
                    'ृ':'ऋ','ॄ':'ॠ','ॅ':'ऍ','ॆ':'ऎ','े':'ए','ै':'ऐ','ॉ':'ऑ','ॊ':'ऒ','ो':'ओ','ौ':'औ'}

hi_punc = {'।','|',',','॥',':',';','–',')','(','…','_','०',':-','!','?','“','”',',,','S','.',"'",'’'}
halant = '्'


def split_syllable(word):
    s_list = []

    word = [ltr for ltr in word]
    word.append(' ')
    
    ind = 0

    while ind < len(word) -1 :
        
        if (word[ind] in hi_consonants) and word[ind+1] == ' ':
            s_list.append(word[ind])
            
        if word[ind+1] == halant:
            if word[ind+2] == ' ':
                s_list.append(word[ind]+word[ind+1])
                ind += 1
            elif word[ind+2] != ' ' and word[ind+3] != ' ':
                
                if (word[ind+2] in hi_consonants) and (word[ind+3] in (hi_depvowels)):
                    s_list.append(word[ind]+word[ind+1]+word[ind+2]+word[ind+3])
                    ind += 3               
                    
                elif (word[ind+2] in hi_consonants) and (word[ind+3] in hi_consonants):
                    
                    s_list.append(word[ind]+word[ind+1]+word[ind+2])
                    ind += 2
                    
        elif (word[ind] in hi_consonants) and (word[ind+1] in (hi_depvowels )):

            if word[ind+2] != ' ' and (word[ind+2] in (hi_depvowels)):
                s_list.append(word[ind]+word[ind+1]+word[ind+2])
                ind +=2
            else:
                s_list.append(word[ind]+ word[ind+1])
                ind += 1
                        
        elif (word[ind] in hi_consonants) and (word[ind+1] in hi_consonants):
            s_list.append(word[ind])

        elif (word[ind] in hi_indvowels) and (word[ind+1] in hi_depvowels):
            s_list.append(word[ind]+ word[ind+1])
            ind += 1
        
        elif word[ind] in (hi_depvowels.union(hi_indvowels)):
            s_list.append(word[ind])

        ind +=1
            
    
    return s_list
            

def get_syllables(line):
    for word in line.strip().split():
        for syllable in split_syllable(word):
            yield syllable


def count_ngram(n, file_names, out_file_name):
    files = [open(file_name) for file_name in file_names]
    counts = defaultdict(int)
    window = deque()


    for file in files:
        print(file)
        for line in file:
            for syllable in get_syllables(line):
                while len(window) != n:
                    window.append(syllable)
                
                counts[''.join(s for s in window)] += 1
                window.popleft()
           
    top_200 = sorted(counts.items(), reverse=True, key=lambda x: x[1])
    with open(out_file_name, 'w') as of:
        for word, freq in top_200:
            of.write('{} - {}\n'.format(word, freq))


