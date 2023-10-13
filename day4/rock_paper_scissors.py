import random
# this goes beyond what day 4 implements using functions


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



rps = [rock, paper, scissors]

def choices():
    user_choice = int(input("Enter 0 for 'Rock', 1 for 'Paper', 2 for 'Scissors': "))
    computer_choice = random.randint(0, 2)
    return user_choice, computer_choice

def win(user_choice, computer_choice):
    symbols(user_choice, computer_choice)
    print("You Win!")

def lose(user_choice, computer_choice):
    symbols(user_choice, computer_choice)
    print("You Lose!")

def symbols(user_choice, computer_choice):
    print(f"You chose:\n{rps[user_choice]}")
    print(f"Computer chose:\n{rps[computer_choice]}")

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        symbols(user_choice, computer_choice)
        print("Its a draw!")
    elif user_choice == 0:
        if computer_choice == 1:
            lose(user_choice, computer_choice)
        else:
            win(user_choice, computer_choice)
    elif user_choice == 1:
        if computer_choice == 2:
            lose(user_choice, computer_choice)
        else:
            win(user_choice, computer_choice)
    elif user_choice == 2:
        if computer_choice == 0:
            lose(user_choice, computer_choice)
        else:
            win(user_choice, computer_choice)   

def play_game():
    while True:
        user_choice, computer_choice = choices()
        winner(user_choice, computer_choice)
        play_again = input("Would you like to play again? Y or N: ")
        if play_again.lower() != 'y':
            break

def main():
    print("Welcome to Rock, Paper, Scissors!")
    play_game()
    print("Thanks for playing!")
   
    
main()
    
