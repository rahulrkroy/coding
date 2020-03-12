from itertools import permutations;
# Enter your code here. Read input from STDIN. Print output to STDOUT

def perm(l):
    leng=len(l)
    l2=[]
    for i in range(leng):
        for j in range(leng):
            for k in range(leng):
                if(i!=j and i!=k and j!=k):
                    l2.append(l[i]+l[j]+l[k])
    return l2


l=input().split(',')
# l=[int(x) for x in l]
print("l=",l)
# l1=list(permutations(l,3))
l1=perm(l)
l1=list(set(l1))
print(l1)
len=len(l1)
l2=[]
for i in l1:
    l2.append(i[0]+i[1]+i[2])
l2=[int(x)for x in l2]
print(max(l2),len,sep=",")
# print(l2)

