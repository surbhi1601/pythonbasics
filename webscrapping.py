#! /usr/bin/python3.4
import sys
from bs4 import BeautifulSoup
import requests

url=input("Enter website")
r=requests.get("http://"+url)
data=r.text
Soup=BeautifulSoup(data)
for link in Soup.find_all('a'):
	print (link.get("href"))
