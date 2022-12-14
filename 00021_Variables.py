

print("# String ")
xName1 = "John"
# is the same as
yName2 = 'John'
print(xName1)
print(yName2)
print()


print("# Case sensitive")
a = 4
A = "Sally"
#A will not overwrite a

print(a)
print(A)
print()


print("# Multi Variables in single line")
x1, y1, z1 = "Orange", "Banana", "Cherry"
print(x1)
print(y1)
print(z1)
print()


print("# One value to Multi Variables in single line")
x2 = y2 = z2 = "Orange"
print(x2)
print(y2)
print(z2)
print()



print("# Unpack List")

fruits = ["apple", "banana", "cherry"]
x3, y3, z3 = fruits
print(x3)
print(y3)
print(z3)
print()



print("# String")

x4 = "Python is awesome"
print(x4)
print()


print("# String Concatenate")
x5 = "Python"
y5 = "is"
z5 = "awesome"
print(x5, y5, z5)
print()


print("# String Concatenate")
x6 = "Python "
y6 = "is "
z6 = "awesome"
print(x6 + y6 + z6)
print()


print("# int + operator")
x7 = 5
y7 = 10
print(x7 + y7)
print()


print("# Concatenate ")
x = 5
y = "John"
print(x, y)
print()



print("# Global Variables ")

x8 = "awesome"

def myfunc():
  print("Python is " + x8)
  print()

myfunc()



print("# Global and Local Variables")

x9 = "awesome"

def myfunc():
  x9 = "fantastic"
  print("Python is " + x9)


myfunc()
print("Python is " + x9)
print()



print("# Global Variable")
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
print()



print("# Change the Global Variable value")
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)





