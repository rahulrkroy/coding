class Stack:
    def __init__(self,size):
        self.__top=None
        self.__stack=[]
        self.__size=size

    def add(self,data):
        if self.__top==self.__size-1:
            print("Stack Overflow")
        else:
            if self.__top==None:
                self.__top=0
            else:
                self.__top+=1
            self.__stack.append(data)


    def pop(self):
        if(self.__top==None):
            print("Underflow")
        else:
            t=self.__stack.pop()
            if(self.__top==0):
                self.__top=None
            else:
                self.__top-=1
            print(t,' is popped out')

    def display(self):
        if self.__top==None:
            print("Stack Empty")
        else:
            for i in range(self.__top+1):
                print(self.__stack[i])

astack=Stack(5)

astack.add(1)
astack.add(2)
astack.add(3)
astack.add(4)
astack.pop()
astack.display()
