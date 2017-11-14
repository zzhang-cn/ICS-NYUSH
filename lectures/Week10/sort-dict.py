# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 15:09:00 2016

@author: zhengzhang
"""

mydict = {'carl':40,
          'alan':2,
          'bob':1,
          'danny':3}

print(sorted(mydict.keys()))    

for key in sorted(mydict.keys()):
    print("%s: %s" % (key, mydict[key]))

print(sorted(mydict.values()))

print(sorted(mydict, key = mydict.get))
    
    
    