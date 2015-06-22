#!/usr/bin/env python3

# ------------
# function 
# ------------

#average of movie's ratings
#average of user's ratings
#check user's rating on movies in time period
#check the movie ratings of time period (ex: 50s)
#weight the ratings based on when the user made them
#RMSE at end
global current_movie
current_movie = ""

global rmse_val
rmse_val = []

global count

average_cache
predict_cache

def netflix_eval (viewer) :
    rating = average_cache[viewer]      #simplest will use the users average ratings
    temp = predict_cache[current_movie]
    netflix_rating = temp[viewer]
    rmse_val += (rating - netflix_rating) ** 2
    count += 1
    return rating[0]

def netflix_solve (r, w) :
    for s in r :
        if ":" not in s:
            v    = netflix_eval(s)
            w.write(v + "\n");
        else:
            current_movie = s
            w.write(current_movie + "\n");
    w.write("RMSE = " + sqrt(reduce(add, rmse_val, 0)/count) + "\n");
        
        
        
        
        
        
