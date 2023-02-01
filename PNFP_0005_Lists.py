names = ['Alice', 'Bob', 'Craig', 'Diana', 'Eric']

print(names[0]) # Alice
print(names[2]) # Craig
print(names[-1]) # Eric
print(names[-4]) # Bob


# Lists are mutable, so you can change the values in a list:

names[0] = 'Ann'
print(names)
# Outputs ['Ann', 'Bob', 'Craig', 'Diana', 'Eric']


# Append object to end of list
names = ['Alice', 'Bob', 'Craig', 'Diana', 'Eric']
names.append("Sia")
print(names)
# Outputs ['Alice', 'Bob', 'Craig', 'Diana', 'Eric', 'Sia']



# Add a new element to list at a specific index.
names.insert(1, "Nikki")
print(names)
# Outputs ['Alice', 'Nikki', 'Bob', 'Craig', 'Diana', 'Eric', 'Sia']


# Remove the occurrence

names.remove("Bob")
print(names) # Outputs ['Alice', 'Nikki', 'Craig', 'Diana', 'Eric', 'Sia']

print(names.index("Alice")) # 0
print(len(names)) # 6
print(names.pop()) # Outputs 'Sia'

count_occurance = [1, 1, 1, 2, 3, 4]
print(count_occurance.count(1)) # 3

# Reverse Count
print(count_occurance[::-1])
# out --> [4, 3, 2, 1, 1, 1]



# Iterate

for name in names:
  print ("#",name)
  

