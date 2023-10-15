import art
import os


user_info = {}


def get_user_info():
    user_name = input("What is your name?: ")
    try:
        user_bid = int(input("What is your bid?: $"))
        if user_bid < 1:
            print("Must enter a bid greater than $0.")
        else:
            user_info[user_name] = int(user_bid)
    except ValueError:
        print("Invalid input. Please enter a number.")
        restart_program()
    

def duplicate_bids(bids):
    bid_count = {}
    for bid in bids.values():
        if bid in bid_count:
            bid_count[bid] += 1
        else:
            bid_count[bid] = 1

    for count in bid_count.values():
        if count > 1:
            return True
        else:
            return False


def highest_bid():
    starting_bid = 0
    winner = ''

    for key, value in user_info.items():
        if value > starting_bid:
            starting_bid = value
        if value == starting_bid:
            winner = key

    if not duplicate_bids(user_info):
        print(f"{winner.capitalize()} wins with a bid of ${value}!")
    else:
        print("There is a tie, restart the bid.")
        restart_program()


def restart_program():
    restart = input("Press enter to restart...")
    if restart == '':
        os.system('clear')
        main()
    else:
        exit()

def additional_bidders():
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

def main():
    print(art.logo)
    print("Welcome to the Secret Auction Program.")
    get_user_info()
    additional_bidders()
    highest_bid()
    restart_program()

main()
