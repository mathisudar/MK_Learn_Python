class BankAcc():
    def __init__(self,AccName,AccNum,AccBalance):
        self.AccName = AccName
        self.AccNum = AccNum
        self.AccBalance = AccBalance
    
    def creditMoney(self,amountDeposit):
        self.AccBalance = self.AccBalance+amountDeposit
        print("\n")
        print("Deposit:")
        print(amountDeposit," deposited successfully!")
        print('Final balance: ',self.AccBalance)
        
    def debitMoney(self,amountWithdrawn):
        self.AccBalance = self.AccBalance-amountWithdrawn
        if amountWithdrawn>self.AccBalance:
            print("\n")
            print("Alert:")
            print("Insufficient Amount")
        else:
            print("\n")
            print("Withdrawn:")
            print(amountWithdrawn," withdrawn successfully.")
            print('Final Balance: ',self.AccBalance)
            
objectAccHolder1 = BankAcc('Mathi', 1234, 10000)

print("Account Details:")
print(objectAccHolder1.AccName,objectAccHolder1.AccNum,objectAccHolder1.AccBalance)


objectAccHolder1.creditMoney(1000)
objectAccHolder1.debitMoney(200)
            
 

*** Result ****

Account Details:
Mathi 1234 10000


Deposit:
1000  deposited successfully!
Final balance:  11000


Withdrawn:
200  withdrawn successfully.
Final Balance:  10800
  
*** Result****  
  
