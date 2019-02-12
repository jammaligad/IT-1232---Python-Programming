class bankAccount:
    def __init__(self, accNumber, balance, dateOpened):
        self.accNumber = accNumber
        self.balance = balance
        self.dateOpened = dateOpened
        
    def deposit(self, dep):
        self.balance += dep
        print(self.balance)
        
    def withdraw(self, wd):
        self.balance -= wd
        print(self.balance)
        
    def drop(self, acc):
        self.accNumber = self.balance = self.dateOpened = None
        print("Account details deleted") if self.accNumber is None else print("Invalid!")
        
acc = bankAccount(1, 1515, "10/27/1987")
x = input().split()
if(x[0] == "dep"):
    acc.deposit(int(x[2]))
elif(x[0] == "wd"):
    acc.withdraw(int(x[2]))
elif(x[0] == "drop" and x[2] == "o"):
    acc.drop(x[1])
else:
    print("Invalid Transaction!")