from bank_account import BankAccount



is_on = True

while is_on:
    print("Welcome to Jojo's Credit Union.")
    user = input("Please enter username: ")
    pw = input("Please enter password: ")
    info = BankAccount(username=user, password=pw)
    while info.cred_valid():
        command = int(input("1 = Check Balance \n2 = Withdraw \n3 = Deposit: "))
        info.view_balance(command)
        info.withdraw_balance(command)
        info.deposit_balance(command)
        if command == 'exit':
            is_on = False
