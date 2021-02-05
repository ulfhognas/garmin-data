import numpy as np

#def arrangespeed(N):

fseq = []
jumps = np.arange(0.01, 1, 0.01)
jumps = np.append(jumps, np.arange(1, 0, -0.01))
last = 1
for i in jumps:
    fseq = np.append(fseq, np.arange(last, last+1, i))
    last = fseq[-1]+i
