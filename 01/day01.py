elfCalorieData = []
elfCalories = 0

f = open("input.txt", "r")

for line in f:
    calories = line.strip()
    if calories:
        elfCalories += int(calories)
    else:
        elfCalorieData.append(elfCalories)
        elfCalories = 0

elfCalorieData.sort(reverse=True)
print(elfCalorieData[0])
print(elfCalorieData[0] + elfCalorieData[1] + elfCalorieData[2])
f.close()
