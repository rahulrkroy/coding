# Given an inmatrix mxn matrix(m,n>3).You have to perform the following operations:
# i) Find the same consecutive numbers in the matrix either vertically, horizontally or diagonally
# such that atleast four consecutive nos. are there.
# ii) If there are more than one such set of numbers then print an integer outnum which is the
# minimum of such consecutive nos.
# iii) If no such no. exists print -1
# Input: First line contains an integer m.
# Second m lines have n space separated integers (note: n was not given)
# Output: An integer outnum or -1 if no such nos. exists
# 5 
# 7 8 9 5 4 2
# 5 7 9 4 5 2
# 6 8 7 9 2 2
# 1 4 2 7 6 2
# 1 1 1 1 1 4
# ans- 1
import sys
# m=int(input())
# if(m<4):
#     sys.exit("wrong input")
m=4
matrix=[[1,8,9,5,4],[1,1,3,4,5],[1,4,1,6,7],[1,1,1,1,1]]
n=5
# matrix=[]
# n=0
# for i in range(m):
#     l=list(map(int,input().split()))
#     if n<len(l):
#         n=len(l)    
#     matrix.append(l)
a=matrix
diag=[]
result=[]
for i in range(m):
    h=[]
    max_array=[]
    max_len=0
    for j in range(n-1):
        if(a[i][j]==a[i][j+1]):
            if(h==[]):
                h.append(a[i][j])
            h.append(a[i][j+1])
        else:
            leng=len(h)
            if(leng>max_len):
                max_len=leng
                max_array=h.copy()
            h=[]
    if(h==[] and len(max_array)>3):
        result.append(max_array)
    elif(len(h)>3):
        result.append(h)



for i in range(n):
    h=[]
    max_array=[]
    max_len=0
    for j in range(m-1):
        if(a[j][i]==a[j+1][i]):
            if(h==[]):
                h.append(a[j][i])
            h.append(a[j+1][i])
        else:
            leng=len(h)
            if(leng>max_len):
                max_len=leng
                max_array=h.copy()
            h=[]
    if(h==[] and len(max_array)>3):
        result.append(max_array)
    elif(len(h)>3):
        result.append(h)

for i in range(m):
    for j in range(n):
        if(i==j):
            diag.append(a[i][j])
h=[]
max_array=[]
max_len=0
for i in range(len(diag)-1):
    if(diag[i]==diag[i+1]):
        if h==[]:
            h.append(diag[i])
        h.append((diag[i+1]))
    else:
        leng=len(h)
        if(leng>max_len):
            max_len=leng
            max_array=h.copy()
        h=[]

if(h==[] and len(max_array)>3):
    result.append(max_array)
elif(len(h)>3):
    result.append(h)

print(len(result))


