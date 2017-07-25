# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 13:04:29 2017

@author: T3
"""

"""
If you sum all of the divisors of X (except X) to get Y and you sum all of the divisors of Y (except Y) to get X then X and Y are 'Friends'. We need a program to find all of the friends between 2 and N.

One way to do this is to iterate through all of the numbers less than or equal to half of N to find which divide into N. Then when you have all of them you add them together and find all of the divisors of that number. If those divisors add up to the first number then you have a pair of 'friends'.

However, if we only compute up to sqrt(N) rather than N/2 then we can simply use division to find the remaining divisors.
"""
import math

def findDivisors(number):
    divisors = []
    for i in range(1,int(math.sqrt(number)+1)):
        remainder = number % i
        if remainder == 0:
            divisors.append(i)
    divisorsListThatWontChange = divisors
    #print(divisorsListThatWontChange)
    #print(divisors)
    for m in range(1,len(divisorsListThatWontChange)):
        additionalFactor = int(number/divisors[m])
        if additionalFactor == divisors[m]:
            next
        else:
            divisors.append(additionalFactor)
    #print(divisors)
    return divisors

def findFriends(limit):
    for i in range(2, limit+1):
        divisorsOfFirstLimit = findDivisors(i)
        #print(divisorsOfFirstLimit)
        sumDivisorsOfFirstLimit = sum(divisorsOfFirstLimit)
        #print(sumDivisorsOfFirstLimit)
        divisorsOfSecondLimit = findDivisors(sumDivisorsOfFirstLimit)
        #print(divisorsOfSecondLimit)
        sumDivisorsOfSecondLimit = sum(divisorsOfSecondLimit)
        #print(sumDivisorsOfSecondLimit)
        if sumDivisorsOfSecondLimit == i:
            print(sumDivisorsOfFirstLimit, i)

findFriends(66928)

        
