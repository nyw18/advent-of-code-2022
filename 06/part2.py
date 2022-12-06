f = open("input.txt", "r")
input = f.readline()
input = input.strip()
output = 0

for i in range(len(input) - 14):
    input_subset = input[i:i + 14]
    duplicate = False
    for j in range(len(input_subset)):
        if input_subset.count(input_subset[j]) > 1:
            duplicate = True
            break
    if duplicate:
        continue
    output = i
    break
print(output + 14)
