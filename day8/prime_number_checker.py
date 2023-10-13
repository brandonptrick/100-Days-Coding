user_number = int(input("Enter a number between 1 and 100: "))

def prime_checker(number):
    isPrime = True
    if number in range(1, 101):
        for i in range(2, number):
            if number % i == 0:
                isPrime = False
    else:
        print("Enter a valid number")
    if isPrime:
        print("Prime")
    else:
        print("Not prime")

prime_checker(user_number)
