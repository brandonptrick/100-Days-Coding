number = int(input("Enter a number between 1 and 100: "))

even_sum = 0

if 0 < number <= 100:   
    for n in range(0, number + 1, 2):
        even_sum += n
    print(even_sum)
else:
    print("Must enter a valid number...")

