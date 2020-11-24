import math
class Student(people):
		def __init__(self,name,ID,gpa):
			self.name=name
			self.ID=ID
			self.gpa=gpa
			try:
				Student.gpa_total.append(self.gpa)
			except AttributeError:
				Student.gpa_total=[self.gpa]
def mean_gpa():
	return sum(Student.gpa_total)/float (len(Student.gpa_total))

def info_gpa(self):
	mean= self.mean_gpa()
	return mean
def __str__(self):
	return self.info_gpa()

class Employee(people):
	def __init__(self,name,ID,salary):
		people._init_(self,name,ID)
		self.name=name
		self.ID-ID
		self.salary=salary
		self.Employee=Employee
		Employee.emp_total.append(self.Employee)

def total_salary():
	return sum(Employee.emp_total)
