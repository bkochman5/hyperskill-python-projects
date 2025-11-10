# A test has five possible grades: A, B, C, D, and F. The grade ranges are as follows:
#
#     A: 90-100%
#
#     B: 80-90%
#
#     C: 70-80%
#
#     D: 60-70%
#
#     F: Below 60%
#
# Your task is to determine a student's grade based on their score and the maximum possible score.
#
# Note: The lower bound of each range is inclusive, while the upper bound is exclusive, except for grade A which includes 100%.




user_score = int(input())
max_possible_score = int(input())

percentage = (user_score / max_possible_score) * 100

if 90 <= percentage <= 100:
    print("A")
elif 80 <= percentage < 90:
    print("B")
elif 70 <= percentage < 80:
    print("C")
elif 60 <= percentage < 70:
    print("D")
else:
    print("F")