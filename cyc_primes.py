# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 08:18:26 2019

@author: cp

Note: Algorithms are not optimized so can run long. Just ad-hoc script.

1. Return primes which consists only of one particular digit "[d]+" 
2. Return cyclop primes - contains of only one particular digit plus only one other digit (inside)

"""
    
## test primes
import numpy as np    
import primes_fx as pfx

# slow method
top150k = pfx.getPrimes(0,150000)
p = np.array(top150k)

# print top 100
print(p[0:100])

# print all mono-primes
m = p[np.where(p[:,1]=="M")]

# print all cyclop primes
c = p[np.where(p[:,1]=="C")]


## plot cyclop primes up to value of 150k:
pfx.plotPrimes(m)
pfx.plotPrimes(c)


## plot primes using imported functions - far more efficient loops
import Primes

# get first million
primes = Primes.primeList(10**6)
len(primes)

# visualize cyclop primes density
cp = [cp for cp in primes if pfx.monoAndCyclopPrimes(cp)]

# plot density and curve per appearance
Primes.PlotPrimeDensityTheory(cp, ylim = 10)
pfx.plotPrimes(cp)

# get subset between:
cs = list(filter(lambda x: (x > 300000 and x < 400000), cp))
print(cs)

# zoom plot to that region
pfx.plotPrimes(cs, title="4th ten of a million", vals=True)


######################################################################
## imported from wiki: mono primes of digit "1" found with indexes: ##
mi = [2, 19, 23, 317, 1031, 49081, 86453, 109297, 270343]

for i in range(len(mi)):
    print(round((10**mi[i]-1)/9))

# error: "OverflowError: integer division result too large for a float"