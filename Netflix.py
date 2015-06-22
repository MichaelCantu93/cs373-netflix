#!/usr/bin/env python3

# ------------
# function 
# ------------

#average of movie's ratings
#average of user's ratings
#check user's rating on movies in time period
#check the movie ratings of time period (ex: 50s)
#weight the ratings based on when the user made them
#import netflix-tests
#r = netflix-tests.get('https://raw.githubusercontent.com/cs373-summer-2015/netflix-tests/master/pam2599-probe_solutions.json')

"""
import urllib, json, urllib.request
url1 = "http://www.cs.utexas.edu/~ebanner/netflix-tests/BRG564-Average_Movie_Rating_Cache.json"
url2 = "http://www.cs.utexas.edu/~ebanner/netflix-tests/pam2599-probe_solutions.json"
response1 = urllib.urlopen(url1)
response2 = urllib.urlopen(url2)
average_cache = json.loads(response1.read())
predict_cache = json.loads(response2.read())
"""

import requests
from math import sqrt
from functools import reduce
r1 = requests.get('http://www.cs.utexas.edu/~ebanner/netflix-tests/BRG564-Average_Movie_Rating_Cache.json')
r2 = requests.get('http://www.cs.utexas.edu/~ebanner/netflix-tests/pam2599-probe_solutions.json')
average_cache = r1.json()
predict_cache = r2.json()


global current_movie
current_movie = ""

global rmse_val
rmse_val = []

global count
count = 0


# ------------
# netflix_eval
# ------------
def netflix_eval (viewer) :
    rating = average_cache[viewer]      #simplest will use the users average ratings
    temp = predict_cache[current_movie]
    netflix_rating = temp[viewer]
    rmse_val += (rating - netflix_rating) ** 2
    count += 1
    return rating[0]


# ------------
# netflix_solve 
# ------------
def netflix_solve (r, w) :
    for s in r :
        if ":" not in s:
            v    = netflix_eval(s)
            w.write(v + "\n");
        else:
            current_movie = s
            w.write(current_movie + "\n");
    w.write("RMSE = " + sqrt(reduce(add, rmse_val, 0)/count) + "\n");
        
        
        
        
        
        
