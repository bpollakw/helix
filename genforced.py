## genforced.py 
# Forced GC content sequence generator

import os
import sys
import re
import itertools
from random import randint

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation, CompoundLocation
from Bio.Alphabet import IUPAC

def main():
	a = ""
	GC = int(sys.argv[2])
	for i in range(int(sys.argv[1])):
		value = randint(0, 99)
		if value < GC:
			a = a + str(randint(0, 1))
		else:
			a = a + str(randint(2, 3))
		
	a = re.sub("0", "C", a)
	a = re.sub("1", "G", a)
	a = re.sub("2", "A", a)
	a = re.sub("3", "T", a)
	

	print a
	
if len(sys.argv) < 3:
    sys.exit("###\n\nUsage: python genforced.py [LENGTH] [GC%]\n\n###")

main()
