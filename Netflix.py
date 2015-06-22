#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

global cache                                        #make global cache which is a dictionary
cache = {}

def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    assert type(i) is int                            #make sure they're numbers
    assert type(j) is int
    
    assert i >=1 and i <= 999999                     #make sure in proper range
    assert j >=1 and j <= 999999

    if i > j:                                        #make sure that the indeces are in proper order, if not switch them
        temp = 0
        temp = i
        i = j
        j = temp

    assert i <= j                                    #check again if now in proper order
   
    index = 0                                        #to store the number you currently got the cycle length from
    maxCount = 0                                     #max cycle length
    count = 1                                        #the temp variable that counts the cycle length 
     
    for x in range(i, j+1):                          #go through range
        index = x                                    #save number you're working with to store in cache later
        while x > 1:
            if x in cache:            
                count = count + cache[x] - 1    #if in cache already, use the current count you have, take the cache value, and minus 1
                x = 1                                #set to 1 so you exit the loop
            else:
                if x%2 == 0:                         #if even shift by 1 to do a divide by 2
                    x = x >> 1
                    count += 1
                else:                                #this is how we discussed in class, this is equivalent to 3x+1 and then divide by 2 because
                    x = x + (x >> 1) + 1             #you know the next number is even
                    count += 2
                    
        if not index in cache:                  #use index value you saved before (which was the x in the range) and see if in cache
            cache[index] = count                #if it wasnt, add it now with the cycle length you found
            
        if count >= maxCount:                        #set the maxcount if the count you found was higher
            maxCount = count
            count = 1
        else:
            count = 1
            
    assert maxCount >= count                         #last assertions to check if maxCount was set properly
    assert maxCount > 0

    return maxCount

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = collatz_read(s)
        v    = collatz_eval(i, j)
        collatz_print(w, i, j, v)
