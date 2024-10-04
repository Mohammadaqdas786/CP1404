name = input("Name: ")
file = open("name.txt","w")
print(name, file=file)
file.close()

file = open("name.txt","r")
name = file.read().strip()
file.close()
print(f"Hello{name}")

with open("number.txt","r") as file:
    number_one = int(file.readline().strip())
    number_two = int(file.readline().strip())
result = number_one + number_two
print(result)

total = 0
with open("number.txt","r") as file:
    for line in file:
        total += int(line.strip())
print(total)