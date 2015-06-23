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
url3 = urlopen("http://www.cs.utexas.edu/~ebanner/netflix-tests/BRG564-Average_Movie_Rating_Cache.json")
url4 = urlopen("http://www.cs.utexas.edu/~ebanner/netflix-tests/ezo55-Average_Viewer_Rating_And_True_Variance_Cache.json")
average_VIEWER_cache = json.loads(url1.read().decode(url1.info().get_param('charset') or 'utf-8'))
predict_cache = json.loads(url2.read().decode(url2.info().get_param('charset') or 'utf-8'))
average_MOVIE_cache = json.loads(url3.read().decode(url3.info().get_param('charset') or 'utf-8'))
variance_cache = json.loads(url4.read().decode(url4.info().get_param('charset') or 'utf-8'))

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
    assert "\n" not in viewer

    viewer_rating = average_VIEWER_cache[viewer]      
    movie_rating = average_MOVIE_cache[current_movie]
    t = variance_cache[viewer]
    variance = t[1]
    s = sqrt(variance)
    if variance < 1.3:
        rating = ((2-s)*viewer_rating + s*movie_rating)/2           #1.9 and .14 gets .999, so does .15
    else:
        rating = (s*viewer_rating + (2-s)*movie_rating)/2 
    temp = predict_cache[current_movie]
    netflix_rating = temp[viewer]
    rmse_val.extend([(rating - netflix_rating) ** 2])
    count = count + 1
    assert count is not 0

    return '%.2f' % round(rating, 2)


# ------------
# netflix_solve 
# ------------
def netflix_solve (r, w) :
    current_movie = ""
    assert type(current_movie) is str
    for s in r :
        if ":" not in s:
            v    = netflix_eval(s, current_movie)            
            assert type(v) is str
            #w.write(v + "\n")
        else:
            current_movie = s
            current_movie = current_movie[:-2]
            assert type(current_movie) is str
            #w.write(current_movie + ":\n")
    w.write("RMSE = " + str('%.3f' % round(sqrt(reduce(add, rmse_val, 0)/count), 3)) + "\n")



