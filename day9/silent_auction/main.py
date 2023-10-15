import art
import os

user_info = {}

def get_user_info():
    user_name = input("What is your name?: ")
    user_bid = int(input("What is your bid?: $"))
    user_info[user_name] = user_bid
    
def highest_bid():
    starting_bid = 0
    winner = ''
    for key, value in user_info.items():
        if value > starting_bid:
            starting_bid = value
    for key, value in user_info.items():
        if value == starting_bid:
            winner = key
    print(f"{winner.capitalize()} wins with a bid of ${value}!")

def main():
    print(art.logo)
    print("Welcome to the Secret Auction Program.")
    get_user_info()
    while True:
        more_users = input("Are there any more bidders? Y or N? ").lower()
        if more_users == 'y':
            os.system('clear')
            get_user_info()
        elif more_users == 'n':
            os.system('clear')
            break
        else:
            print("Enter Y or N...")
    highest_bid()

main()
