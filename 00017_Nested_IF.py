# Nested If Statement in Python


"""
3 Marks as Input
Total
Average
Result
If Pass Grade
    90-100 A
    80-89 B
    70-79 C
    Else D
"""



m1 = int(input("Enter Mark-1  : "))
m2 = int(input("Enter Mark-2  : "))
m3 = int(input("Enter Mark-3  : "))

total = m1 + m2 + m3
average = total / 3.0

print("Total  : ", total)
print("Average  : ", average)

if m1 >= 35 and m2 >= 35 and m3 >= 35:
    print("Result  : Pass")
    if average >= 90 and average <= 100:
        print("Grade : A")
    elif average >= 80 and average <= 89:
        print("Grade : B")
    elif average >= 70 and average <= 79:
        print("Grade : C")
    else:
        print("Grade : D")
else:
    print("Result  : Fail")
    print("Grade   : No Grade")
    
    

    
# Output
Enter Mark-1  : 90
Enter Mark-2  : 90
Enter Mark-3  : 90
Total  :  270
Average  :  90.0
Result  : Pass
Grade : A
  
  
