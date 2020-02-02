class abc:
	age=10
	def __init__(self):
		self.age=30
		print("default constructor")

	def display(self):
		print("Output Display")
		print(self.age)
	
	@classmethod
	def clmethod(cls):
		print('class variable',cls.age)
	
	@staticmethod
	def statmethod():
		print(abc.age*3)



ob1=abc()
ob2=abc()

ob1.display()
abc.clmethod()
print('naem','roll')
abc.statmethod()



# ob1.display()

