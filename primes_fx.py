# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 23:54:49 2019

@author: cp
"""

# Functions used
from progressbar import ProgressBar

# primes: mono-1, cyclop-2, neither-0
def monoAndCyclopPrimes(prime):    
    x = str(prime)
    if len(x) == 1:
        return 1
    else:
        cycl = 0
        for i in range(0,len(x)):
            if x[0] != x[i]:                
                if (i+1) < len(x):
                    cycl += 1                    
                    if cycl > 1:
                        return 0
                else:
                    return 0                
            #else:
            #    continue
        if cycl == 1:
            return 2
        else:
            return 1


# get all primes
def getPrimes(lower, upper):
    prim = []    
    # uneven lower value, for stepping of 2
    if lower % 2 == 0:
        lower += 1
    # going loop    
    pbar = ProgressBar()        
    for num in pbar(range(lower,upper + 1,2)):        
       # prime numbers are greater than 1
       if num > 1:
           for i in range(2,num):
               if (num % i) == 0:
                   break
           else:
               # group by types
               if monoAndCyclopPrimes(num) == 1:
                   prim.append([num, "M"])     
               elif monoAndCyclopPrimes(num) == 2:
                   prim.append([num, "C"])     
               else:
                   prim.append([num, "P"])                       
       if num % 1000 == 0:
          print("iteration: ",num)               
    return prim
                   
# plot primes value per i-th appearance 
import matplotlib.pyplot as plt
import numpy as np    

def plotPrimes(c, title=None, vals=False):    
    cp = np.array(c)          
    if len(cp.shape) > 1:
        cp = cp[:,0].astype(int)
    
    plt.plot(range(0, len(cp)), cp, 'ro')
    if title != None:
        title = title
    else:
        title = "First " + str(len(cp)) + " cyclop primes"
    plt.title(title)        
    if vals:
        r = range(0, len(cp))
        for a,b in zip(r,cp):
            plt.text(a, b, str(b), rotation = 45)
    plt.grid(True)
    plt.yticks(range(0,max(cp),max(cp)/10))

