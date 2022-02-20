def show_balance(balance):
    print("Current balance: $" + str(balance))
def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    return float(balance) + amount
def withdraw(balance):
    while True:
        amount2 = float(input("Enter amount to withdrawl: "))
        if amount2 > balance:
            print("Your balance is too low, please try again")
            continue
        if amount2 <= balance:
            break
    return float(balance) - amount2
def logout(name):
    print("Goodbye! " + name)