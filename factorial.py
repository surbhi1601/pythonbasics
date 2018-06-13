#! /usr/bin/python2

def factorial(num) :
	if num==1 :
		return num
	else :
		return num*factorial(num-1)

num=input("Enter a number : ")
if num<0 :
	print "Cant find neagtive numbers factorial"
elif num==0:
	print "factorial is 0"
else :
	print "factorial of a given number is " , factorial(num)


