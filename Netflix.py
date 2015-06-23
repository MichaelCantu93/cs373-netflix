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


import urllib, json
import requests
from math import sqrt
from operator import add
from functools import reduce
from urllib.request import urlopen


url1 = urlopen("http://www.cs.utexas.edu/~ebanner/netflix-tests/ezo55-Average_Viewer_Rating_Cache.json")
url2 = urlopen("http://www.cs.utexas.edu/~ebanner/netflix-tests/pam2599-probe_solutions.json")
average_cache = json.loads(url1.read().decode(url1.info().get_param('charset') or 'utf-8'))
predict_cache = json.loads(url2.read().decode(url2.info().get_param('charset') or 'utf-8'))

global rmse_val
rmse_val = []

count = 0


# ------------
# netflix_eval
# ------------
def netflix_eval (viewer, current_movie) :
    global count
    if "\n" in viewer:
        viewer = viewer[:-1]
    rating = average_cache[viewer]      #simplest will use the users average ratings
    temp = predict_cache[current_movie]
    netflix_rating = temp[viewer]
    rmse_val.extend([(rating - netflix_rating) ** 2])
    count = count + 1
    return '%.2f' % round(rating, 2)


# ------------
# netflix_solve 
# ------------
def netflix_solve (r, w) :
    current_movie = ""
    for s in r :
        if ":" not in s:
            v    = netflix_eval(s, current_movie)
            w.write(str(v) + "\n")
        else:
            current_movie = s
            current_movie = current_movie[:-2]
            w.write(current_movie + ":\n")
    w.write("RMSE = " + str('%.3f' % round(sqrt(reduce(add, rmse_val, 0)/count), 3)) + "\n")
