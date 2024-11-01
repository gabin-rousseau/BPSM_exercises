#!/usr/bin/python3

#species name, sequence, gene name, expression level
data=open("data.csv")


for line in data.readlines():
	fields=line.rstrip("\n").split(",")
	species,sequence,gene,expression=str(fields[0]),str(fields[1]),str(fields[2]),float(fields[3])

	if species=="Drosophila melanogaster" or species=="Drosophila simulans":
		print(f"Gene {gene} from species of interest: {species}.")
	if 90<=len(sequence)<=110:
		print(f"Gene {gene} between 90 and 110 bases long: {len(sequence)}.")
	AT_content=(sequence.upper().count("A") + sequence.upper().count("T"))/len(sequence)
	if AT_content<0.5 and expression>200:
		print(f"Gene {gene} has predominant GC content (AT<0.5) and high expression ({expression}).")
	if species!="Drosophila melanogaster" and  (
	   gene.lower().startswith("k") or gene.lower().startswith("h") ):
		print(f"Gene {gene} begins with k or h and isn't from melanogaster.")
	if AT_content<0.45:
		print(f"Gene {gene} has low AT content: {AT_content}.")
	elif 0.45<=AT_content<=0.65:
		print(f"Gene {gene} has medium AT content: {AT_content}.")
	elif AT_content>0.65:
		print(f"Gene {gene} has high AT content: {AT_content}.")
	print("\n####################\n")

data.close()
