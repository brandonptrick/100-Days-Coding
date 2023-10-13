line1 = [" "," "," "]
line2 = [" "," "," "]
line3 = [" "," "," "]
map1 = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")
position = str(input("Where would you like to hide your treasure: "))

if position.lower() == "a1":
    line1[0] = "X"
elif position.lower() == "a2":
    line1[1] = "X"
elif position.lower() == "a3":
    line1[2] = "X"
elif position.lower() == "b1":
    line2[0] = "X"
elif position.lower() == "b2":
    line2[1] = "X"
elif position.lower() == "b3":
    line2[2] = "X"
elif position.lower() == "c1":
    line3[0] = "X"
elif position.lower() == "c2":
    line3[1] = "X"
elif position.lower() == "c3":
    line3[2] = "X"
else:
    print("Please enter a valid input")

print(f"{line1}\n{line2}\n{line3}")
