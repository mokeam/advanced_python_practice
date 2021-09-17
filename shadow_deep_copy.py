import copy

org = 5
cpy = org
cpy = 6
print(cpy)
print(org)

org = [0, 1, 2, 3, 4]
cpy = org
cpy[0] = -10
print(cpy)
print(org)

org = [0, 1, 2, 3, 4]
cpy = copy.copy(org)
cpy[0] = -10
print(cpy)
print(org)

org = [[0, 1, 2, 3, 4],[5, 6, 7, 8, 9]]
cpy = copy.copy(org)
cpy[0][1] = -10
print(cpy)
print(org)

org = [[0, 1, 2, 3, 4],[5, 6, 7, 8, 9]]
cpy = copy.deepcopy(org)
cpy[0][1] = -10
print(cpy)
print(org)

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

class Company:
	def __init__(self, boss, employee):
		self.boss = boss
		self.employee = employee

p1 = Person('Mariam',25)
p2 = Person('Olajumoke', 30)

# c1 = Company(p1,p2)
# c_clone = copy.copy(c1)
# c_clone.boss.age = 56
# print(c_clone.boss.age)
# print(c1.boss.age)

c1 = Company(p1,p2)
c_clone = copy.deepcopy(c1)
c_clone.boss.age = 56
print(c_clone.boss.age)
print(c1.boss.age)




















