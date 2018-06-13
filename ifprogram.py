#! /usr/bin/python2

from time import sleep

number=int(raw_input("Enter a number: "))
if number<0 :
	print "Negative number"
elif number==0 :
	print "Number is 0"
else :
	print "Positive number"
