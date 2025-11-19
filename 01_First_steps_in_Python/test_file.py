def find_max(numbers):
    current_max = numbers[0]

    for num in numbers:
        if num > current_max:
            current_max = num
    return current_max



print(find_max([1, 2, 10, 99, 1, 20]))