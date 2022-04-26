
import pandas as pd
import pickle
import numpy as np



words_gt = []
# to make the list of list which contain the list of word pair with ground truth
with open('Word similarity/hindi.txt', encoding = 'utf-8', errors = 'ignore') as file:
    words_gt = [word.strip().split(',') for word in file if word.strip() != '']


gt_list1 = []
gt_list2 = []
gt_list1 = [word[0].strip() for word in words_gt]
gt_list2 = [word[1].strip() for word in words_gt]
gt = [word[2].strip() for word in words_gt]



accuracy_for_glove = pd.DataFrame(columns = ['0.4', '0.5', '0.6', '0.7', '0.8'], index = ['50', '100', '200', '300'])

def find_cos_sim(list1, list2):     # takes two list return their cosine similarity after converting them into vector
    vector1 = np.array(list1)
    vector2 = np.array(list2)
    normalized_v1 = vector1 / np.sqrt(np.sum(vector1**2))
    normalized_v2 = vector2 / np.sqrt(np.sum(vector2**2))
    cosine_sim = np.dot(normalized_v1 , normalized_v2 )
    return cosine_sim

cosim_of_each_word = []
dim_glove = ['50', '100', '200', '300']
threshold_glove = ['0.4', '0.5', '0.6', '0.7', '0.8']

glove_vector_50 = pickle.load(open('Ques1/glove_vector_50.dat', 'rb'))
glove_vector_100 = pickle.load(open('Ques1/glove_vector_100.dat', 'rb'))
glove_vector_200 = pickle.load(open('Ques1/glove_vector_200.dat', 'rb'))
glove_vector_300 = pickle.load(open('Ques1/glove_vector_300.dat', 'rb'))
# print(arr_dict['रेलगाड़ी'])

# for col,ind in zip(dim, threshold):
for dim in dim_glove:
    for threshold in threshold_glove:
    
        correct_prediction = 0
        if dim == '50':

            # define dataframe to store the value of required format
            df = pd.DataFrame(columns = ['Word1','Word2','Similarity Score','Ground Truth', 'Label_similar', 'label_correct'])

            for i in range(len(gt_list1)):

                cs = find_cos_sim(glove_vector_50[gt_list1[i]], glove_vector_50[gt_list2[i]])

                if (cs*10 >= float(threshold)*10 and float(gt[i]) >= float(threshold)*10):
                    temp_correct = 1      # to track the correctly prediction
                    temp_similar = 1       # to track the similar prediction
                    correct_prediction += 1
                elif (cs*10 < float(threshold)*10 and float(gt[i]) < float(threshold)*10):
                    temp_correct = 1
                    temp_similar = 0
                    correct_prediction += 1
                else:
                    temp_correct = 0
                    temp_similar = 0

                # add the data rowwise into dataframe
                df.loc[i] = [gt_list1[i],gt_list2[i],cs*10,gt[i],temp_similar,temp_correct]


                # if(cs * 10 >= float(threshold)*10 and float(gt[i]) >= float(threshold)*10) or (cs * 10 < float(threshold)*10 and float(gt[i]) < float(threshold)*10):
                #     # true_pos += 1
                #     correct_prediction += 1
                #     temp = 1
                # else:
                #     # true_neg += 1
                #     temp = 0
                # # add the data rowwise into dataframe
                # df.loc[i] = [gt_list1[i],gt_list2[i],cs*10,gt[i],temp]
            A = (correct_prediction)/len(words_gt)*100
            df = df.append(['Accuracy  = ',A])   # append accuracy to dataframe

            # make the csv file for dataFrame
            df.to_csv('Ques1/glove/Q1_{0}_glove_{1}.csv'.format(dim,int(float(threshold)*10)),index = False)

        if dim == '100':

            # define dataframe to store the value of required format
            df = pd.DataFrame(columns = ['Word1','Word2','Similarity Score','Ground Truth', 'Label_similar', 'label_correct'])

            for i in range(len(gt_list1)):

                cs = find_cos_sim(glove_vector_100[gt_list1[i]], glove_vector_100[gt_list2[i]])

                if (cs*10 >= float(threshold)*10 and float(gt[i]) >= float(threshold)*10):
                    temp_correct = 1      # to track the correctly prediction
                    temp_similar = 1       # to track the similar prediction
                    correct_prediction += 1
                elif (cs*10 < float(threshold)*10 and float(gt[i]) < float(threshold)*10):
                    temp_correct = 1
                    temp_similar = 0
                    correct_prediction += 1
                else:
                    temp_correct = 0
                    temp_similar = 0

                # add the data rowwise into dataframe
                df.loc[i] = [gt_list1[i],gt_list2[i],cs*10,gt[i],temp_similar,temp_correct]
            A = (correct_prediction)/len(words_gt) * 100
            df = df.append(['Accuracy  = ',A])   # append accuracy to dataframe

            # make the csv file for dataFrame
            df.to_csv('Ques1/glove/Q1_{0}_glove_{1}.csv'.format(dim,int(float(threshold)*10)),index = False)

        if dim == '200':

            # define dataframe to store the value of required format
            df = pd.DataFrame(columns = ['Word1','Word2','Similarity Score','Ground Truth', 'Label_similar', 'label_correct'])

            for i in range(len(gt_list1)):

                cs = find_cos_sim(glove_vector_200[gt_list1[i]], glove_vector_200[gt_list2[i]])

                if (cs*10 >= float(threshold)*10 and float(gt[i]) >= float(threshold)*10):
                    temp_correct = 1      # to track the correctly prediction
                    temp_similar = 1       # to track the similar prediction
                    correct_prediction += 1
                elif (cs*10 < float(threshold)*10 and float(gt[i]) < float(threshold)*10):
                    temp_correct = 1
                    temp_similar = 0
                    correct_prediction += 1
                else:
                    temp_correct = 0
                    temp_similar = 0

                # add the data rowwise into dataframe
                df.loc[i] = [gt_list1[i],gt_list2[i],cs*10,gt[i],temp_similar,temp_correct]
            A = (correct_prediction)/len(words_gt) * 100
            df = df.append(['Accuracy  = ',A])   # append accuracy to dataframe

            # make the csv file for dataFrame
            df.to_csv('Ques1/glove/Q1_{0}_glove_{1}.csv'.format(dim,int(float(threshold)*10)),index = False)


        if dim == '300':

            # define dataframe to store the value of required format
            df = pd.DataFrame(columns = ['Word1','Word2','Similarity Score','Ground Truth', 'Label_similar', 'label_correct'])

            for i in range(len(gt_list1)):

                cs = find_cos_sim(glove_vector_300[gt_list1[i]], glove_vector_300[gt_list2[i]])

                if (cs*10 >= float(threshold)*10 and float(gt[i]) >= float(threshold)*10):
                    temp_correct = 1      # to track the correctly prediction
                    temp_similar = 1       # to track the similar prediction
                    correct_prediction += 1
                elif (cs*10 < float(threshold)*10 and float(gt[i]) < float(threshold)*10):
                    temp_correct = 1
                    temp_similar = 0
                    correct_prediction += 1
                else:
                    temp_correct = 0
                    temp_similar = 0

                # add the data rowwise into dataframe
                df.loc[i] = [gt_list1[i],gt_list2[i],cs*10,gt[i],temp_similar,temp_correct]
            A = (correct_prediction)/len(words_gt) * 100
            df = df.append(['Accuracy  = ',A])   # append accuracy to dataframe

            # make the csv file for dataFrame
            df.to_csv('Ques1/glove/Q1_{0}_glove_{1}.csv'.format(dim,int(float(threshold)*10)),index = False)
