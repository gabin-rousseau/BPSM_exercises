#!/usr/bin/python3

dna="ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"

print(dna.find("GAATTC"))
print(dna[21:28])

print("Cut between nt 21 and nt 22")

dna1=dna[:22]
dna2=dna[22:]

print(f"The length of the second fragment is {len(dna2)}.")
