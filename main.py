from bank_account import BankAccount
from new_acct import NewAccount


is_on = True
print("Welcome to Jojo's Credit Union.")


while is_on:
    new_acct = input('Would you like to create a new acct (type yes or no): ')
    new = NewAccount()
    new.new_account1(new_acct)
    if new_acct == 'no':
        user = input("Please enter username: ")
        pw = input("Please enter password: ")
        info = BankAccount(username=user, password=pw)
        while info.cred_valid():
            print("MAIN MENU")
            command = int(input("1 = Check Balance \n2 = Withdraw \n3 = Deposit \n4 = Exit: "))
            if command == 4:
                is_on = False
                break
            else:
                info.view_balance(command)
                info.withdraw_balance(command)
                info.deposit_balance(command)
