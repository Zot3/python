class Baccount:
  #creates class "Bank Account" with all functions inside of it

  #creates account
  def __init__ (self,name):
    self.accocunt_name = name
    self.account_balance = 0
  #adds deposit function, however, if the amount inputted is zero or less than zero it will not run the deposit
  def deposit(self,amount):
    if self.amount <=0:
      return False
    else:
       self.account_balance += amount
     return True
  #same idea as the deposit function with the added feature that if the amount inputted is more than the account balance, it will not run the withdrawal
  def withdraw(self,amount):
      if amount <= 0 or amount > self.account_balance:
        return False
      else:
          self.account_balance -= amount
        return True
  #simply returns balance of the account
  def getbalance(self):
      return self.account_balance
 #returns the name of the account    
  def get_name(self):
      return self.account_name
