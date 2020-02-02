from collections import deque

d=deque([1,2,3,4,5,6])

print(len(d))

d.append(3)
d.appendleft(2)

print(d)

print(d.pop())
print(d.popleft())

d.insert(4,9)
d.remove(2)
print(d)

print(d.count(3))

l2=[3,2,1]
l3=[9,8,7]
d.extend(l2)
d.extendleft(l3)
print(d)

d.reverse()
print(d)

