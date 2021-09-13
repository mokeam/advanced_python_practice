from abc import ABCMeta, abstractstaticmethod, abstractmethod

class IDepartment(metaclass = ABCMeta):

	@abstractmethod
	def __init__(self, employees):
		""" Implement in child class """

	@abstractstaticmethod
	def print_department():
		""" Implement in child class """

class Accounting(IDepartment):

	def __init__(self, employees):
		self.employees = employees

	def print_department(self):
		print(f"Accounting Department: {self.employees}")

class Development(IDepartment):

	def __init__(self, employees):
		self.employees = employees

	def print_department(self):
		print(f"Development Department: {self.employees}")

class ParentDepartment(IDepartment):

	def __init__(self, employees):
		self.employees = employees
		self.base_employees = employees
		self.sub_departments = []

	def add(self, department):
		self.sub_departments.append(department)
		self.employees += department.employees

	def print_department(self):
		print("Parent Department")
		print(f"Parent Department Base Employees: {self.base_employees}")
		for dept in self.sub_departments:
			dept.print_department()
		print(f"Total number of employees: {self.employees}")


if __name__ == '__main__':
	dep1 = Accounting(200)
	dept2 = Development(170)

	parent_dept = ParentDepartment(30)
	parent_dept.add(dep1)
	parent_dept.add(dept2)
	parent_dept.print_department()