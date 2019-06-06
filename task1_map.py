#!/usr/bin/python
def mapper():
	import sys 
	for line in sys.stdin:
	    data = line.split('::')
	    if len(data) == 4:
		userID, movieID, rating, timestamp = data
		print "{0}\t{1}".format(movieID, rating)
	 
if __name__ == "__main__":
    mapper()
