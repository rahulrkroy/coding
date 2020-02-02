class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self,other):
        m3=self.m1+other.m1
        m4=self.m2+other.m2
        s3= student(m3,m4)
        return s3

        # printing objects
    def __str__(self):
        return('{} {}'.format(self.m1,self.m2))



s1=student(10,20)
s2=student(30,40)

s3=s1+s2
print(s3.m1)
print(s3.m2)

print(s3)