# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 08:50:53 2016

@author: peter
"""

# import packages
import collections
import numpy as np 
import scipy.stats as stats
import matplotlib.pyplot as plt

# set list
testlist = [1,4,5,6,9,9]
c = collections.Counter(testlist)
print(c)

# calculate number of instances in the list
count_sum = sum(c.values())
print(count_sum)

# loop through the list pull out key and value
for k, v in c.iteritems():
    print("The frequency of number " + str(k) + " is " + str(float(v) / count_sum))
    
# create box plot
x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
plt.boxplot(x)
plt.savefig("boxplot.png")
plt.show()

# create histogram
plt.hist(x, histtype='bar')
plt.savefig("hist.png")
plt.show

# create QQ-pllots
plt.figure()
test_data = np.random.normal(size=1000)
graph1 = stats.probplot(test_data, dist='norm', plot=plt)
plt.savefig("qqplot.png")
plt.show()

plt.figure()
test_data2 = np.random.uniform(size=1000)
graph2 = stats.probplot(test_data2, dist="norm", plot=plt)
plt.savefig("qqplot2.png")
plt.show()