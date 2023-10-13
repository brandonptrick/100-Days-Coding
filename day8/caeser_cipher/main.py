import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ''
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if cipher_direction == 'decrypt':
                new_position = (position - shift_amount) % 26
            else:
                new_position = (position + shift_amount) % 26
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"Here's the {cipher_direction}ed result: {end_text}")

def main():
    print(art.logo)
    print("Welcome to Caesar Cipher.")

    while True:
        reply = input("To continue enter Y. To exit enter N: ").lower()
        if reply =='y':
            direction = input("Would you like to encrypt or decrypt? ")
            if direction in ['encrypt', 'decrypt']:
                text = input(f"What would you like to {direction}? ")
                shift = int(input("How many letters would you like to shift by? "))
                caesar(start_text=text, cipher_direction=direction, shift_amount=shift)
            else:
                print("Enter either encrypt or decrypt...")
        else:
            break
    return direction


main()