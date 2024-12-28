MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

def deposit():
    #continually ask user the deposit amount until getting a valid amount
    while True:
        amount = input("What would you like to deposit? €")
        # if input is digit convert the default string to int
        if amount.isdigit():
            amount = int(amount)
            try:
                # check the value if greater than 0
                if amount > 0:
                    break
                else: 
                    print("Amount must be greater than 0.")
            except ValueError:
                print("Please enter a number.")
            continue
            
    return amount


def get_number_of_lines():
       #continually ask user the lines until getting a valid number
    while True:
        lines = input("Enter the number of lines to bet on between 1-"+ str(MAX_LINES)+ ". ")
        # if input is digit convert the default string to int
        if lines.isdigit():
            lines = int(lines)
            # check the value if between 1-3
            if 1 <= lines <= MAX_LINES:
                break
            else: 
                print("Lines value must be between 1-"+ str(MAX_LINES) + ".")
        else:
            print("Please enter a number.")
            
    return lines

def get_bet():
       #continually ask user the bet amount until getting a valid amount
    while True:
        amount = input("What would you like to bet on each line? €")
        # if input is digit convert the default string to int
        if amount.isdigit():
            amount = int(amount)
            try:
                # check the value if greater than 0
                if MIN_BET <= amount <= MAX_BET:
                    break
                else: 
                    print(f"Amount must be between {MIN_BET} - {MAX_BET}.")
            except ValueError:
                print("Please enter a number.")
            continue
            
    return amount
    


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: €{balance}")

        else:
            break

    print (f"You're betting €{bet} on {lines} lines. Total bet is equal to €{total_bet}")

main()