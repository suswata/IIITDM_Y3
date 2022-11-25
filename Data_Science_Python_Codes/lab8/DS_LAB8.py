#Done By CS20B1057
#A S V Dhanush
#Diabetes
import pandas as pd
df = pd.read_csv("diabetes.csv")#read csv file
#print(df)
count = int(0)
df = df.drop(['Type'],axis=1) #removed NaN
#print(df['Outcome'].count())
total = df['Outcome'].count() #calculated total outcomes
while(1):
    print("1. Find the probability of diabetes given the dataset. Also, calculate the probability of diabetes given\n"
    "2.Find the probability of diabetes with a glucose level of more than 120 + blood pressure of more than 90 + skin thickness of more than 30 + insulin above 150 + BMI above 25.\n"
    "3.Exit")
    choice = int(input("Enter Choice : "))
    if(choice == 1):
        while(1):
            print("a.Age above 50\n"
            "b.Age between 40 and 50\n"
            "c.Age between 30 and 40\n"
            "d.Age less than 30\n"
            "e.Exit")
            opt = input("Enter choice : ")
            if(opt == 'a'):
                out_one = 0
                prob=0
                print(f"Total Outcomes : {total}")
                for i in df.index:
                    if(df['Outcome'][i] == 1 and  df['Age'][i]>50):#calculating desired outcomes
                        out_one=out_one+1#counting outcomes
                print(f" Outcomes as 1 and Age>50 : {out_one}")
                prob = out_one / total
                print(f"Probability of diabetes of age above 50 is : {prob}")#printing values

            elif(opt == 'b'):
                out_one_1 = 0
                print(f"Total Outcomes : {total}")
                for i in df.index:
                    if(df['Outcome'][i] == 1 and (df['Age'][i]>40 and df['Age'][i]<50)):
                        out_one_1=out_one_1+1
                print(f" Outcomes as 1 and Age >40 and < 50 : {out_one_1}")
                prob_1 = out_one_1 / total
                print(f"Probability of diabetes of age between 40 and 50 is : {prob_1}")#printing values
            elif(opt == 'c'):
                out_one_1 = 0
                print(f"Total Outcomes : {total}")
                for i in df.index:
                    if(df['Outcome'][i] == 1 and (df['Age'][i]>30 and df['Age'][i]<40)):
                        out_one_1=out_one_1+1
                print(f" Outcomes as 1 and Age >30 and < 40 : {out_one_1}")
                prob_1 = out_one_1 / total
                print(f"Probability of diabetes of age between 40 and 50 is : {prob_1}")#printing values
            elif(opt == 'd'):
                out_one_1 = 0
                print(f"Total Outcomes : {total}")
                for i in df.index:
                    if(df['Outcome'][i] == 1 and df['Age'][i]<30):
                        out_one_1=out_one_1+1
                print(f" Outcomes as 1 and Age <30 : {out_one_1}")
                prob_1 = out_one_1 / total
                print(f"Probability of diabetes of age between 40 and 50 is : {prob_1}")#printing values

            else:
                break
    elif(choice == 2):
        out_one_1 = 0
        print(f"Total Outcomes : {total}")
        for i in df.index:
            if(df['Outcome'][i] == 1 and df['BMI'][i]>25 and df['Insulin'][i]>150 and df['Glucose'][i]>120 and df['BloodPressure'][i]>90 and df['SkinThickness'][i]>30):
                out_one_1=out_one_1+1
        print(f" Outcomes as 1 and Glucose>120 and Bloodpressure>90 and skin thickness > 30 and insulin >150 and BMI>25: {out_one_1}")
        prob_1 = out_one_1 / total
        #printing values
        print(f"Probability of diabetes with a glucose level of more than 120 + blood pressure of more than 90 + skin thickness of more than 30 + insulin above 150 + BMI above 25 is : {prob_1}")
    elif(choice == 3):
        print("Exitting !")
        break
    else:
        break




            
