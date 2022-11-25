#DONE BY CS20B1057
#A S V DHANUSH
#KNN CLASSIFIER
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier as knn
from sklearn.metrics import accuracy_score as accs
from sklearn.metrics import confusion_matrix as cm

#TAKING THE CSV DATA INTO A DATAFRAME
df = pd.read_csv("SteelPlateFaults-2class.csv")
#print(df)
print(df.shape)

X_train, X_test, X_label_train, X_label_test = train_test_split(df,df['Class'],test_size=0.3, random_state=42)
#DROPPING 'Class' COLUMN IN TRAINING AND TESTING DATA SET
X_train = X_train.drop('Class',axis=1)
X_test = X_test.drop('Class',axis=1)

#FINDING NORMALISED DATA
for i in X_train.columns:
    X_train[i] = (X_train[i] - X_train[i].min()) / (X_train[i].max()-X_train[i].min())
    X_test[i] = (X_test[i] - X_test[i].min()) / (X_test[i].max()-X_test[i].min())

print("The Normalized Data Sets Are")

print("The Train Data Set Is")
print(X_train)

print("The Test Data Set Is")
print(X_test)

#K-Nearest Neigbours for K = 1
n1 = knn(n_neighbors=1)
n1.fit(X_train, X_label_train)
pred1 = n1.predict(X_test)
print("The Predicted Values Are")
print(pred1)

print("Confusion Matrix")
confusion1 =  cm(X_label_test, pred1)
print(confusion1)
print("Accuracy Score")
accur1 = accs(X_label_test,pred1)
print(accur1)

#K-Nearest Neigbours for K = 3
n3 = knn(n_neighbors=3)
n3.fit(X_train, X_label_train)
pred2 = n3.predict(X_test)
print("The Predicted Values Are")
print(pred2)
print("The Confusion Matrix Is")
confusion2 =  cm(X_label_test, pred2)
print(confusion2)
print("Accuracy Score")
accur2 = accs(X_label_test, pred2)
print(accur2)

#K-Nearest Neigbours for K = 5
n5 = knn(n_neighbors=5)
n5.fit(X_train, X_label_train)
pred3 = n5.predict(X_test)
print("The Predicted Values Are")
print(pred3)
print("The Confusion Matrix Is")
confusion3 =  cm(X_label_test, pred3)
print(confusion3)
print("Accuracy Score")
accur3 = accs(X_label_test, pred3)
print(accur3)

#K-Nearest Neigbours for K = 10
n10 = knn(n_neighbors=10)
n10.fit(X_train, X_label_train)
pred3 = n10.predict(X_test)
print("The Predicted Values Are")
print(pred3)
print("The Confusion Matrix Is")
confusion4 =  cm(X_label_test, pred3)
print(confusion4)
print("Accuracy Score")
accur4 = accs(X_label_test, pred3)
print(accur4)



    
    