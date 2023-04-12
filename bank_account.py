from data import bank_data


class BankAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.money = 0

    def cred_valid(self):
        """""Checks to see if credentials are correct, if not prompts user to try again"""
        for d in bank_data:

            if self.username == d['username'] and self.password == d['password']:
                return d

        print("Your username and/or password is incorrect. Please try again")

    def view_balance(self, command):
        """""Checks how much money is in account"""
        for d in bank_data:
            self.money = d['balance']
            if command == 1:
                if self.username == d['username']:
                    print(f'Your balance is ${self.money}')
        return self.money

    def withdraw_balance(self, command):
        """""Withdraws money from account. If withdraw is too big, reads insufficient funds"""
        for d in bank_data:
            self.money = d['balance']
            if command == 2:
                if self.username == d['username']:
                    print(f'Your current balance is ${self.money}')
                    withdraw = float(input("How much do you want to withdraw? $"))
                    if self.money > withdraw:
                        self.money -= withdraw
                        print(f'Your new balance is ${self.money}')
                    elif withdraw > self.money:
                        print('Insufficient funds. Please try again.')

    def deposit_balance(self, command):
        """""Deposits money into the account."""
        for d in bank_data:
            self.money = d['balance']
            if command == 3:
                if self.username == d['username']:
                    print(f'Your current balance is ${self.money}')
                    withdraw = float(input("How much do you want to deposit? $"))
                    self.money += withdraw
                    print(f"Your new balance is ${self.money}")
        return self.money
