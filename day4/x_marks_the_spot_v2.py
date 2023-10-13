line1 = [" "," "," "]
line2 = [" "," "," "]
line3 = [" "," "," "]
map1 = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")
position = input("Where would you like to hide your treasure: ")

# example input: C3

letter = position[0].lower()
# letter = c

abc = ["a", "b", "c"]


letter_index = abc.index(letter)
# letter_index = abc.index(c)
# letter_index = 2

number_index = int(position[1]) - 1
# number_index = int(3) - 1
# number_index = 2

map1[number_index][letter_index] = "X"
# map1[2][2] = "X"

print(f"{line1}\n{line2}\n{line3}")
