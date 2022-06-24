# Tasks:
# 1.Prompt user for a pin code
# 2.If the pin code is correct then proceed to the next step, otherwise ask a user to type in a password again. 
# You can give a user a maximum of 3 attempts and then exit a program.
# 3.Set account balance to 100.
# 4.Now we need to simulate cash withdrawal
# 5.Accept the withdrawal amount
# 6.Subtract the amount from the account balance and display the remaining balance (NOTE! The balance cannot be negative!)
# 7.However, when a user asks to ‘withdraw’ more money than they have on their account, then you need to raise an error an exit the program. 



#withdraw money
def withdraw(with_amount, acc_balance):
    try:
        with_amount = float(with_amount)
        if (acc_balance < with_amount) or (with_amount < 0):
            raise Exception
        else:
            acc_balance -= with_amount
    except Exception:
        print('Failed withdrawal')
    finally:
        return acc_balance

#validate pin
def pin_valid(pin_input, pin_correct):
    return pin_input == pin_correct

def run(pin_correct, acc_balance):
    trial = 0
    while trial < 3: #three attempts for correct PIN
        pin_input = input('Input your PIN: ')
        if pin_valid(pin_input, pin_correct):
            print(f'Your balance is {acc_balance}')
            with_amount = input('Please enter withdrawal amount: ')
            acc_balance = withdraw(with_amount, acc_balance)
            print(f'Your balance is {acc_balance}')
            break
        else:
            print('Incorrect PIN, Please try again ')
            trial += 1

    if trial >= 3:
        print('Maximum number of attempts was reached! Good bye! ')

if __name__ == '__main__':
    run(pin_correct='0000', acc_balance=100)




