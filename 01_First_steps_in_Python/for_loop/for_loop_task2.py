# You have a predefined string vowels that contains all letters designating vowel sounds.
# Write a program that counts the number of vowels in the variable string and prints this number.

string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'

counter = 0

for ch in string:
    if ch.lower() in vowels:
        counter = counter + 1
print(counter)