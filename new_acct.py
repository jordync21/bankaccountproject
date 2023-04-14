from data import bank_data

class NewAccount:

    def new_account1(self, new1):
        if new1 == "yes":
            new_usr = input("Choose a username: ")
            new_pw = input('Choose a new password: ')
            new_bal = int(input('How much money are you deposit?: '))
            new_data = {
                "username": f'{new_usr}',
                "password": f'{new_pw}',
                "balance": f'{new_bal}'

            }
            bank_data.append(new_data)
            print("A new account was made. Please login.")
