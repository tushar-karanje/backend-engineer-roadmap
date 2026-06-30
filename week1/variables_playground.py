"""
a=[1,2,3,4,5]
b=a
c=[1,2,3,4,5]


print(a==b) # This should return true because both a and b have same contents
print(a is b) # This should return true because both a and b are pointing to same object in memory

print(a==c) # This should return true because both a and c have same contents
print(a is c) # This should return false because both a and c are pointing to different objects in memory and will have different id's

b.append(6)

print(a) # [1,2,3,4,5,6] 6 will be added to a as well because both a and b are pointing to same object in memory
print(c) # [1,2,3,4,5] this will remain same because c is having different id

name='Tushar'

print(type(name))
print(id(name))

name='Hruday'
print(type(name))
print(id(name))


age=36
print(type(age))
print(id(age))

age=42
print(type(age))
print(id(age))


skills=['Python','JavaScript','SQL','HTML','CSS']
print(type(skills))
print(id(skills))

skills.append(1999)
print(skills)
print(type(skills))
print(id(skills))

"""
"""
salary=4000000
print(type(salary))
print(id(salary))

salary=5000000
print(type(salary))
print(id(salary))


is_engineer=True
print(type(is_engineer))
print(id(is_engineer))

is_engineer=False
print(type(is_engineer))
print(id(is_engineer))

"""


"""

a = [1, 2, 3]

b = a

b = [7, 8, 9]

print(a)
print(b)

"""




a = [1, 2, 3]

b = a.copy()

b.append(4)

print(a)
print(b)

print(a == b)
print(a is b)