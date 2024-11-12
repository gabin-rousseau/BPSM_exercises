#!/usr/bin/python3

import os, sys, subprocess
import numpy as np
import pandas as pd

df = pd.read_csv('eukaryotes.txt',sep="\t")

#Fungal species with 100Mb+ genomes, names
names=list(set(df[(df["Group"]=="Fungi") & (df["Size (Mb)"]>100)]["#Organism/Name"]))
number=len(names)
print(f'There are {number} Fungal species with 100Mb+ genomes\n#####\nTheir names are {names}\n')


