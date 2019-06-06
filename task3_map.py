def mapper():
    import sys
 
    for line in sys.stdin:
        data = line.strip().split('::')
        if len(data) == 3:
            movieID, title, genre = data
            data2 = genre.split('|')
            for item in data2:
                print "{0}\t{1}".format(item, movieID)
 
if __name__ == "__main__":
    mapper()
