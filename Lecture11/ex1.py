#!/usr/bin/py

dna="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

a_count=dna.count("A")
t_count=dna.count("T")
at_ratio=(a_count+t_count)/len(dna)

print(a_count,t_count,at_ratio)


