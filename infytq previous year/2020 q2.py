# longest subarray

s1="11,5,19,2,8,3,4"
l=s1.split(',')
l=[int(x) for x in l]
l.sort()
fib=[]
for i in range(len(l)):
    a=l[i]
    temp=[]
    for j in range(i+1,len(l)):
        b=l[j]
        temp=[]
        temp.append(a)
        temp.append(b)
        k=j+1
        x,y=a,b
        while(k<len(l)):
            if(l[k]== x+y):
                temp.append(l[k])
                x=y
                y=l[k]
            k+=1
        if(len(temp)>2):
            fib.append(temp)

print(fib)

if(fib==[]):
    print(-1)
else:
    t=[len(i) for i in fib]
    m=max(t)
    series=[]
    for i in range(len(t)):
        if(t[i]==m):
            series.append(fib[i])
    s=''
    for i in min(series):
        print(i)


