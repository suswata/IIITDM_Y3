'''
DONE BY CS20B1057
A S V DHANUSH
Generate a random data set of size 1000 for each independent and identically distributed
(a) n Exponential Distribution,
(b) n Uniform Distribution (self-study),
(c) n Bernoulli Distribution.
Numerically compute and plot the distribution of the sample mean (X1 +. . .+Xn )/n and
 corresponding “normal” approximation for n = 1, 2, 4, 8, 16, 32 for (a), (b), (c). 
 This way, verify the Central Limit Theorem (CLT).

'''
from scipy.stats import expon,bernoulli,uniform
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#Exponential Distribution
#PLOTTING THE GRAPHS
#starting from n=2 as the graphs are not coming properly for n=1
#n=2
arrays1 = {i:expon.rvs(scale=1,size=1000) for i in range(2)}
arrays_mean1 = {str(i):np.mean(arrays1[i]) for i in arrays1}
sns.histplot(arrays_mean1.values(),kde=True) //histplot attribute

#n=4
arrays2 = {i:expon.rvs(scale=1,size=1000) for i in range(4)}
arrays_mean2 = {str(i):np.mean(arrays2[i]) for i in arrays2}
sns.histplot(arrays_mean2.values(),kde=True)

#n=8
arrays3 = {i:expon.rvs(scale=1,size=1000) for i in range(8)}
arrays_mean3 = {str(i):np.mean(arrays3[i]) for i in arrays3}
sns.histplot(arrays_mean3.values(),kde=True)

#n=16
arrays4= {i:expon.rvs(scale=1,size=1000) for i in range(16)}
arrays_mean4 = {str(i):np.mean(arrays4[i]) for i in arrays4}
sns.histplot(arrays_mean4.values(),kde=True)

#n=32
arrays5 = {i:expon.rvs(scale=1,size=1000) for i in range(32)}
arrays_mean5 = {str(i):np.mean(arrays5[i]) for i in arrays5}
sns.histplot(arrays_mean5.values(),kde=True)

#for n=1000 or above we see clearly the the plot changes from exponential to normal distribution
arrays6 = {i:expon.rvs(scale=1,size=1000) for i in range(1200)}
arrays_mean6 = {str(i):np.mean(arrays6[i]) for i in arrays6}
sns.histplot(arrays_mean6.values(),kde=True)

#Uniform Distribution
#PLOTTING THE GRAPHS
#n=2
arrays11 = {i:uniform.rvs(size=1000) for i in range(2)}
arrays_mean11 = {str(i):np.mean(arrays11[i]) for i in arrays11}
sns.histplot(arrays_mean11.values(),kde=True)

#n=4
arrays12 = {i:uniform.rvs(size=1000) for i in range(4)}
arrays_mean12 = {str(i):np.mean(arrays12[i]) for i in arrays12}
sns.histplot(arrays_mean12.values(),kde=True)

#n=8
arrays13 = {i:uniform.rvs(size=1000) for i in range(8)}
arrays_mean13 = {str(i):np.mean(arrays13[i]) for i in arrays13}
sns.histplot(arrays_mean13.values(),kde=True)

#n=16
arrays14= {i:uniform.rvs(size=1000) for i in range(16)}
arrays_mean14 = {str(i):np.mean(arrays14[i]) for i in arrays14}
sns.histplot(arrays_mean14.values(),kde=True)

#n=32
arrays15 = {i:uniform.rvs(size=1000) for i in range(32)}
arrays_mean15 = {str(i):np.mean(arrays15[i]) for i in arrays15}
sns.histplot(arrays_mean15.values(),kde=True)

#n=1200
arrays16 = {i:uniform.rvs(size=1000) for i in range(1200)}
arrays_mean16 = {str(i):np.mean(arrays16[i]) for i in arrays16}
sns.histplot(arrays_mean16.values(),kde=True)

#BERNOULLI DISTRIBUTION
#PLOTTING THE GRAPHS
p=0.4 #probablity of success
x=bernoulli(p)
#n=2
arrays21 = {i:x.rvs(size=1000) for i in range(2)}
arrays_mean21 = {str(i):np.mean(arrays21[i]) for i in arrays21}
sns.histplot(arrays_mean21.values(),kde=True)

#n=4
arrays22 = {i:x.rvs(size=1000) for i in range(4)}
arrays_mean22 = {str(i):np.mean(arrays22[i]) for i in arrays22}
sns.histplot(arrays_mean22.values(),kde=True)

#n=8
arrays23 = {i:x.rvs(size=1000) for i in range(8)}
arrays_mean23 = {str(i):np.mean(arrays23[i]) for i in arrays23}
sns.histplot(arrays_mean23.values(),kde=True)

#n=16
arrays24= {i:x.rvs(size=1000) for i in range(16)}
arrays_mean24 = {str(i):np.mean(arrays24[i]) for i in arrays24}
sns.histplot(arrays_mean14.values(),kde=True)

#n=32
arrays25 = {i:x.rvs(size=1000) for i in range(32)}
arrays_mean25 = {str(i):np.mean(arrays25[i]) for i in arrays25}
sns.histplot(arrays_mean25.values(),kde=True)

#n=1200
arrays26 = {i:x.rvs(size=1000) for i in range(1200)}
arrays_mean26 = {str(i):np.mean(arrays26[i]) for i in arrays26}
sns.histplot(arrays_mean26.values(),kde=True)

#IF WE OBSERVE IN ALL  THE CASES THE GRAPH SLOWLY CONVERTS TO NORMAL DISTRIBUTION
#HENCE CENTRAL LIMIT THEOREM (CLT) IS SATISFIED/VERIFIED