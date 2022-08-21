# All string methods return new values. They do not change the original string.

txt = "hello, and welcome to my world."

x = txt.capitalize()

print (x) # Hello, and welcome to my world.



txt = "python is FUN!"

x = txt.capitalize()

print (x) # Python is fun!



txt = "Hello, And Welcome To My World!"

x = txt.casefold()

print(x) # hello, and welcome to my world!



txt = "banana"

x = txt.center(20)

print(x) #        banana



txt = "banana"

x = txt.center(20, "O")

print(x) # OOOOOOObananaOOOOOOO



txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x) # 2



txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple", 10, 24)

print(x) # 1


txt = "My name is Ståle"

x = txt.encode()

print(x) # b'My name is St\xc3\xe5le'


txt = "Hello, welcome to my world."

x = txt.endswith(".")

print(x) # True


txt = "Hello, welcome to my world."

x = txt.endswith("my world.")

print(x) # True


txt = "Hello, welcome to my world."

x = txt.endswith("my world.", 5, 11)

print(x) # False


txt = "H\te\tl\tl\to"

x =  txt.expandtabs(2)

print(x) # H e l l o


txt = "H\te\tl\tl\to"

print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))


/*

H       e       l       l       o
H       e       l       l       o
H e l l o
H   e   l   l   o
H         e         l         l         o

*/


txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x) # 7



txt = "Hello, welcome to my world."

x = txt.find("e")

print(x) # 1



txt = "Hello, welcome to my world."

x = txt.find("e", 5, 10)

print(x) # 8


txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49)) # For only 49.00 dollars!


#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("John",36)
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("John",36)

print(txt1)
print(txt2)
print(txt3)

/*

My name is John, I'm 36
My name is John, I'm 36
My name is John, I'm 36

*/


txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x) # 7


txt = "Hello, welcome to my world."

x = txt.index("e")

print(x) # 1


txt = "Hello, welcome to my world."

x = txt.index("e", 5, 10)

print(x) # 8



