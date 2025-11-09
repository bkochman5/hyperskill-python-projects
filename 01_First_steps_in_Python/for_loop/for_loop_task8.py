# In a computer game, each gamer has an army of units.
#
# Write a program that will classify the army of your enemies corresponding to the following rules:
#
# Units: Category
#
# less than 1: no army
#
# from 1 to 9: few
#
# from 10 to 49: pack
#
# from 50 to 499: horde
#
# from 500 to 999: swarm
#
# 1000 and more: legion
#
# The program should read the number of units and output the corresponding category.



no_of_units = int(input())

if no_of_units < 1:
    print("no army")
elif 1 <= no_of_units <= 9:
    print("few")
elif 10 <= no_of_units <= 49:
    print("pack")
elif 50 <= no_of_units <= 499:
    print("horde")
elif 500 <= no_of_units <= 999:
    print("swarm")
else:
    print("legion")