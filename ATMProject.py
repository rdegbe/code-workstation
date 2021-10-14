import sys, os, time, re
from datetime import datetime



# ATM Class

class ATM():

    def __init__(self, username, avail_amount):
        self.username = username
        self.avail_amount = avail_amount

    def check_balance(self):
        print("Your Account balance is GH {} cedis ".format(self.avail_amount))

    def print_receipt(self, transaction_type, amount, balance):

        active = True
        while active:
            ask = (input(
                "Do you want a receipt printed for this transaction? Y/N: ")).upper()
            if ask == "Y":
                print("Receipt printed for {} of {}. \n Your available balance is {}.".format(
                    transaction_type, amount, balance))
                active = False
            elif ask == "N":
                print("Receipt not printed ")
                active = False
            else:
                print("Please try again")

    def withdraw(self, withdrawal_amount):

        if (self.avail_amount <= withdrawal_amount):
            print("Insufficient funds..")
        else:
            self.avail_amount = self.avail_amount - withdrawal_amount
            # print("Your Account balance is GH {} gh cedis ".format(self.avail_amount))
            print("Your updated Account balance is GH {} cedis ".format(self.avail_amount))
            now = datetime.now()
            current_time = "%s:%s %s / %s / %s" % (
                now.hour, now.minute, now.month, now.day, now.year)
            history_file = open(self.username + 'history.txt', 'a')
            history_file.write(current_time + '\n')
            history_file.write(str(withdrawal_amount) + '\n')
            history_file.close()

        self.print_receipt(transaction_type="withdrawal",
                           amount=withdrawal_amount, balance=self.avail_amount)

    def deposit(self, deposited_amount):
        self.avail_amount = self.avail_amount + deposited_amount
        print("You have deposited GH {} cedis in your Account.\nYour updated Account balance is {} ".format(
            deposited_amount, self.avail_amount))
        self.print_receipt(transaction_type="deposit",
                           amount=deposited_amount, balance=self.avail_amount)

    def print_transaction(self):
        transactions = open(self.username + 'history.txt', 'r')
        allTransactions = transactions.readlines()
        transactions.close()
        if len(allTransactions) == 0:
            print("No transactions yet")
        else:
            print("Transactions:")
        for tran in range(len(allTransactions)):
            sys.stdout.write(allTransactions[tran])

    def pin_change(self, user_pin):
        i = 2
        while (i > 0):
            p = int(input('Enter Original PIN: '))
            if p == user_pin:
                x = input('Enter New PIN: ')
                user_pin = x
                break
            else:
                i = i - 1
                print('PIN incorrect, {} tries left'.format(i))
        if i == 0:
            del self.username
            print('Account Blocked!')


# Main Function


users = {"Ralph": [1234, 5000], "Nana Kwame": [4567, 2000], "Gifty": [9000, 10000], "Mawunyo": [2020, 1500],
         "Wadi": [2021, 4500], "Razak": [2022, 6000], "Raymond": [2023, 7000]}


app_state = True
active1 = True
k = users.keys()




while app_state:

    name = "* * * * * W E L C O M E   T O   T A G   B A N K   G H A N A * * * * *\n"
    for char in name:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.04)

    uname = str(input('Enter Name: '))
    user1 = ATM(uname, users[uname][1])
    if uname in k:
        i = 3
        while (i > 0):
            pin = int(input('Enter PIN: '))
            if pin == users[uname][0]:
                print("Access granted.....")

                while app_state:
                    # print("\n")

                    name = "* * * * * T A G   B A N K   G H A N A * * * * *\n"
                    for char in name:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(.05)

                    print(""" 
1. Check balance
2. Withdraw Cash
3. Deposit Money
4. View History
5. Change Pin
6. Quit""")
                    print("\n")
                    choice = int(input("Please enter the number of your choice: "))
                    if choice == 1:
                        user1.check_balance()
                    elif choice == 2:
                        withdrawl = float(input("Please enter amount to withdraw: "))
                        user1.withdraw(withdrawl)
                    elif choice == 3:
                        amt_to_deposit = float(input("Please enter amount to deposit: "))
                        user1.deposit(amt_to_deposit)

                    elif choice == 4:
                        user1.print_transaction()

                    elif choice == 5:
                        user1.pin_change(users[uname][0])
                        

                    elif choice == 6:
                        print(" Thank you for banking with us!!!")
                        app_state = False
                    else:
                        print("Invalid number choice .\t Select the correct number")
                break

            else:
                i = i - 1
                print('Incorrect PIN, {} tries left'.format(i))
        if i == 0:
            del users[uname]
            print('Account Blocked!')
        break
