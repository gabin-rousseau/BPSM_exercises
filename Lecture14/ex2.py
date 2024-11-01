#!/usr/bin/python3

from collections import Counter

#dna=input("What is the DNA sequence?")
#dna=dna.upper()
dna="ATCATATGTC"

k=input("What k? (At least 1.)")
k=int(k)
n=input("What n? (At least 0.)")
n=int(n)

k_mers=[]


for i in range(len(dna)-k+1):
	k_mers.append(dna[i:i+k])

k_counts=Counter(k_mers)

for key in k_counts.keys():
	if k_counts[key]>n:
		print(f"{k}-mer {key} occurs more than {n} time(s).")




