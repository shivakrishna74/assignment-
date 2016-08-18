import string
sentence=input('')
c=[]
l=[]
t=len(sentence)
try:
    for i in range(0,t):        
        if sentence[i].isupper()==True:
            c.append(sentence[i])
        elif sentence[i].islower()==True:
            l.append(sentence[i])
        else:
            pass
except ValueError:
    print("error")
print(c)
print(l)
print(len(c))
print(len(l))
