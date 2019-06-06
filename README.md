# MovieLens-MapReduce-Analysis
MapReduce code to find some interesting facts about MovieLens data. Matplotlib,pandas,numpy also used to produce visual outputs to support our facts.

## Requirements

* Apache Hadoop
* Cloudera(In this case) / Linux
* Python3
* Numpy,Pandas,Matplotlib,Seaborn

## Dataset
Dataset taken from https://grouplens.org/datasets/movielens/
* Movies.dat

     Movie information is contained in the file movies.dat. Each line of this file represents one movie, and has the following format: 

     MovieID::Title::Genres

     MovieID is the real MovieLens id.

* Users.dat

    User information is in the file "users.dat" and is in the following format: 

    UserID::Gender::Age::Occupation::Zip-code


    All demographic information is provided voluntarily by the users and is not checked for accuracy. Only users who have provided some demographic information are included in this data set.

    Gender is denoted by a "M" for male and "F" for female - Age is chosen from the following ranges:
    * 1: "Under 18" 
    * 18: "18-24" 
    * 25: "25-34" 
    * 35: "35-44" 
    * 45: "45-49" 
    * 50: "50-55" 
    * 56: "56+"
    
    
    Occupation is chosen from the following choices:
    * 0: "other" or not specified 
    * 1: "academic/educator" 
    * 2: "artist" 
    * 3: "clerical/admin" 
    * 4: "college/grad student" 
    * 5: "customer service" 
    * 6: "doctor/health care" 
    * 7: "executive/managerial" 
    * 8: "farmer" 
    * 9: "homemaker" 
    * 10: "K-12 student" 
    * 11: "lawyer" 
    * 12: "programmer" 
    * 13: "retired" 
    * 14: "sales/marketing" 
    * 15: "scientist"
    * 16: "self-employed" 
    * 17: "technician/engineer" 
    * 18: "tradesman/craftsman" 
    * 19: "unemployed" 
    * 20: "writer"

* Ratings.dat

    All ratings are contained in the file ratings.dat. Each line of this file represents one rating of one movie by one user, and has the following format: UserID::MovieID::Rating::Timestamp
    
    The lines within this file are ordered first by UserID, then, within user, by MovieID. 12Ratings are made on a 5-star scale, with half-star increments.
    
    Timestamps represent seconds since midnight Coordinated Universal Time (UTC) of January 1, 1970.

## Task Performed
### Task1
Finding and sorting users on the basis of the no of movies they rated. 

In this task, from the given dataset we’ll find a distribution for the number of movies rated by a user - that is, the number of users who have rated 1 movie, 2 movies, 3 movies etc. This will give us an analysis that how many persons who rated the movie and based on the number of ratings he/she can estimate the content in the movie.

File used: ratings.dat used

### Task2
To compute the frequency of user age groups that gives ratings to movies in order to find out the highest rated movie.

File used: users.dat
### Task3
Sorting and organizing all the movies on the basis of genres

In this task, from the given dataset we’ll find the distribution of movies by different genres available like Drama, Comedy, etc. This will give the user a wide perspective with which he can decide which category is more reviewed.

File used: movies.dat

## How to run 

* Copy/paste all your mapper, reducer and data set files on Desktop
* Now on Cloudera , open Terminal and execute the following commands

    ```bash
    cd Desktop
    hdfs dfs -mkdir "Directory Name"
    hdfs dfs -put <mapper_file> "Directory_Name"/<mapper_file>
    hdfs dfs -put <reducer_file> "Directory_Name"/<reducer_file>
    hdfs dfs -put <data_set file> "Directory_Name"/<data_set file>
    chmod +x <mapper_file> 
    chmod +x <reducer_file> 
    cat <data_set file> | python <mapper_file> | python <reducer_file>
    ```
    


