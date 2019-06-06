def reducer():
	import sys
	age_ratings = {}
	ans={}
	for line in sys.stdin:
		data = line.strip().split("\t")
		if len(data) !=2:
		 continue
		UserID, Age = data
		if Age in age_ratings:
			age_ratings[Age] = age_ratings[Age]+1
		elif Age not in age_ratings:
			age_ratings[Age] = 1 
	
	for i in age_ratings:
		if i=='1':
			ans['Under-18']=age_ratings[i]
		elif i=='18':
			ans['18-24']=age_ratings[i]
		elif i=='25':
			ans['25-34']=age_ratings[i]
		elif i=='35':
			ans['35-44']=age_ratings[i]
		elif i=='45':
			ans['45-49']=age_ratings[i]
		elif i=='50':
			ans['50-55']=age_ratings[i]
		else:
			ans['56+']=age_ratings[i]
			
	for key in ans:
		print "{0}\t{1}".format(key, ans[key])
 
if __name__ == "__main__":
	reducer()
