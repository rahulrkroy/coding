st="Robert:6973,Tina:67281,Jo:38765"
x=st.split(',')
s1=""
y=[i.split(':') for i in x]
print(y)
for i in y:
    l=len(i[0])
    for j in range(l,0,-1):
        k=str(j)
        p=i[1].find(k)
        if(p!=-1):
            s1+=i[0][j-1]
            break
    else:
        s1+='X'
print("s1=",s1)
