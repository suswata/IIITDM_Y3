#Breast Cancer Wisconsin (Diagnostic) Data Set
#Predict whether the cancer is benign or malignant
#M = Malignant , B=Benign

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.stats import zscore
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier as knn
from sklearn.metrics import accuracy_score as accs
from sklearn.metrics import confusion_matrix as cm
import seaborn as sns


# driver code

df = pd.read_csv("cancer_data.csv")
#print(df) 
print(df.shape)
print("-------------------------------------------------------------------------------------------------------")
#checking for datatypes
print(df.dtypes)
print("-------------------------------------------------------------------------------------------------------")
#copying the data frames data into another dataframe
df_copy = df.copy(deep = True)
print("------------------------------------------DESCRIBE-----------------------------------------------------")
print(df_copy.describe().transpose())
print("-------------------------------------------------------------------------------------------------------")
#print(df_copy)

#removing the duplicate values in this dataframe
retStatus = df_copy.drop_duplicates(inplace=True)
print("IF DUPLICATES ARE NOT PRESENT THEN IT WILL PRINT 'None' AS THE OUTPUT FOR THE ABOVE CODE!")
print(retStatus)

#since there are no duplicates in this dataframe we will go ahead and remove NaN values in this dataframe
#df_without_nan = df_copy.dropna()
#print(df_without_nan)
#since there are no NaN entries in our dataframe we can move forward to plotting the graphs adn synthesizing the data and remvoing the outliers

#dividing the dataset based on the diagnosis (based of M OR B)


print("--------------------------------------------MALIGNANT--------------------------------------------------")
df_malignant = df_copy[df["diagnosis"] == 'M']
print(f"The size of Malignant dataset : {df_malignant.shape}")
print(df_malignant)
print(df_malignant.describe().transpose())
print("-------------------------------------------------------------------------------------------------------")
print("--------------------------------------------BENIGN-----------------------------------------------------")
df_benign = df_copy[df["diagnosis"] == 'B']
print(f"The size is of Benign dataset : {df_benign.shape}")
print(df_benign)
df_copy['diagnosis'] = df_copy.diagnosis.astype('category')
#print(df_benign.describe().transpose())
print("-------------------------------------------------------------------------------------------------------")
print("---------------------------- DATA FRAME GROUPED BY DIAGNOSIS COUNT ------------------------------------")
print(df_copy.groupby(["diagnosis"]).count())
print("-------------------------------------------------------------------------------------------------------")
#finding the ratio of  benign and benign
ratio = df_benign["diagnosis"].count()/df_malignant["diagnosis"].count()

print(f"RATIO OF BENIGN / MALIGNANT : {math.ceil(ratio)}")
#SINCE THE RATIO IS CLOSE TO 2:1 WE CAN PREDICT FOR NOW THAT MOJORILY BENIGN DIAGNOSIS IS MORE!

#Since we dont need the patient id for the prediction of brest cancer
#we drop the id column

df_copy = df_copy.drop(labels = "id" ,axis=1)
print(df_copy)
#id column has been dropped

'''A Z-score is a numerical measurement that describes a value's relationship to 
the mean of a group of values. 
Z-score is measured in terms of standard deviations from the mean. 
If a Z-score is 0, it indicates that the data point's score is identical to 
the mean score.'''


df_without_diagnosis = df_copy.drop(["diagnosis"],axis=1)
#dataframe without diagnosis column
#print(df_without_diagnosis)
print("-------------------------------------------------------------------------------------------------------")
cols = list(df_without_diagnosis.columns)
for i in cols:
    col_zscore = i + '_scaled'
    df_without_diagnosis[col_zscore] = (df_without_diagnosis[i]-df_without_diagnosis[i].mean())/df_without_diagnosis[i].std(ddof=0)
print(f"---------------------------------------NORMALIZED VALUES OF THE DATA SET------------------------------\n{df_without_diagnosis}")

print("-------------------------------------------------------------------------------------------------------")
print("____________________________________K-NEAREST NEIGHBOURS CLASSIFIER____________________________________")
X_train, X_test, X_label_train, X_label_test = train_test_split(df_without_diagnosis,df_copy["diagnosis"],test_size=0.3, random_state=42)
#dropping the 'Class' column is the training and testing array

acc_list=[]
acc_index=[]
for i in range(1,100,2):
    #K-Nearest Neigbours for K = 11
    n1 = knn(n_neighbors=i)
    n1.fit(X_train, X_label_train)

    pred1 = n1.predict(X_test)
    #print("The Predicted Values Are")
    #print(pred1)

    #print("Confusion Matrix")
    confusion1 =  cm(X_label_test, pred1)
    #print(confusion1)
    #print("Accuracy Score")
    accur1 = accs(X_label_test,pred1)
    acc_list.append(accur1)
    acc_index.append(i)
    #print(accur1)
print(acc_list)
#sns.kdeplot(acc_list)
plt.scatter(acc_index,acc_list)
plt.bar(df_malignant["radius_mean"],df_benign["radius_mean"])









        