#! /usr/bin/python2

import commands

print "***** Enter commands ******"
x=''' Press 1 for date /n Press 2 for calender '''
print x
value=raw_input("Enter your  choice: ")
if value=="1" :
	value1=commands.getoutput("date")
	print value1
elif value=="2" :
	value2=commands.getoutput("cal")
	print value2
else :
	print "wrong choice" 
