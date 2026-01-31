'''4. ATM Simulation System
Scenario: Simulate a simple ATM.

Task:

Start with a balance

Let user choose: deposit, withdraw, check balance

Prevent withdrawal if balance is too low

Keep transaction history in a list'''

balance=100000
transaction_history=[]
while True:
    print("choose an option:")
    print("1. deposit")
    print("2. withdraw")
    print("3. check balance")
    print("4. exit")
    choice=input("enter your choice (1-4):")
    if choice=='1':
        amount=float(input("enter amount to deposit:"))
        balance+=amount
        transaction_history.append(f"deposited: {amount}")
        print(f"you have deposited {amount}. new balance is {balance}")
    elif choice=='2':
        amount=float(input("enter amount to withdraw:"))
        if amount>balance:
            print("insufficient balance")
        else:
            balance-=amount
            transaction_history.append(f"withdrew: {amount}")
            print(f"you have withdrawn {amount}. new balance is {balance}")
    elif choice=='3':
        print(f"current balance is {balance}")
    elif choice=='4':
        print("exiting...")
        break
    else:
        print("invalid choice, please try again")