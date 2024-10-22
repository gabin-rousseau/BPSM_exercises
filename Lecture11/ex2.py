#!/usr/bin/python3

dna="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
complement=""

for nt in dna:
    if nt=="A":
        complement+="T"
    elif nt=="T":
        complement+="A"
    elif nt=="C":
        complement+="G"
    elif nt=="G":
        complement+="C"
print(complement)
