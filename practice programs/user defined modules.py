data  = {
    '1234':{'Balance':4567,'pin':345,'History':[]}
    '1236':{'Balance':4597,'pin':346,'History':[]}
    '1238':{'Balance':4577,'pin':355,'History':[]}
    '1279':{'Balance':4799,'pin':349,'History':[]}

}

acc_num=None
login_status=False

def Welcome():
     print('Welcome to the ATM'.center(40,'-'))


def menu():
print('1.Check Balance')
print('2.Deposit')
print('3.withdraw')
print('4.View Transaction')
print('0.Exit')

def logic(acc,pin):
    if acc in data:
       if data[acc]['pin']==pin:
          global acc_num
          global
         acc_num = acc
         login_status = True
         print("Login Successful")
       else:
         print("Invalid Pin")
    else:
         print("Invalid Account Number")

def check_balance():
      if login_status and acc_num:
         print(f"Current Balance: {data[acc_num]['balance']}")
      else:
         print("Login Again")

def deposit():
     if login_status and acc_num:
          amount=int(input("Enter the amount to withdraw:"))
          if amount <= data[acc_num]['balance']
             data[acc_nu