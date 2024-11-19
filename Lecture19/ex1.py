#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

#Get AT content in sliding 1000 base window (50k, 100k, whole genome)
#the method in the lecture gives the values for a window of bases ahead and including successive single bases
ecoli = open("ecoli.txt").read().replace('\n', '').upper()

window=1000

at50 = []
at100 = []
at = []

#50k
for start in range(len(ecoli[0:50000]) - window):
    win = ecoli[start:start+window]
    at50.append((win.count('A')+win.count('T')) / window)

#100k
for start in range(len(ecoli[0:100000]) - window):
    win = ecoli[start:start+window]
    at100.append((win.count('A')+win.count('T')) / window)

#whole
for start in range(len(ecoli) - window):
    win = ecoli[start:start+window]
    at.append((win.count('A')+win.count('T')) / window)




fig=plt.figure(figsize=(20,10))

plt.subplot(311)
plt.plot(at50, label="AT", linewidth=3)
plt.suptitle("AT content in the first 50k bases of the E coli genome",fontsize=20) # Note!
plt.title("Window size of "+str(window),fontsize=14)
plt.legend('upper right')

plt.subplot(312)
plt.plot(at100, label="AT", linewidth=3)
fig.supylabel('Fraction of AT bases in the next 1000')
plt.legend('upper right')

plt.subplot(313)
plt.plot(at, label="AT", linewidth=3)
fig.supxlabel('Position on genome')
plt.legend('upper right')

plt.savefig("Chart_ex1.png",transparent=True)

plt.show();
