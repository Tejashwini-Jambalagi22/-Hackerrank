'''Mini-project: ATM Simulator  Version 1
#Build a simple ATM program

#Your program should:

#Start with a balance of ₹5,000.
#Ask the user to enter a PIN.
#Check whether the PIN is correct.Allow balance checking.
#A llow money withdrawal if sufficient balance exists.    
'''

balance=5000
correct_pin="1234"

pin=input("Enter pin: ")

if pin == correct_pin:
    print("1. Check Balance")
    print("2. Withdraw Money")

    choice = int(input("enter choice: "))

    if choice ==1:
        print("balance:",balance)

    elif choice==2:
        amount=int(input("enter amount: "))

        if amount > 0 and amount <= balance:
            balance -= amount
            print("Withdrawal successful")
            print("Remaining:", balance)
        else:
            print("Invalid amount or insufficient balance")

    else:
        print("Invalid choice")

else:
    print("Incorrect PIN")
