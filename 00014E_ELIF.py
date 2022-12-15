# elif Statement in Python


"""
0       No Fine
1-5     0.5
5-10    1
10-30   5
>30     Membership Cancel
"""


days = int(input("Enter The Days : "))
if days == 0:
    print("Good No Fine")
elif days >= 1 and days <= 5:
    print("Fine Amount : ", days * 0.5)
elif days > 5 and days <= 10:
    print("Fine Amount : ", days * 1)
elif days > 10 and days <= 30:
    print("Fine Amount : ", days * 5)
else:
    print("Membership Cancel")
    
    

    
# Output

Enter The Days : 5
Fine Amount :  2.5
