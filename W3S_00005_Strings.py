#You can use double or single quotes:

print("Hello")
print('Hello')


a = "Hello"
print(a)


# You can assign a multiline string to a variable by using three quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(a)


a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

print(a)


a = "Hello, World!"
print(a[1]) # e


# Loop through the letters in the word "banana":
for x in "banana":
  print(x) 
  
# The len() function returns the length of a string:  
  
a = "Hello, World!"
print(len(a)) # 13 


# Check if "free" is present in the following text:

txt = "The best things in life are free!"
print("free" in txt) # True



txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
  

txt = "The best things in life are free!"
print("expensive" not in txt)  # True


txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


# Slicing

b = "Hello, World!"
print(b[2:5]) # llo


b = "Hello, World!"
print(b[:5]) # Hello


b = "Hello, World!"
print(b[2:]) # llo, World!


b = "Hello, World!"
print(b[-5:-2]) # orl


# The upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper()) # HELLO, WORLD!



# The lower() method returns the string in lower case:

a = "Hello, World!"
print(a.lower())  # hello, world!


# The strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! "
print(a.strip()) # Hello, World!



# The replace() method replaces a string with another string:

a = "Hello, World!"
print(a.replace("H", "J")) # Jello, World!


# The split() method splits the string into substrings if it finds instances of the separator:

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

a = "Hello, World!"
b = a.split(",")
print(b) # ['Hello', ' World!']



# String Concatenation

a = "Hello"
b = "World"
c = a + b
print(c) # HelloWorld


a = "Hello"
b = "World"
c = a + " " + b
print(c) # Hello World


# Use the format() method to insert numbers into strings:

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age)) # My name is John, and I am 36


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price)) # I want 3 pieces of item 567 for 49.95 dollars.


quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) # I want to pay 49.95 dollars for 3 pieces of item 567


# Escape Character

txt = "We are the so-called \"Vikings\" from the north."
print(txt)  # We are the so-called "Vikings" from the north.
