def show_homepage():
    print("")
    print("        === DonateMe Homepage ===         ")
    print("------------------------------------------")
    print("| 1.    Login     | 2.     Register      |")
    print("------------------------------------------")
    print("| 3.    Donate    | 4.   Show Donations  |")
    print("------------------------------------------")
    print("|             5.   Exit                  |")
    print("------------------------------------------")
total_donations = 0

def donate(username):
    global total_donations
    while True:
        donation_amt = input("Enter amount to donate: ")
        if donation_amt.isnumeric():
            donation_amt = float(donation_amt)
            donation = username + " has donated $" + str(donation_amt)
            print("Thank you for your donation!")
            total_donations += donation_amt
            return donation
        else:
            print("Please enter a valid number to donate.")
def show_donations(donations):
    global total_donations
    if len(donations) == 0:
        print("Currently, there are no donations.")
    else:
        print("\n---All Donations ---")
        for x in donations:
            print(x)
        print("Total = $",total_donations)