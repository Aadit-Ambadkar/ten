import sys
import re
from collections import deque

filename = sys.argv[1]

file = open(filename, "r")

contents = file.read()

q = deque()

i = 0
while (i<len(contents)):

    i+=1

print (contents)

print ()
print ()
input("Press Return to Exit (Consumes CPU if you Don't) ")