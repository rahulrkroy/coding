
def divisor(n):
    a=[]
    for i in range(1,n):
        if(n%i==0):
            a.append(i)
    return(a)

for _ in range(int(input())):
    n=int(input())
    a=divisor(n)
    if sum(a)==n:
        print("YES")
    else:
        print("NO")

