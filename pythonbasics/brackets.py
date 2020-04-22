ob=['','(','((','(((','((((','(((((','((((((','(((((((','((((((((','(((((((((']
cb=['',')','))',')))','))))',')))))','))))))',')))))))','))))))))',')))))))))']

for _ in range(int(input())):
    num=input()
    l=[]
    s1=''
    for i in num:
        if(s1==''): 
            s1+=i
        else:
            if(s1[0]==i):
                s1+=i
            else:
                l.append(s1)
                s1=''
                s1+=i
    
    l.append(s1)
    print("l=",l)
    s1=''
    for i in range(len(l)):
        n=int(l[i][0])
        s1+=ob[n]+l[i]+cb[n]
    print('ans=',s1)
    