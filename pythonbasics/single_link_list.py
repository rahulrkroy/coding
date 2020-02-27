class Node:
    def __init__(self,data=None):
        self.__data=data
        self.__next=None

    def get_data(self):
        return self.__data

    def set_data(self,data):
        self.__data=data

    def get_next(self):
        return self.__next

    def set_next(self,next_node):
        self.__next=next_node

 
class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def insert_at_end(self,data):
        new_node=Node(data)
        if(self.__head==None):
            self.__head=new_node
            self.__tail=new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail=new_node  
        # print(self)
    
    def insert_at_beg(self,data):
        new_node=Node(data)
        if(self.__head==None):
            self.__head=new_node
            self.__tail=new_node
        else:
            new_node.set_next(self.__head)
            self.__head=new_node


    def insert_at_pos(self,pos,data):
        temp=self.__head
        for i in range(pos-1):
            temp=temp.get_next()
        new_node=Node(data)
        new_node.set_next(temp.get_next())
        temp.set_next(new_node)

    def insert_after_element(self,data,data_before):
        temp=self.find_node(data_before)
        new_node=Node(data)
        if(temp==None):
            new_node.set_next(self.__head.get_next())
            self.__head=new_node
            if(self.__tail==None):
                self.__tail=new_node
        else:
            new_node.set_next(temp.get_next())
            temp.set_next(new_node)


    def remove_at_end(self):
        temp=self.__head
        if(self.__head==None):
            print("List Empty")
        else:
            while(temp.get_next().get_next() is not None):
                temp=temp.get_next()
            val=self.__tail.get_data()
            self.__tail=temp
            self.__tail.set_next(None)
            
    def remove_at_beg(self):
        # temp=Node()
        temp=self.__head
        val=self.__head.get_data()
        self.__head=self.__head.get_next()
        # temp.set_next(None)
        del(temp)
        print(val," is deleted")
        
    
    def remove_at_pos(self,pos):
        temp=self.__head
        for i in range(pos-1):
            temp=temp.get_next()
        val=temp.get_next().get_data()
        temp.set_next(temp.get_next().get_next())
        print(val,' is deleted. Bye')
        
    def find_node(self,data):
        temp=self.__head
        while temp is not None:
            val=temp.get_data()
            if(val==data):
                return temp
                break
            temp=temp.get_next()
        return None


    def display(self):
        print("Elements of list are:- ")
        if(self.__head==None):
            print("List Empty")
        else:
            tmp=self.__head
            while tmp is not None:
                val=tmp.get_data()
                print(val)
                tmp=tmp.get_next()
    
    def rev(self):
        self.reverse(self.__head)

    def reverse(self,temp):
        if (temp.get_next()==None or temp==None):
            print(temp.get_data())
            return temp
        else:
            self.reverse(temp.get_next())
            print(temp.get_data())

    def __str__(self):
        temp=self.__head
        msg=[]
        while(temp is not None):
           msg.append(str(temp.get_data()))
           temp=temp.get_next()
        msg=" ".join(msg)
        msg="Linkedlist data(Head to Tail): "+ msg
        return msg

def remove_duplicates(duplicate_list):
    temp = duplicate_list.get_head()
    while(temp.get_next()):
        if temp.get_data() == temp.get_next().get_data():
            temp1=temp
            temp=temp.get_next()
            # print("Removed: "+str(temp1.get_data()))
            duplicate_list.delete(temp1.get_data())
            continue
        temp=temp.get_next()
    duplicate_list.display()
    return duplicate_list


list1=LinkedList()
list1.insert_at_beg("Sugar")
list1.insert_at_end("tea")
list1.insert_at_beg("coffee")
list1.insert_at_beg("pasta")
list1.insert_at_beg("chicken")
list1.insert_at_end("biscuit")
list1.insert_at_pos(2,"chanachur")
list1.remove_at_pos(2)
list1.insert_after_element("susu","chicken")
# list1.rev()
# list1.remove_at_end()
# list1.remove_at_beg()
remove_duplicates(list1)
list1.display()