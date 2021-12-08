#!/usr/bin/env python
# coding: utf-8

# In[29]:


class User():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def Show_details(self):
        print(f"PERSONAL DETAILS")
        print("")
        print(f"NAME :- {self.name}")
        print(f"AGE :- {self.age}")
        print(f"GENDER:- {self.gender}")
class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance=0
    def Deposit(self,amount):#method overriding
        self.amount=amount
        self.balance=self.amount + self.balance#method overloading
        return(f"ACCOUNT BALANCE HAS BEEN UPDATED AFTER DEPOSIT :- ₹ {self.balance}")
    def Withdraw(self,amount):
        self.amount=amount
        if self.amount>self.balance:
            return(f"INSUFFICIENT BALANCE :- ₹ {self.balance}")
        else:
            self.balance=self.balance - self.amount
            return(f"ACCOUNT BALANCE HAS BEEN UPDATED AFTER WITHDRAW :- ₹ {self.balance}")
    def View_balance(self):
        self.Show_details()
        return(f"ACCOUNT BALANCE :- {self.balance}")
b=Bank("Ashutosh",24,"Male")
print(b.Show_details())
print(b.Deposit(1000))
print(b.Withdraw(100))
print(b.View_balance())
print(b.Withdraw(900))
print(b.View_balance())
print(b.Deposit(5000))
print(b.View_balance())


# In[ ]:




