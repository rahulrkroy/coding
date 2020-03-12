# Input: rhdt:246, ghftd:1246
# Output: trhd, ftdgh
# Explanation:
# Here, every string (rhdt : 1246) is associated with a number, separated by semicolon, if sum of
# square of digit is even the rotate the string right by 1 position. If square of digit is odd the rotate
# the string left by 2 position.
# For first case:
# 2*2+4*4+6*6=84 which is even so rotate string, rotate right by 1 so ”rhdt” will be “trhd”
# For second case:
# 1*1+2*2+4*4+6*6=85 which is odd so rotate string left by 2 so “ghftd” will be “ftdgh”
def rotate_left(s):
    return(s[2:]+s[0:2])
def rotate_right(s):
    return(s[-1]+s[0:-1])

s="rhdt:246, ghftd:1246"
s=s.split(', ')
s=[i.split(':') for i in s]
print(s)
s1=[]
for i in range(len(s)):
    num=s[i][1]
    temp_sum=0
    for j in num:
        temp_sum+= (int(j)**2)
    print(temp_sum)
    if(temp_sum%2==0):
        s2=rotate_right(s[i][0])
    else:
        s2=rotate_left(s[i][0])
    s1.append(s2)
    
print(*s1,sep=',')
