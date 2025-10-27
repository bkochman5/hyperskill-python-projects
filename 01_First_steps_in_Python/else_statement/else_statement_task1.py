A = int(input("Minimum time sleep: "))
B = int(input("Max time sleep: "))
H = int(input("Ann sleep in hours: "))


if H < A:
    print("Deficiency")
elif H > B:
    print("Excess")
else:
    print("Normal")