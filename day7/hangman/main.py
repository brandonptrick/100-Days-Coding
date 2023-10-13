import random, hangman_art, hangman_words

print(f"{hangman_art.logo}\nWelcome to Hangman!")
chosen_word = random.choice(hangman_words.word_list)

display = ["_" for _ in chosen_word]

print(' '.join(display))

lives = 6
guessed_letters = []

while '_' in display:
    guess = input("Guess a letter: ").lower()  
  
    if guess in chosen_word and guess not in guessed_letters:
        for p in range(len(chosen_word)):
            letter = chosen_word[p]
            if letter == guess:
                display[p] = letter
        print(f"{' '.join(display)}")
    elif guess not in guessed_letters:
        print(f"'{guess}' is not in the word!")
        lives -= 1
        print(hangman_art.stages[lives])
        print(f"{' '.join(display)}")
        if lives == 0:
            print(f"{chosen_word}")
            print("You loose!")
            break
    else:
        print(f"You've already guessed '{guess}'.")

    guessed_letters.append(guess)

    if '_' not in display:
        print(f"{''.join(display)}")
        print("You win!")