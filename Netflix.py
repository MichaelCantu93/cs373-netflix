#!/usr/bin/env python3


import urllib, json
import requests
from math import sqrt
from operator import add
from functools import reduce
from urllib.request import urlopen

#to open the three urls needed for the program
url1 = urlopen("http://www.cs.utexas.edu/~ebanner/netflix-tests/ezo55-Average_Viewer_Rating_Cache.json")
url2 = urlopen("http://www.cs.utexas.edu/~ebanner/netflix-tests/pam2599-probe_solutions.json")
url3 = urlopen("http://www.cs.utexas.edu/~ebanner/netflix-tests/BRG564-Average_Movie_Rating_Cache.json")

average_VIEWER_cache = json.loads(url1.read().decode(url1.info().get_param('charset') or 'utf-8')) #use cache with average viewer ratings (their average is 3.675)
predict_cache = json.loads(url2.read().decode(url2.info().get_param('charset') or 'utf-8')) #use cache with all the netflix ratings they predicted (for RSME)
average_MOVIE_cache = json.loads(url3.read().decode(url3.info().get_param('charset') or 'utf-8')) #use cache with average movie ratings (their average is 3.228)

global rmse_val         #global list to store the differences squared for RSME
rmse_val = []
 
count = 0          #for mean of RSME


# ------------ 
# netflix_eval
# ------------
def netflix_eval (viewer, current_movie) :
    global count                            #had to reference as global in here or error occurred 
    if "\n" in viewer:                      #need to remove new line from the viewer string so it can be used as index
        viewer = viewer[:-1]
    if "\r" in viewer:
        viewer = viewer[:-1]
    assert "\r" not in viewer
    assert "\n" not in viewer

    viewer_rating = average_VIEWER_cache[viewer]           #get viewer rating based on viewer string from cache     
    movie_rating = average_MOVIE_cache[current_movie]     #get movie rating based on current movie from movie cache
    
    avg_all_users = 3.675                                   #was found by avg all the users ratings ever

    """
    this method here produces RMSE of about .972, we decided to use this cause we couldn't get 
    our method with variance to go below 1.000, we tried this using the avg of all movie ratings
    and the avg for all users, and the users worked better. this way it takes the offset of the
    viewer from the avg, and the movie rating from the avg (both of which could be pos or neg) and
    applies this to the avg itself, which gives a decent approximation of the rating, the code runs
    in less than one minute, the part that takes long is just the reading in of the input file, but 
    the actual calculations are fast
    """
    rating = avg_all_users + (viewer_rating - avg_all_users) + (movie_rating - avg_all_users)        

    temp = predict_cache[current_movie]                 #so you get dictionary from the dictionary of netflix predictions
    netflix_rating = temp[viewer]               #then you get the actual rating from the dictionary you just got
    rmse_val.extend([(rating - netflix_rating) ** 2])       #add the value of the difference squared to the list
    count = count + 1                                 #increase count for mean
    assert count is not 0

    return '%.2f' % round(rating, 2)                 #return the rating with rounding to 2 decimal places


# ------------
# netflix_solve 
# ------------
def netflix_solve (r, w) :
    current_movie = ""                              #current movie starts null
    assert type(current_movie) is str
    for s in r :                                          
        if ":" not in s:                           #checks if current input is not a movie title
            v    = netflix_eval(s, current_movie)  #call eval with the viewer string and the current movie
            assert type(v) is str
            w.write(v + "\n")                      #write this to output
        else:
            current_movie = s              #if ":" in string, its a movie title, set current movie
            current_movie = current_movie[:-2]          #remove the newline and : so it can be used to index
            assert type(current_movie) is str
            w.write(current_movie + ":\n")       #write it to output
    #at end write the rmse to output, used reduce with add and seed at 0, also rounded to 2 decimal places
    w.write("RMSE = " + str('%.2f' % round(sqrt(reduce(add, rmse_val, 0)/count), 2)) + "\n")


