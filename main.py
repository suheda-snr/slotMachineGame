import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol_to_check != symbol:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
             
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    # Generate the pool of symbols based on their counts
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)  # Append the column to columns

    return columns

def print_slot_machine(columns):
    # Transpose the columns to rows
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")  # Print without a newline
            else:
                print(column[row])  # Print the last column and a newline


def deposit():
    while True:
        amount = input("What would you like to deposit? €")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else: 
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid number.")
    return amount


def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on between 1-{MAX_LINES}: ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else: 
                print(f"Lines value must be between 1 and {MAX_LINES}.")
        else:
            print("Please enter a valid number.")
    return lines

def get_bet():
    while True:
        amount = input(f"What would you like to bet on each line? €")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else: 
                print(f"Amount must be between {MIN_BET} - {MAX_BET}.")
        else:
            print("Please enter a valid number.")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: €{balance}")
        else:
            break

    print(f"You're betting €{bet} on {lines} lines. Total bet is equal to €{total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    
    # Adjust balance and ensure it is never negative
    balance_change = winnings - total_bet
    new_balance = max(balance + balance_change, 0)
    
    if winnings > 0:
        print(f"You won €{winnings}")
        print(f"You won on lines: {winning_lines}")
    else:
        print("No winning lines this time.")

    return new_balance - balance  # Return only the net change


def main():
    balance = deposit()
    while balance > 0:
        print(f"Your current balance is: €{balance}")
        answer = input("Press Enter to play or 'q' to quit: ").strip().lower()
        if answer == 'q':
            break
        balance += spin(balance)

        if balance <= 0:
            print("You have run out of money!")
            replay = input("Would you like to deposit more funds? (yes/no): ").strip().lower()
            if replay == "yes":
                balance = deposit()
            else:
                print("Thank you for playing! Goodbye!")
                break

    if balance > 0:
        print(f"You are left with €{balance}. Thank you for playing!")
    else:
        print("Game over. You have no remaining balance.")


main()