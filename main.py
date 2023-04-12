from bank_account import BankAccount
import os


clear = os.system('cls')

is_on = True
print("Welcome to Jojo's Credit Union.")
while is_on:
    user = input("Please enter username: ")
    pw = input("Please enter password: ")
    info = BankAccount(username=user, password=pw)
    clear
    while info.cred_valid():
        command = int(input("1 = Check Balance \n2 = Withdraw \n3 = Deposit \n4 = Exit: "))
        if command == 4:
            is_on = False
            break
        else:
            info.view_balance(command)
            info.withdraw_balance(command)
            info.deposit_balance(command)

