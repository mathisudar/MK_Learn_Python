# String And String Function

s = "tutor Joes"
print(s)
print(type(s))
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.count("t"))
print(s.endswith("ED"))
print(s.find("o"))
print(s.find("o", 5))
print(s.replace("o", '0'))

# Output

tutor Joes

TUTOR JOES
tutor joes
Tutor joes
Tutor Joes
2
False
3
7
tut0r J0es






# String And String Function

a = "joes1234"
print("Is Upper : ", a.isupper())
print("Is Lower : ", a.islower())
print("Is Alpha Numeric : ", a.isalnum())
print("Is Alpha : ", a.isalpha())


# Output

Is Upper :  False
Is Lower :  True
Is Alpha Numeric :  True
Is Alpha :  False
  
  
  
  

 # String And String Function 

s = "he\nis\ngood"
print(s)
print(s.splitlines())
print(s.splitlines(True))


# Output

he
is
good
['he', 'is', 'good']
['he\n', 'is\n', 'good']




 # String And String Function 

a = "Tutor Joes Computer Education"
print(a.split(" "))

# Output

['Tutor', 'Joes', 'Computer', 'Education']





 # String And String Function 

a = "Tutor,Joes,Computer,Education"
print(a.split(","))


# Output

['Tutor', 'Joes', 'Computer', 'Education']





 # String And String Function 

s="    Joes     "
print(len(s))
print(len(s.strip()))
print(len(s.lstrip()))
print(len(s.rstrip()))

# Output

13
4
9
8




 # String And String Function 

s='12-03-2020'
print(s.partition('-'))

# Output

('12', '-', '03-2020')







