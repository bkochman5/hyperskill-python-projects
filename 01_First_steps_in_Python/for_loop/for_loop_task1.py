a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

total = 0
count = 0

for i in range(a, b + 1):
    if i % 3 == 0:
        total += i
        count += 1

mean = total / count

print(f"The average of numbers divisible by 3 in range [{a}, {b}] is: {mean:.2f}")
