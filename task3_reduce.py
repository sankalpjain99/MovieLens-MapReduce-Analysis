#!/usr/bin/python
 
def reducer():
    import sys
    num_movies = {}
    oldGenre = None
    oldMovie = None
    Movies = 0
    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) !=2:
		continue
        genre, movieID = data
        if genre in num_movies:
		num_movies[genre] = num_movies[genre]+1
        elif genre not in num_movies:
		num_movies[genre] = 1 
    for key in sorted(num_movies, key=num_movies.get, reverse=True):
	print "{0}\t{1}".format(key, num_movies[key])

if __name__ == "__main__":
    reducer()
