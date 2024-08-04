print("Welcome to the simple ATM simulator")

user_password = 1234

balance = 15358

entered_password = int(input("Enter your password:"))

if entered_password != user_password:
    print("Invalid password")
    atm_on = False
else:
    atm_on = True

while atm_on == True:
    print("Main menu")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter the number of your choice:")
    if choice == "1":
        print(f"Your balance is {balance}$")
    elif choice == "2":
        c = int(input("Enter the amount of money you want to deposit:"))
        balance = balance + c
        print(f"Your current balance is {balance}$")
    elif choice == "3":
        w= int(input("Enter the amount of money you want to withdraw:"))
        if balance < w:
            print("Not enough balance to withdraw")
        elif balance >= w:
            balance = balance - w
            print(f"Done. Your current balance is {balance}")
    elif choice == "4":
        print("Thanks for dealing")
        atm_on = False
    else:
        print("Yor choice is not in the menu.Please try again")