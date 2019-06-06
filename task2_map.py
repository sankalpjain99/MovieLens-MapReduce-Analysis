#!/usr/bin/python
def mapper():
	import sys 
	for line in sys.stdin:
	    data = line.split('::')
	    if len(data) == 5:
		UserID,Gender,Age,Occupation,Zip = data
		print "{0}\t{1}".format(UserID, Age)
	 
if __name__ == "__main__":
    mapper()
