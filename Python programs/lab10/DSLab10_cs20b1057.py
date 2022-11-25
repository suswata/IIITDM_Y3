#DONE BY CS20B1057
#A S V DHANUSH
#USING HISTOGRAM FOR STATISTICAL PLOTTING
import pandas as pd
import matplotlib.pyplot as plt 

df_old = pd.read_csv("diabetes1.csv")
df = df_old.drop("Outcome",axis=1)
df_1 = df_old.drop("Outcome",axis=1) #removing column Outcome
print(df)
print("\n-----MEAN-----\n")
df1=df.mean() #mean of all columns
print(df1)
print("\n-----MODE-----\n")
df2=df.mode() #mean of all columns
print(df2)
print("\n-----MAX-----\n")
df3 = df.max()
print(df3)
print("\n-----MIN-----\n")
df4 = df.min()
print(df4)
print("\n-----STANDAR DEVIATION-----\n")
df5 = df.std()
print(df5)
print("\n-----CORRELATION COEFFICIENT OF AGE CALCULATION-----\n")
col1 ,col2 = "Age" , "BMI"
corr1 = df[col1].corr(df["Pregnancies"])
print("Correlation between ", col1, " and Pregnancies attribute is: ", round(corr1, 2))
corr2 = df[col1].corr(df["Glucose"])
print("Correlation between ", col1, " and Glucose attribute is: ", round(corr2, 2))
corr3 = df[col1].corr(df["BloodPressure"])
print("Correlation between ", col1, " and BloodPressure attribute is: ", round(corr3, 2))
corr4 = df[col1].corr(df["SkinThickness"])
print("Correlation between ", col1, " and SkinThickness attribute is: ", round(corr4, 2))
corr5 = df[col1].corr(df["Insulin"])
print("Correlation between ", col1, " and Insulin attribute is: ", round(corr5, 2))
corr6 = df[col1].corr(df["BMI"])
print("Correlation between ", col1, " and BMI attributeis: ", round(corr6, 2))
corr7 = df[col1].corr(df["DiabetesPedigreeFunction"])
print("Correlation between ", col1, " and DiabetesPedigreeFunction attribute is: ", round(corr7, 2))
corr8 = df[col1].corr(df["Age"])
print("Correlation between ", col1, " and BMI attribute is: ", round(corr8, 2))

print("\n-----CORRELATION COEFFICIENT OF BMI CALCULATION-----\n")
cor1 = df[col2].corr(df["Pregnancies"])
print("Correlation between ", col2, " and Pregnancies attribute is: ", round(cor1, 2))
cor2 = df[col2].corr(df["Glucose"])
print("Correlation between ", col2, " and Glucose attribute is: ", round(cor2, 2))
cor3 = df[col2].corr(df["BloodPressure"])
print("Correlation between ", col2, " and BloodPressure attribute is: ", round(cor3, 2))
cor4 = df[col2].corr(df["SkinThickness"])
print("Correlation between ", col2, " and SkinThickness attribute is: ", round(cor4, 2))
cor5 = df[col2].corr(df["Insulin"])
print("Correlation between ", col2, " and Insulin attribute is: ", round(cor5, 2))
cor6 = df[col2].corr(df["Age"])
print("Correlation between ", col2, " and Age attributeis: ", round(cor6, 2))
cor7 = df[col2].corr(df["DiabetesPedigreeFunction"])
print("Correlation between ", col2, " and DiabetesPedigreeFunction attribute is: ", round(cor7, 2))
cor8 = df[col2].corr(df["BMI"])
print("Correlation between ", col2, " and BMI attribute is: ", round(cor8, 2))
#SCATTER PLOTS
plt.scatter(df["Age"],df["Pregnancies"])
plt.show()
plt.scatter(df["Age"],df["Glucose"])
plt.show()
plt.scatter(df["Age"],df["BloodPressure"])
plt.show()
plt.scatter(df["Age"],df["SkinThickness"])
plt.show()
plt.scatter(df["Age"],df["Insulin"])
plt.show()
plt.scatter(df["Age"],df["DiabetesPedigreeFunction"])
plt.show()
plt.scatter(df["Age"],df["BMI"])
plt.show()
#SCATTER PLOTS
plt.scatter(df["BMI"],df["Pregnancies"])
plt.show()
plt.scatter(df["BMI"],df["Glucose"])
plt.show()
plt.scatter(df["BMI"],df["BloodPressure"])
plt.show()
plt.scatter(df["BMI"],df["SkinThickness"])
plt.show()
plt.scatter(df["BMI"],df["Insulin"])
plt.show()
plt.scatter(df["BMI"],df["DiabetesPedigreeFunction"])
plt.show()
plt.scatter(df["BMI"],df["Age"])
plt.show()


#HISTOGRAM PLOTS
df.plot( x="Pregnancies", y="SkinThickness", kind='hist')


df_old.groupby('Outcome').plot(x = "Pregnancies", y="Outcome",kind='hist')

#box-plot

df_1.plot.box(grid='False')