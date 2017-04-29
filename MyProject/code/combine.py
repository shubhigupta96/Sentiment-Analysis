"""This code combines the output of the tokeniser and the input tweet set and returns the final input file in the following format"""
""" tweet Id, Tweet tokens, POS tokens, label """

import sys
from itertools import izip

def main():

	if len(sys.argv)!=4:
		print "Usage :: python combine.py trainingDatasetProcessed trainingTokenised finalTrainingInput"
		sys.exit(0)

	data = []
	f1 = open(sys.argv[1], 'r')
	f2 = open(sys.argv[2], 'r')
	for line1, line2 in izip(f1,f2):
		words1 = line1.strip().split('\t')
		words2 = line2.strip().split('\t')
		string = words1[0] + '\t' + words2[0] + '\t' + words2[1] + '\t' + words1[2] +'\n'
		data.append(string)
	f1.close()
	f2.close()
	print data
	f = open(sys.argv[3], 'w')
	f.write("".join(data))
	f.close()

if __name__ == "__main__":
	main()
		