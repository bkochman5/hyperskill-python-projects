ticket = input("Input your 6 digits: ")

half1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
half2 = int(ticket[3]) + int(ticket[4]) + int(ticket[5])


if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")