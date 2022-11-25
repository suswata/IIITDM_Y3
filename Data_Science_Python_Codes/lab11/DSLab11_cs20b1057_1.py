#DONE BY CS20B1057
#A S V DHANUSH
#DS LAB11
#OUTLIER DETECTION, BOX PLOT , REPLACING VALUES IN ATTRIBUTES
import pandas as pd
import matplotlib.pyplot as plt
#CONVERTING MISSED VALS CSV TO DF
df1 = pd.read_csv("landslide_data3_miss.csv")
#print(df1)
print(df1.shape)
#empty dict for stroring missing values

#CONVERTING  ORIGINAL CSV TO DF
#df2 = pd.read_csv("landslide_data3_original.csv")
#print(df2.shape)
#COUNTS THE NUMBER OF NaN values
sum9 = df1['dates'].isna().sum()
sum1 = df1['stationid'].isna().sum()
sum2 = df1['temperature'].isna().sum()
sum3 = df1['humidity'].isna().sum()
sum4 = df1['pressure'].isna().sum()
sum5 = df1['rain'].isna().sum()
sum6 = df1['lightavgw/o0'].isna().sum()
sum7 = df1['lightmax'].isna().sum()
sum8 = df1['moisture'].isna().sum()
print(f"sum1 - {sum1}\nsum2-{sum2}\nsum3 - {sum3}\nsum4-{sum4}\nsum5 - {sum5}\nsum6-{sum6}\nsum7 - {sum7}\nsum8-{sum8}\nsum9-{sum9}\n")

#PLOTTING THE BAR GRAPH 
#a
df = pd.DataFrame({'FACTORS':['dates', 'stationid', 'temperature','humidity','pressure','rain','lightavgw/o0','lightmax','moisture'], 'DATA':[sum9, sum1, sum2,sum3,sum4,sum5,sum6,sum7,sum8]})
ax = df.plot.bar(x='FACTORS', y='DATA', rot=30)
#sum1 has all the missing values of stationoid

#b
#removed all the rows with NaN in stationid
df1=df1.dropna(axis=0,subset=['stationid'])
print(df1)
print(f"No of vals deleted values : {sum1}\n")
len1 = len(df1)
print(f"LEN1 - {len1}\n")
df1=df1.dropna(axis=0,thresh=7)
print(f"LEN2-{len(df1)}\n")
print(f"The Number Of rows deleted having equal to or more than one third of attributes with missing values : {len1-len(df1)}")

#c
sum_9 = df1['dates'].isna().sum()
sum_1 = df1['stationid'].isna().sum()
sum_2 = df1['temperature'].isna().sum()
sum_3 = df1['humidity'].isna().sum()
sum_4 = df1['pressure'].isna().sum()
sum_5 = df1['rain'].isna().sum()
sum_6 = df1['lightavgw/o0'].isna().sum()
sum_7 = df1['lightmax'].isna().sum()
sum_8 = df1['moisture'].isna().sum()

print(f"sum1 - {sum_1}\nsum2-{sum_2}\nsum3 - {sum_3}\nsum4-{sum_4}\nsum5 - {sum_5}\nsum6-{sum_6}\nsum7 - {sum_7}\nsum8-{sum_8}\nsum9-{sum_9}\n")
#or
df1_miss = df1.isna().sum()
print(df1_miss)
#sum
sum_tot = sum_1+sum_2+sum_3+sum_4+sum_5+sum_6+sum_7+sum_8+sum_9
print(f"TOTAL NUMBER OF MISSING VALUES : {sum_tot}\n")

