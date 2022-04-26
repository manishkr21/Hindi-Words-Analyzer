import pickle
import pandas as pd
# Import writer class from csv module
from csv import writer

cosim_of_sg = pickle.load(open('Ques1/cosim_of_sg.dat','rb'))

# for dim in cosim_of_sg:
#     for ind in cosim_of_sg[dim]:
#         true_pos = 0
#         true_neg = 0

#         for pair,cs in cosim_of_sg[dim][ind].items():
#             # to find the true positive and true negative
#             if(cs * 10>= float(ind) and float(pair[2]) >= float(ind)):
#                 true_pos += 1
#             elif(cs * 10 < float(ind) and float(pair[2]) < float(ind)):
#                 true_neg += 1
#         # finding the accuracy for each dimension and threshold
#         acc = (true_pos + true_neg)/len(cosim_of_sg[dim][ind])
#         accuracy_for_sg[ind][dim] = acc


# # save the accuracy into csv file
# accuracy_for_sg.to_csv('Ques1/accuracy.csv',mode='a', header=False)



for dim in cosim_of_sg:     # iterate through dimensions
    for threshold in cosim_of_sg[dim]:  # iterate through threshold
       
        correct_prediction = 0
    
        if dim == '50':
            # define dataframe to store the value of required format
            df = pd.DataFrame(columns = ['Word1','Word2','Similarity Score','Ground Truth', 'Label_similar', 'label_correct'])

            for i,(pair,cs) in enumerate(cosim_of_sg[dim][threshold].items()):
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
            A = correct_prediction/len(cosim_of_sg[dim][threshold]) * 100
            df = df.append(['Accuracy  = ',A])   # append accuracy to dataframe

            # make the csv file for dataFrame
            df.to_csv('Ques1/sg/Q1_{0}_sg_{1}.csv'.format(dim,int(float(threshold)*10)),index = False)

        if dim == '100':
            # define dataframe to store the value of required format
            df = pd.DataFrame(columns = ['Word1','Word2','Similarity Score','Ground Truth', 'Label_similar', 'label_correct'])

            for i,(pair,cs) in enumerate(cosim_of_sg[dim][threshold].items()):
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
            A = correct_prediction/len(cosim_of_sg[dim][threshold]) * 100
            df = df.append(['Accuracy  = ',A])   # append accuracy to dataframe

            # make the csv file for dataFrame
            df.to_csv('Ques1/sg/Q1_{0}_sg_{1}.csv'.format(dim,int(float(threshold)*10)),index = False)

        if dim == '200':
            # define dataframe to store the value of required format
            df = pd.DataFrame(columns = ['Word1','Word2','Similarity Score','Ground Truth', 'Label_similar', 'label_correct'])

            for i,(pair,cs) in enumerate(cosim_of_sg[dim][threshold].items()):
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
            A = correct_prediction/len(cosim_of_sg[dim][threshold]) * 100
            df = df.append(['Accuracy  = ',A])   # append accuracy to dataframe

            # make the csv file for dataFrame
            df.to_csv('Ques1/sg/Q1_{0}_sg_{1}.csv'.format(dim,int(float(threshold)*10)),index = False)
 

        if dim == '300':
            # define dataframe to store the value of required format
            df = pd.DataFrame(columns = ['Word1','Word2','Similarity Score','Ground Truth', 'Label_similar', 'label_correct'])

            for i,(pair,cs) in enumerate(cosim_of_sg[dim][threshold].items()):
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
            A = correct_prediction/len(cosim_of_sg[dim][threshold]) * 100
            df = df.append(['Accuracy  = ',A])   # append accuracy to dataframe

            # make the csv file for dataFrame
            df.to_csv('Ques1/sg/Q1_{0}_sg_{1}.csv'.format(dim,int(float(threshold)*10)),index = False)


