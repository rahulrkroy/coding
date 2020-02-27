class Stack:
    def __init__(self,size):
        self.__top=-1
        self.__max_size=size
        self.__elements=[None]*self.__max_size

    def get_max_size(self):
        return self.__max_size
        
    def is_full(self):
        if self.__top==self.get_max_size()-1:
            return True
        else:
            return False

    def is_empty(self):
        if self.__top==-1:
            return True
        else:
            return False

    def push(self,data):
        if self.is_full():
            print(f"Stack Overflow. {data} cannot be pushed")
        else:
            self.__top+=1
            self.__elements[self.__top]=data


    def pop(self):
        if self.is_empty():
            print("Underflow")
        else:
            t=self.__elements[self.__top]
            self.__elements[self.__top]=None
            self.__top-=1
            print(t,' is popped out')

    def display(self):
        if self.is_empty():
            print("Stack Empty")
        else:
            for i in range(self.__top+1):
                print(self.__elements[i])

astack=Stack(5)

astack.push(1)
astack.push(2)
astack.push(3)
astack.push(4)
astack.push(5)
astack.push(6)
astack.pop()

astack.display()
