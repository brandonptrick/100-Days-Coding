allHeights_str = input("Type all heights in inches sperated by a comma: ").split(",")

allHeights_int = []
totalHeight = 0
totalStudents = 0

for i in allHeights_str:
    allHeights_int.append(int(i))
    
for i in allHeights_int:
    totalHeight += i
    totalStudents += 1
    
avgHeight = round(totalHeight / totalStudents)

print(f"total height = {totalHeight}")
print(f"number of students = {totalStudents}")
print(f"average height = {avgHeight}") 
