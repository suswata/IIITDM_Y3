# DONE BY CS20B1057
# A S V DHANUSH
# DS LAB11
# OUTLIER DETECTION, BOX PLOT , REPLACING VALUES IN ATTRIBUTES
import pandas as pd
import matplotlib.pyplot as plt
import math
import sklearn.metrics
import numpy as np
# CONVERTING MISSED VALS CSV TO DF
# 2
# a
df1 = pd.read_csv("landslide_data3_miss.csv")
df2 = pd.read_csv("landslide_data3_original.csv")
# print(df1)
print(df1.shape)
# Replaced NaN values with mean values
df1_rep = df1.fillna(df1.mean())
print(df1_rep)
print(f"Mean\n")
print(f"Replaced df : \n{df1_rep.mean()}\nOriginal df : \n{df2.mean()}\n")
print(f"Median\n")
print(f"Replaced df : \n{df1_rep.median()}\nOriginal df : \n{df2.median()}\n")
print(f"Mode\n")
print(f"Replaced df : \n{df1_rep.mode()}\nOriginal df : \n{df2.mode()}\n")
print(f"Standard Deviation\n")
print(f"Replaced df : \n{df1_rep.std()}\nOriginal df : \n{df2.std()}\n")

o_val = {}
r_val = {}
rms_d = {}
for i in df2.columns:
    o_val[i] = df2.loc[df1[i].isna()][i]
    r_val[i] = df1_rep.loc[df1[i].isna()][i]

for i in o_val:
    if i == "dates" or i == "stationid":
        continue
    o_arr = np.array(o_val[i])
    r_arr = np.array(r_val[i])
    # RMSE BY BUILTIN
    mse = sklearn.metrics.mean_squared_error(o_arr, r_arr)
    rmse = math.sqrt(mse)
    print(f"THE RMSE VALUES ARE : {rmse}\n")
    # RMSE BY FORMULA
    rms_d[i] = (np.sum((o_arr-r_arr)**2)/len(o_arr))**0.5
print(f"RMSE VALUES BY FORMULA : {rms_d}\n")
# plotting bar graph
plt.bar(rms_d.keys(), rms_d.values())
plt.xticks(rotation=30)
plt.show()

# b
inter_df = df1.interpolate()
print("INTERPOLATED FATA FRAME : \n")
print(inter_df)
print(f"Mean\n")
print(f"Replaced df : \n{inter_df.mean()}\nOriginal df : \n{df2.mean()}\n")
print(f"Median\n")
print(f"Replaced df : \n{inter_df.median()}\nOriginal df : \n{df2.median()}\n")
print(f"Mode\n")
print(f"Replaced df : \n{inter_df.mode()}\nOriginal df : \n{df2.mode()}\n")
print(f"Standard Deviation\n")
print(f"Replaced df : \n{inter_df.std()}\nOriginal df : \n{df2.std()}\n")

# CALCULATING RMSE AND PLOTTING THE BAR GRAPH
o_val1 = {}
in_val1 = {}
rms_d1 = {}
for i in df2.columns:
    o_val1[i] = df2.loc[df1[i].isna()][i]
    in_val1[i] = inter_df.loc[df1[i].isna()][i]

for i in o_val1:
    if i == "dates" or i == "stationid":
        continue
    o_arr1 = np.array(o_val1[i])
    in_arr1 = np.array(in_val1[i])
    # RMSE BY BUILTIN
    mse1 = sklearn.metrics.mean_squared_error(o_arr1, in_arr1)
    rmse1 = math.sqrt(mse1)
    print(f"THE RMSE VALUES ARE : {rmse1}\n")
    # RMSE BY FORMULA
    rms_d1[i] = (np.sum((o_arr1-in_arr1)**2)/len(o_arr1))**0.5
print(f"RMSE VALUES BY FORMULA : {rms_d1}\n")
# plotting bar graph
plt.bar(rms_d1.keys(), rms_d1.values())
plt.xticks(rotation=30)
plt.show()

# c
# i)
out_df = inter_df.quantile([0.25, 0.75])
print(out_df)
# Outliers of temperature
print("OUTLIERS OF TEMPERATURE : \n")
print(inter_df.loc[np.logical_not(np.logical_and(inter_df['temperature'] > (out_df['temperature'].iat[0])-(1.5*(out_df['temperature'].iat[1]-out_df['temperature'].iat[0])),
      inter_df['temperature'] < (out_df['temperature'].iat[1])+(1.5*(out_df['temperature'].iat[1]-out_df['temperature'].iat[0]))))]['temperature'])
# plotting the boxplot of temperature attribute
inter_df.boxplot(column=['temperature'])
# Outliers of rain
print(inter_df.loc[np.logical_not(np.logical_and(inter_df['rain'] > (out_df['rain'].iat[0])-(1.5*(out_df['rain'].iat[1] -
      out_df['rain'].iat[0])), inter_df['rain'] < (out_df['rain'].iat[1])+(1.5*(out_df['rain'].iat[1]-out_df['rain'].iat[0]))))]['rain'])
# Plotting the boxplot of rain attribute
inter_df.boxplot(column=['rain'])

# ii)
# calculating the medians of temperatures and rain attributes
out_median_t = np.median(inter_df['temperature'])
out_median_r = np.median(inter_df['rain'])
# Replacing outliers with median values
for i in range(0, len(inter_df)):
    if not (inter_df.loc[np.logical_not(np.logical_and(inter_df['temperature'] > (out_df['temperature'].iat[0])-(1.5*(out_df['temperature'].iat[1]-out_df['temperature'].iat[0])), inter_df['temperature'] < (out_df['temperature'].iat[1])+(1.5*(out_df['temperature'].iat[1]-out_df['temperature'].iat[0]))))]['temperature']):
        inter_df['temperature'][i] = out_median_t
    if not (inter_df.loc[np.logical_not(np.logical_and(inter_df['rain'] > (out_df['rain'].iat[0])-(1.5*(out_df['rain'].iat[1]-out_df['rain'].iat[0])), inter_df['rain'] < (out_df['rain'].iat[1])+(1.5*(out_df['rain'].iat[1]-out_df['rain'].iat[0]))))]['rain']):
        inter_df['rain'][i] = out_median_r
# plotting the boxplot after replacing for the attributes
inter_df.boxplot(column='temperature')
inter_df.boxplot(column='rain')
# Yes we still get the outliers
# as even though we change the initial outliers after changing we get another set of new otuliers are formed due to this change
