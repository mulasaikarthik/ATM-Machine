balance = 100000

def check_balance():
    print("Your Current Balance ₹", balance)

def deposite():
    global balance

    amount = int(input("Enter amount to deposite: "))

    if amount > 0:
        balance = balance + amount
        print("Deposite Succesfull!...")
        print("Updated balance: ₹", balance)
    
    else:
        print("Invalid Amount")

def withdraw():
    global balance 

    amount = int(input("Enter Your Withdraw Amount: "))

    if amount <= 0:
        print("Invaild amount")

    elif amount > balance:
        print("Insufficient Balanced")
    else:
        balance = balance - amount
        print("Withdraw Successfull")
        print("Remaining balance: ₹", balance)

print("\n===== WELCOME TO ATM ======")

while True:
    print()
    print("1. Check Balance")
    print("2. Deposite")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        check_balance()
    elif choice == "2":
        deposite()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        print("Thank You for Using The ATM!..")
        break
    
    else:
        print("Invaild!!, Please Enter The Choice From 1-4...")