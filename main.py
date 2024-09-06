class Student:
	def __init__(self, name, m1, m2, m3):
		self.name = name
		self.m1 = m1
		self.m2 = m2
		self.m3 = m3
	def sum(self):
		return self.m1 + self.m2 + self.m3

if __name__ == "__main__":
	s = Student("Harsh Mittal", 98,100)
	print(s.name)
