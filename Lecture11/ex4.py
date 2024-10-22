#!/usr/bin/python3

dna="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

exon1=dna[:63]
intron=dna[63:90]
exon2=dna[90:]
spliced_dna=exon1 + exon2

print(f"The length of the coding sequence is {len(spliced_dna)}, which represents about {round(len(spliced_dna)/len(dna)*100)}% of the original sequence")

print(exon1 + intron.lower() + exon2)
print("Exons and intron defined properly:", dna == exon1 + intron + exon2)
