class Student:
	def __init__(self, name, rollnumber, m1, m2, m3):
		self.name = name
		self.m1 = m1
		self.m2 = m2
		self.m3 = m3
    self.rollnumber = rollnumber	

	def sum(self):
		return self.m1 + self.m2 + self.m3
	
	def __str__(self):
		print(f"Name: {self.name} Total: {self.sum()}")

if __name__ == "__main__":
	s = Student("Harsh Mittal", 98,100, 50)
	print(s)
