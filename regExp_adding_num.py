import re
sum1=0
file=open('sample.txt','r')
for line in file:
    line=line.rstrip()
    stuff=re.findall('([0-9]+)',line)
    for x in stuff:
        num=int(x)
        sum1=sum1+num
print(sum1)
