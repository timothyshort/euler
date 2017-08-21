#!/usr/bin/env python
import time

def findPalindrome(digit):
	palindromes = [[]]
	maxNumber = 10**digit-1
	minNumber = 0
	x=maxNumber

	#Start at the maximum number and decrement by one
	#Loop while that number is greater than the minimum number
	#This condition drastically reduces the number of iterations
	while ((x) > minNumber):
		x-=1
		for y in range(x,1,-1):
			product = x*y
			if (str(product) == str(product)[::-1]):
				palindromes+= [[x,y,product]]
				display(x,y,product)

				#We don't need to know any palindromes below the minimum
				#Minimum number is the highest number of the multiplicand
				if y > minNumber:
					minNumber = y
					print " NEW MIN " + str(y)
				break
	return printPalindromes(palindromes)

def display(x,y,product):
	print "PALINDROME:",
	print str(x) + " x " + str(y) + " = " + str(product)

def printPalindromes(list):
	max = list[1][2]
	maxIndex = 0
	for i in range(len(list)-1,1,-1):
		if (list[i][2] > max):
			max = list[i][2]
			maxIndex = i
	return (list[maxIndex][0],list[maxIndex][1],list[maxIndex][2])

digits = 3
start = time.time()
maxLocation = findPalindrome(digits)
elapsed = time.time() - start

print maxLocation
print "Time elapsed",
print elapsed

print "********"

s = time.time()
print(max(a * b for a in range(100, 1000) for b in range(a, 1000) if str(a * b) == str(a * b)[::-1]))
e = time.time() - s
print e

print "********"

print "My algorithm runs ",
print e/elapsed,
print " times faster"
