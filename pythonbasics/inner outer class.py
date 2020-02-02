class outer:
    age=10

    def __init__(self):
        self.age=20

    def display(self):
        print('outer display',self.age)
        self.ob2=self.inner()
        self.ob2.display()

    class inner:
        def __init__(self):
            self.x=9

        def display(self):
            print("Inner display",self.x)

obj=outer()
obj.display()
# obj.ob2.display()
obj.ob2.display()
            