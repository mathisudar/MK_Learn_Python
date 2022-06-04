
#Source Code 


# Input

#Getting input in Python
#Getting String input Statement

name=input("Enter Name : ")
print(type(name))
print(name)

# Output
Enter Name : Tuttor
<class 'str'>
Tuttor





#Getting Integer input Statement

a=int(input("Enter The Value of A : "))
b=int(input("Enter The Value of B : "))
c=a+b
print(c)
print(type(a))

# Output

Enter The Value of A : 23
Enter The Value of B : 12
35
<class 'int'>





#Getting Float input Statement

a=float(input("Enter The Value of A : "))
b=float(input("Enter The Value of B : "))
c=a+b
print(c)
print(type(a))


# Output

Enter The Value of A : 34.45
Enter The Value of B : 23.76
58.21000000000001
<class 'float'>






# Multiple Values in Single Line
name1,name2,name3=input("Enter 3 Names : ").split()
print("Name 1 : ",name1)
print("Name 2 : ",name2)
print("Name 3 : ",name3)


# Output
Enter 3 Names : Ram kumar siva
Name 1 :  Ram
Name 2 :  kumar
Name 3 :  siva
  
  
  
  
  
  
# Multiple Values in Single Line  
name1,name2,name3=input("Enter 3 Names : ").split(',')
print("Name 1 : ",name1)
print("Name 2 : ",name2)
print("Name 3 : ",name3)

# Output

Enter 3 Names : Ram kumar,Sam kumar,siva kumar
Name 1 :  Ram kumar
Name 2 :  Sam kumar
Name 3 :  siva kumar
  
 



  
# Multiple Line String Input in Python
a="""
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
"""
print(type(a))
print(a)



# Output
<class 'str'>

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,







# Multiple Line String Input in Python

para=[]
print("Enter a Para : ")

while True:
  line=input()
  if line:
    para.append(line)
  else:
    break
print(para)
output='\n'.join(para)

print(output)



# Output

Enter a Para :
Ram is Good
HE is in Salem

['Ram is Good', 'HE is in Salem']
Ram is Good
HE is in Salem



