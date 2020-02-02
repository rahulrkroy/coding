
def equalStacks(h1, h2, h3):
    #
    # Write your code here.
    s1=sum(h1)
    s2=sum(h2)
    s3=sum(h3)
    h1.reverse()
    h2.reverse()
    h3.reverse()
    
    while((s1!=s2) and (s1!=s3)):
        m=max(s1,s2,s3)
        if(s1==0 or s2==0 or s3==0):
            break
        if max==s1:
            t=h1.pop()
            s1-=t
            print('s1=',s1)
        elif max==s2:
            t=h2.pop()
            s2-=t
            print('s2=',s2)
        elif max==s3:
            t=h3.pop()
            s3-=t
            print('s3=',s3)
    
    return s1




h1=[3,2,1,1,1]
h2=[4,3,2]
h3=[1,1,4,1]

result = equalStacks(h1, h2, h3)

print(result)