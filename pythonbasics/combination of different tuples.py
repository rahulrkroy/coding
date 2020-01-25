from itertools import combinations

s=6
l=[1,2,3,4]

for k in range(1,len(l)):    
    p=list(combinations(l,k))
    for i in p:
        c=sum(i)
        if(c==s):
            print(list(i))

print("love you")

    

        

