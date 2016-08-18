a=input()
b=input()
c=input()
d=input()
list=[]
list.append(a)
list.append(b)
list.append(c)
list.append(d)
f=[s.replace(',','') for s in list]
g=[s.replace(' ','') for s in f]
print("sorted elements in ascending order are as follows:")
print("#########")
print (sorted(g))

