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




