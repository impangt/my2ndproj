#!/usr/bin/python
# Filename : helloworld.py
print ('Hello World' )

def calculate1(x):
    istr=str(x)
    len0=len(istr)
    c=istr[len0-1]
    k=int(c)
    j=int(x/10)
    m=j*4+k
    print(x,k,"-->",j, "x 4 +",c,"=",m)
    return m

i=222
while i>=10 :
     i=calculate1(i)







