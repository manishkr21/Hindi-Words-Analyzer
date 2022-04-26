import pickle
from sqlite3 import Row
import pandas as pd
# Import writer class from csv module
from csv import writer


#load already created datastructure as dict of dict of dict    {50:{0.4:{(word1, word2,ground truth):co_sim,...},...},...}
cosim_of_cbow = pickle.load(open('Ques1/cosim_of_cbow.dat','rb'))


for dim in cosim_of_cbow:     # iterate through dimensions
    for threshold in cosim_of_cbow[dim]:  # iterate through threshold
       
        correct_prediction = 0
    
        if dim == '50':
            # define dataframe to store the value of required format
            df = pd.DataFrame(columns = ['Word1','Word2','Similarity Score','Ground Truth', 'Label_similar', 'label_correct'])

            for i,(pair,cs) in enumerate(cosim_of_cbow[dim][threshold].items()):
                # to check for the correct prediction 
                
                if (cs*10 >= float(threshold)*10 and float(pair[2]) >= float(threshold)*10):
                    temp_correct = 1      # to track the correctly prediction
                    temp_similar = 1       # to track the similar prediction
                    correct_prediction += 1
                elif (cs*10 < float(threshold)*10 and float(pair[2]) < float(threshold)*10):
                    temp_correct = 1
                    temp_similar = 0
                    correct_prediction += 1
                else:
                    temp_correct = 0
                    temp_similar = 0

                # add the data rowwise into dataframe
                df.loc[i] = [pair[0],pair[1],cs*10,pair[2],temp_similar,temp_correct]
            
            # find the accuracy 
            A = correct_prediction/len(cosim_of_cbow[dim][threshold]) * 100
            df = df.append(['Accuracy  = ',A])   # append accuracy to dataframe

            # make the csv file for dataFrame
            df.to_csv('Ques1/cbow/Q1_{0}_cbow_{1}.csv'.format(dim,int(float(threshold)*10)),index = False)

        if dim == '100':
            # define dataframe to store the value of required format
            df = pd.DataFrame(columns = ['Word1','Word2','Similarity Score','Ground Truth', 'Label_similar', 'label_correct'])

            for i,(pair,cs) in enumerate(cosim_of_cbow[dim][threshold].items()):
                # to check for the correct prediction 
                if (cs*10 >= float(threshold)*10 and float(pair[2]) >= float(threshold)*10):
                    temp_correct = 1      # to track the correctly prediction
                    temp_similar = 1       # to track the similar prediction
                    correct_prediction += 1
                elif (cs*10 < float(threshold)*10 and float(pair[2]) < float(threshold)*10):
                    temp_correct = 1
                    temp_similar = 0
                    correct_prediction += 1
                else:
                    temp_correct = 0
                    temp_similar = 0

                # add the data rowwise into dataframe
                df.loc[i] = [pair[0],pair[1],cs*10,pair[2],temp_similar,temp_correct]
            
            # find the accuracy 
            A = correct_prediction/len(cosim_of_cbow[dim][threshold]) * 100
            df = df.append(['Accuracy  = ',A])   # append accuracy to dataframe

            # make the csv file for dataFrame
            df.to_csv('Ques1/cbow/Q1_{0}_cbow_{1}.csv'.format(dim,int(float(threshold)*10)),index = False)

        if dim == '200':
            # define dataframe to store the value of required format
            df = pd.DataFrame(columns = ['Word1','Word2','Similarity Score','Ground Truth', 'Label_similar', 'label_correct'])

            for i,(pair,cs) in enumerate(cosim_of_cbow[dim][threshold].items()):
                # to check for the correct prediction 
                if (cs*10 >= float(threshold)*10 and float(pair[2]) >= float(threshold)*10):
                    temp_correct = 1      # to track the correctly prediction
                    temp_similar = 1       # to track the similar prediction
                    correct_prediction += 1
                elif (cs*10 < float(threshold)*10 and float(pair[2]) < float(threshold)*10):
                    temp_correct = 1
                    temp_similar = 0
                    correct_prediction += 1
                else:
                    temp_correct = 0
                    temp_similar = 0

                # add the data rowwise into dataframe
                df.loc[i] = [pair[0],pair[1],cs*10,pair[2],temp_similar,temp_correct]
            
            # find the accuracy 
            A = correct_prediction/len(cosim_of_cbow[dim][threshold]) * 100
            df = df.append(['Accuracy  = ',A])   # append accuracy to dataframe

            # make the csv file for dataFrame
            df.to_csv('Ques1/cbow/Q1_{0}_cbow_{1}.csv'.format(dim,int(float(threshold)*10)),index = False)
 

        if dim == '300':
            # define dataframe to store the value of required format
            df = pd.DataFrame(columns = ['Word1','Word2','Similarity Score','Ground Truth', 'Label_similar', 'label_correct'])

            for i,(pair,cs) in enumerate(cosim_of_cbow[dim][threshold].items()):
                # to check for the correct prediction 
                if (cs*10 >= float(threshold)*10 and float(pair[2]) >= float(threshold)*10):
                    temp_correct = 1      # to track the correctly prediction
                    temp_similar = 1       # to track the similar prediction
                    correct_prediction += 1
                elif (cs*10 < float(threshold)*10 and float(pair[2]) < float(threshold)*10):
                    temp_correct = 1
                    temp_similar = 0
                    correct_prediction += 1
                else:
                    temp_correct = 0
                    temp_similar = 0

                # add the data rowwise into dataframe
                df.loc[i] = [pair[0],pair[1],cs*10,pair[2],temp_similar,temp_correct]
            
            # find the accuracy 
            A = correct_prediction/len(cosim_of_cbow[dim][threshold]) * 100
            df = df.append(['Accuracy  = ',A])   # append accuracy to dataframe

            # make the csv file for dataFrame
            df.to_csv('Ques1/cbow/Q1_{0}_cbow_{1}.csv'.format(dim,int(float(threshold)*10)),index = False)


