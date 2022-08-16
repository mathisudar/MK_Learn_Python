
x = 1
y = 2.8
z = 1j

print(type(x)) # int
print(type(y)) # float
print(type(z)) # complex


x = 1
y = 35656222554887711
z = -3255522

print(type(x)) # int
print(type(y)) # int
print(type(z)) # int



x = 1.10
y = 1.0
z = -35.59

print(type(x)) # float
print(type(y)) # float
print(type(z)) # float



x = 35e3
y = 12E4
z = -87.7e100

print(type(x)) # float
print(type(y)) # float
print(type(z)) # float



x = 3+5j
y = 5j
z = -5j

print(type(x)) # complex
print(type(y)) # complex
print(type(z)) # complex



#convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(1)

print(x)
print(y)
print(z)

print(type(x)) # float
print(type(y)) # int
print(type(z)) # complex



import random

print(random.randrange(1, 10))



