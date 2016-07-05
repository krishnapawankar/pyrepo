#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      krishna
#
# Created:     25/05/2016
# Copyright:   (c) krishna 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

s = "qwertyqweryyyy"
d={}
for l in s:
        d[l] = d.get(l,0) + 1

print(d)


f = open("words.txt")
t={}
while(f):
    x = f.read(40)
    w = str(x).split()
    for i in w:
        t[i] = d.get(i,0) + 1

print(t)

