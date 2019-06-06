def reducer():
	import sys
	num_ratings = {}
	for line in sys.stdin:
		data = line.strip().split("\t")
		if len(data) !=2:
		 continue
		movieID, rating = data
		if rating in num_ratings:
			num_ratings[rating] = num_ratings[rating]+1
		elif rating not in num_ratings:
			num_ratings[rating] = 1 
	
	for key in num_ratings:
		print "{0}\t{1}".format(key, num_ratings[key])
 
if __name__ == "__main__":
	reducer()
