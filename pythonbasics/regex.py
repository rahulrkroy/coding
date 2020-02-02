import re

name='''hello world 
        this is me
        sat, cat , mat,rat 
        
        12 123 1234 12345
        '''

k=re.findall('\d{0,9}4',name)

for i in k:
    print(i)
