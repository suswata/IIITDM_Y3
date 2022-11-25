'''
DONE BY CS20B1057
A S V DHANUSH
1)Generate a random data set x1 , . . . , xm of size m for
(a) Exponential Distribution,
(b) Uniform Distribution (self-study),
(c) Bernoulli Distribution.
Plot the sample mean (x1 + . . . + xm )/m for m = 10, 100, 500, 1000, 5000, 10000, 50000 for 
(a), (b), (c). This way, verify the weak law of large numbers (WLLN).

'''
from scipy.stats import expon,bernoulli,uniform
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#generating random data set from exponential distribution 
#m=10
arr1 = expon.rvs(scale=10, size=10)
#print(arr1)
sum1=0
#we got the data set(x1,x2,x3,...xm) and now we will calculate its mean
for i in range(0,len(arr1)):
    sum1 = sum1 + arr1[i]
print(f"SUM IS {sum1}\n")
print(f"The value of 'm' is : {len(arr1)}\n")
mean1=sum1/len(arr1)
print(f"The Mean : {mean1}\n")
#m=100
arr2 = expon.rvs(scale=10, size=100)
#print(arr2)
sum2=0
#we got the data set(x1,x2,x3,...xm) and now we will calculate its mean
for i in range(0,len(arr2)):
    sum2 = sum2 + arr2[i]
print(f"SUM IS {sum2}\n")
print(f"The value of 'm' is : {len(arr2)}\n")
mean2=sum2/len(arr2)
print(f"The Mean : {mean2}\n")
#m=500
arr3 = expon.rvs(scale=10, size=500)
#print(arr3)
sum3=0
#we got the data set(x1,x2,x3,...xm) and now we will calculate its mean
for i in range(0,len(arr3)):
    sum3 = sum3 + arr3[i]
print(f"SUM IS {sum3}\n")
print(f"The value of 'm' is : {len(arr3)}\n")
mean3=sum3/len(arr3)
print(f"The Mean : {mean3}\n")
#m=1000
arr4 = expon.rvs(scale=10, size=1000)
#print(arr4)
sum4=0
#we got the data set(x1,x2,x3,...xm) and now we will calculate its mean
for i in range(0,len(arr4)):
    sum4= sum4 + arr4[i]
print(f"SUM IS {sum4}\n")
print(f"The value of 'm' is : {len(arr4)}\n")
mean4=sum4/len(arr4)
print(f"The Mean : {mean4}\n")
#m=5000
arr5 = expon.rvs(scale=10, size=5000)
#print(arr5)
sum5=0
#we got the data set(x1,x2,x3,...xm) and now we will calculate its mean
for i in range(0,len(arr5)):
    sum5 = sum5 + arr5[i]
print(f"SUM IS {sum5}\n")
print(f"The value of 'm' is : {len(arr5)}\n")
mean5=sum5/len(arr5)
print(f"The Mean : {mean5}\n")
#m=10000
arr6 = expon.rvs(scale=10, size=10000)
#print(arr6)
sum6=np.mean(arr6)
#we got the data set(x1,x2,x3,...xm) and now we will calculate its mean
for i in range(0,len(arr6)):
    sum6 = sum6 + arr6[i]
print(f"SUM IS {sum6}\n")
print(f"The value of 'm' is : {len(arr6)}\n")
mean6=sum6/len(arr6)
print(f"The Mean : {mean6}\n")
#m=50000
arr7 = expon.rvs(scale=10, size=50000)
#print(arr3)
sum7=0
#we got the data set(x1,x2,x3,...xm) and now we will calculate its mean
for i in range(0,len(arr7)):
    sum7 = sum7 + arr7[i]
print(f"SUM IS {sum7}\n")
print(f"The value of 'm' is : {len(arr7)}\n")
mean7=sum7/len(arr7)
print(f"The Mean : {mean7}\n")
list_mean=[mean1,mean2,mean3,mean4,mean5,mean6,mean7]
m_val=[10,100,500,1000,5000,10000,50000]
#plotting
df = pd.DataFrame({'m':m_val, 'exp_mean':list_mean})
ax = df.plot(x='m', y='exp_mean', rot=45)

#b
# UNIFORM DISTRIBUTION
#genarating random variables
#m=10
arr21 = uniform.rvs(size=10)
mean21 = np.mean(arr21)
#m=100
arr22 = uniform.rvs(size=100)
mean22 = np.mean(arr22)
#m=500
arr23 = uniform.rvs(size=500)
mean23 = np.mean(arr23)
#m=1000
arr24 = uniform.rvs(size=1000)
mean24 = np.mean(arr24)
#m=5000
arr25 = uniform.rvs(size=5000)
mean25 = np.mean(arr25)
#m=10000
arr26 = uniform.rvs(size=10000)
mean26 = np.mean(arr26)
#m=50000
arr27 = uniform.rvs(size=50000)
mean27 = np.mean(arr27)

#plotting bar graph
list_uni= [mean21,mean22,mean23,mean24,mean25,mean26,mean27]
df2 = pd.DataFrame({'m':m_val, 'uniform_mean':list_uni})
ax2 = df2.plot(x='m', y='uniform_mean', rot=45)

#c
#BERNOULLI DISTRIBUTION
p=0.4 #probablity of success
x=bernoulli(p)
#print(np.round(x.pmf(1),2))
#print(np.round(x.pmf(0), 2))
#m=10
sample1 = x.rvs(10)
mean11=np.mean(sample1)
#print(sum11)
#print(sample1)
#m=100
sample2 = x.rvs(100)
mean12=np.mean(sample2)
#m=500
sample3 = x.rvs(500)
mean13=np.mean(sample3)
#m=1000
sample4 = x.rvs(1000)
mean14=np.mean(sample4)
#m=5000
sample5 = x.rvs(5000)
mean15=np.mean(sample5)
#m=10000
sample6 = x.rvs(10000)
mean16=np.mean(sample6)
#m=50000
sample7 = x.rvs(50000)
mean17=np.mean(sample7)
#plotting bar graph
list1= [mean11,mean12,mean13,mean14,mean15,mean16,mean17]
df1 = pd.DataFrame({'m':m_val, 'bernoulli_mean':list1})
ax1 = df1.plot(x='m', y='bernoulli_mean', rot=45)
'''IN ALL THE THREE CASES THE MEANS ARE SLOWLY STABILIZING WHICH VERIFIES
THE WEAK LAW OF LARGE NUMBERS (WLLN) 
'''
