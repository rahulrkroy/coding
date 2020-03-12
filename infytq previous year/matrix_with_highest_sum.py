# Take string input then form all possible mXm square matrix, and print the matrix with
# maximum sum.
# In case, two or more square matrix has maximum sum then print largest matrix followed by next
# largest matrix and so on.
# In case, more than one matrix has same size print in order of their occurrence.
# INPUT: 6, 3, 6, 20, 3, 6,-15, 3, 3
# OUTPUT:
# 6 3 6
# 20 3 6
# -15 3 3

# 6 3
# 6 20

# 6 20
# 3 6

# Explanation:-
# 6 3 6
# 20 3 6 -> its sum is 35 and is order 3*3,
# -15 3 3
# 6 3
# 6 20 -> its sum is 35 and is order 2*2,
# 6 20
# 3 6 -> its sum is 35 and is order 2*2
import math
inp="6, 3, 6, 20, 3, 6,-15, 3, 3"
num=list(map(int, inp.split(",")))
length=int(math.sqrt(len(num)))

for i in range(length):
    for j in range()





# for i in range(0,len(num),length):
#     for j in range(length):
#         print(num[i+j],end=' ')
#     print("")
