---
layout: post
title: "Some random python tricks"
subtitle: ""
date:   2016-06-20 10:00:00
---

The following are just a collection of some useful shortcuts and tools I've found in Python over the years. Hopefully you find them helpful.

more advance pyDuffers like me can look here vjex/PyTricks

**Swapping Variables**

    x = 6
    y = 5
    x, y = y, x
     
    print x
    >>> 5
    print y
    >>> 6



**Inline if Statement**

    print "Hello" if True else "World"
    >>> Hello



**Concatenations**

The last one is a pretty cool way to combine objects of two different types.

    nfc = ["Packers", "49ers"]
    afc = ["Ravens", "Patriots"]
    print nfc + afc
    >>> ['Packers', '49ers', 'Ravens', 'Patriots']



    print str(1) + " world"
    >>> 1 world
     



    print `1` + " world"
    >>> 1 world


 

    print 1, "world"
    >>> 1 world



    print nfc, 1
    >>> ['Packers', '49ers'] 1



**Number Tricks**


    #Floor Division (rounds down)
    print 5.0//2
    >>> 2


 

    #2 raised to the 5th power
    print 2**5
    >> 32



**Be careful with division and floating point numbers.**


    print .3/.1
    >>> 2.9999999999999996
     
    print .3//.1
    >>> 2.0



**Numerical Comparison**
This is a pretty cool shortcut that I haven't seen in too many languages.

    x = 2
     
    if 3 > x > 1:
        print x
    >>> 2
     
    if 1 < x > 0:
        print x
    >>> 2



**Iterate Through Two Lists at the Same Time**


    nfc = ["Packers", "49ers"]
    afc = ["Ravens", "Patriots"]
     
    for teama, teamb in zip(nfc, afc):
        print teama + " vs. " + teamb
     
    >>> Packers vs. Ravens
    >>> 49ers vs. Patriots



**Iterate Through List With an Index**


    teams = ["Packers", "49ers", "Ravens", "Patriots"]
    for index, team in enumerate(teams):
        print index, team
     
    >>> 0 Packers
    >>> 1 49ers
    >>> 2 Ravens
    >>> 3 Patriots



**List Comprehension**

With a list comprehension we can turn this:

    numbers = [1,2,3,4,5,6]
    even = []
    for number in numbers:
        if number%2 == 0:
            even.append(number)



Into this:

    numbers = [1,2,3,4,5,6]
    even = [number for number in numbers if number%2 == 0]



Pretty sweet huh?

**Dictionary Comprehension**

Similar to the list comprehension we can also do a dictionary comprehension like this:

    teams = ["Packers", "49ers", "Ravens", "Patriots"]
    print {key: value for value, key in enumerate(teams)}
    >>> {'49ers': 1, 'Ravens': 2, 'Patriots': 3, 'Packers': 0}




**Initialize List Values**

    items = [0]*3
    print items
    >>> [0,0,0]



**Converting a List to a String**

    teams = ["Packers", "49ers", "Ravens", "Patriots"]
    print ", ".join(teams)
    >>> 'Packers, 49ers, Ravens, Patriots'



**Get Item From Dictionary**

I'll admit that try/except code doesn't look the prettiest. Here's a simple way to fix that with dictionaries. This will try to find the key in the dictionary and if it can't be found it will set the variable to the second parameter.
Instead of:

    data = {'user': 1, 'name': 'Max', 'three': 4}
    try:
        is_admin = data['admin']
    except KeyError:
        is_admin = False



Do this:

    data = {'user': 1, 'name': 'Max', 'three': 4}
    is_admin = data.get('admin', False)



**Taking a Subset of a List**

Sometimes you only want to run code over a portion of a list. Here are a few ways you can get the subset of a list.

    x = [1,2,3,4,5,6]
     
    #First 3 
    print x[:3]
    >>> [1,2,3]
     
    #Middle 4
    print x[1:5]
    >>> [2,3,4,5]
     
    #Last 3
    print x[-3:]
    >>> [4,5,6]
     
    #Odd numbers
    print x[::2]
    >>> [1,3,5]
     
    #Even numbers
    print x[1::2]
    >>> [2,4,6]



**FizzBuzz in 60 Characters**

Here's a short, fun way to solve the problem.

    for x in range(1,101):print"Fizz"[x%3*4:]+"Buzz"[x%5*4:]or x
     



**Collections**

In addition to python's built in datatypes they also include a few extra for special use cases in the collections module.

    from collections import Counter
     
    print Counter("hello")
    >>> Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})



**Itertools**

Along with the collections library python also has a library called itertoolswhich has really cool efficient solutions to problems.

    from itertools import combinations
     
    teams = ["Packers", "49ers", "Ravens", "Patriots"]
    for game in combinations(teams, 2):
        print game
     
    >>> ('Packers', '49ers')
    >>> ('Packers', 'Ravens')
    >>> ('Packers', 'Patriots')
    >>> ('49ers', 'Ravens')
    >>> ('49ers', 'Patriots')
    >>> ('Ravens', 'Patriots')



**False == True**

This is more of a fun one than a useful technique. In python True and False are basically just global variables. Thus:

    False = True
    if False:
        print "Hello"
    else:
        print "World"
     
    >>> Hello
     



one more :
Useful for working with the interpreter. Underscore uses last result.

    >>> 2 + 2 
    4
    >>> _ * 2 
    8
    >>> _ + 1 
    9



Thanks for reading!