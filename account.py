class Baccount:
  
  def __init__ (self,name):
    self.accocunt_name = name
    self.account_balance = 0
    
  def deposit(self,amount):
    if self.amount <=0:
      return False
    else:
       self.account_balance += amount
     return True
    
  def withdraw(self,amount):
      if amount <= 0 or amount > self.account_balance:
        return False
      else:
          self.account_balance -= amount
        return True
        
  def getbalance(self):
      return self.account_balance
    
  def get_name(self):
      return self.account_name
