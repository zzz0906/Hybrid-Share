import matplotlib.pyplot as plt
import numpy as np

from numpy import power
from scipy.special import comb
from scipy.stats import poisson
import random

N = 80
C = 32
G = 4
M = 250

T_Number = 100
phi = 0.25
T = []
'''
0: number of nodes
1: cpu per nodes
2：gpu per nodes
3: mem per nodes
4: time
'''
Ns = []
Cs = []
Gs = []
Ms = []
Ts = []
for i in range(0,T_Number):
    tmp = []
    if random.random() < phi:
        tmp.append(poisson.rvs(mu=10/2, size=1)[0])
        Ns.append(tmp[0])
        tmp.append(poisson.rvs(mu=10/2, size=1)[0])
        Cs.append(tmp[1])
        tmp.append(poisson.rvs(mu=G/2, size=1)[0])
        Gs.append(tmp[2])
    else:
        tmp.append(poisson.rvs(mu=N/2, size=1)[0])
        Ns.append(tmp[0])
        tmp.append(poisson.rvs(mu=C/2, size=1)[0])
        Cs.append(tmp[1])
        tmp.append(0)
        Gs.append(0)
    tmp.append(poisson.rvs(mu=M/4, size=1)[0])
    Ms.append(tmp[3])
    tmp.append(poisson.rvs(mu=30, size=1)[0])
    Ts.append(tmp[4])
    T.append(tmp)

plt.hist(Ns, 15, density=True)
plt.xlabel('the number of nodes')
plt.ylabel('density')
plt.savefig('ns.png')

plt.cla()
plt.hist(Cs, 15, density=True)
plt.xlabel('the number of CPUs')
plt.ylabel('density')
plt.savefig('cs.png')

plt.cla()
plt.hist(Gs, 15, density=True)
plt.xlabel('the number of GPUs')
plt.ylabel('density')
plt.savefig('gs.png')

plt.cla()
plt.hist(Ms, 15, density=True)
plt.xlabel('the number of Memory')
plt.ylabel('density')
plt.savefig('ms.png')

plt.cla()
plt.hist(Ts, 15, density=True)
plt.xlabel('the time')
plt.ylabel('density')
plt.savefig('ts.png')