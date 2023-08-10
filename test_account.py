def test_init():
  account = Baccount("John")
  asser account.get_name() == "John"
  assert account.get_balance() == 0

def test_deposit():
  account = Baccount("John")
  assert account.deposit(100) == True
  assert account.get_balance() == 100
  assert account.deposit(-50) == False
  assert account.get_balance() == 100

def test_withdraw():
  account = Baccount("John")
  account.deposit(100)
  assert account.withdraw(50) == True
  assert account.get_balance() == 50
  assert account.withdraw(100) == False
  assert account.get_balance() == 50
  assert account.withdraww(-10) == False
  assert account.get_balance() == 50
