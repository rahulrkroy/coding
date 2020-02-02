class Queuee:
    def __init__(self,size):
        self.__front=None
        self.__rear=None
        self.__queue=[]
        self.__size=size

    def add(self,data):
        if self.__rear==self.__size-1:
            print("Queue Overflow")
        else:
            if self.__front==None:
                self.__front=0
                self.__rear=0
            else:
                self.__rear+=1
            self.__queue.append(data)

    def pop(self):
        if(self.__front==None):
            print("Underflow")
        else:
            t=self.__queue[0]
            del(self.__queue[0])
            self.__rear-=1
            if(self.__rear==0):
                self.__front=None
                self.__rear-None
            
            print(t,' is popped out')

    def display(self):
        if self.__rear==None:
            print("Stack Empty")
        else:
            for i in range(self.__rear+1):
                print(self.__queue[i])

astack=Queuee(5)

astack.add(1)
astack.add(2)
astack.add(3)
astack.add(4)
astack.pop()
astack.display()
