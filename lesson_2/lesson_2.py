# Operators < > == <= >= != and or not
# Boolean -> True, False
# Logic -> If, elif, else

"""
IN-BUILT FUNCTIONS
    input()
    int()
    str()
    float()
    bool()
    print()
    type()
"""

# if 2 == 1:
#     print(True)
# elif 3 == 2:
#     print(True, 2)
# else:
#     print("Else")

# if 2 > 1:
#     ...
# elif 1 < 2:
#     ...
# elif 1 <= 1:
#     ...
# elif 1 >= 1:
#     ...
# elif 1 == 1:
#     ...
# elif 1 != 2:
#     ...

# age = int(input("Input your age: "))
#
# if age >= 18:
#     print("You are adult!")
# else:
#     print("You are a teenager.")

# 250 > 42.01  # True
# 490 <= 450  # False
# 24 == 12  # False
# 40 != 23  # True
# 40 > 40  # False
# 99 < 98.4  # False
#
# print(12 == 15)  # False -> ==, <, !=, <
# print(5 < 10000)  # True -> ==, >, <, <=
# print(120 < 120)  # False -> ==, <, !=, >=
# print(60 == 150)  # False -> ==, <, !=, >=
# print(25.3421 == 25.3421)  # True -> ==, !=, <=, >=

# height = "150 cm"
#
# height < "115 cm"   # False
# height < "149 cm"   # False
# height <= "150 cm"  # True
# height <= "151 cm"  # False
# height < "210 cm"   # True


# height = int(input("Input your height: "))
#
# if height > 150:
#     print("Yes, you can use it!")

# not True  # False
# not False  # True
#
# not 50 == 50.001  # True
# not 2 > 10  # True
# not (not 4 > 10)   # False
# not 1 == 1  # False

# True and True   # True
# True and False  # False
# False and True  # False
# False and False  # False
#
# 1 == 1 and 2 == 2   # True
# 1 == 1 and 2 != 2   # False
# 1 != 1 and 2 == 2   # False
# 1 != 1 and 2 != 2   # False

# 20 < 25 and 24 == 0  # False
# 24 == 0 and 20 < 25  # False
# 4 != 4.0 and 2 <= 0  # False
# 2 < 5 and 50 != 50.001  # True

# True or True    # True
# True or False   # True
# False or True   # True
# False or False  # False

# 20 < 25 or 24 == 0  # True
# 4 != 4.0 or 2 <= 0  # True
# 2 < 5 or 50 != 50.001  # True

# height = int(input("Input your height (in cm): "))
#
# if 150 < height < 215:
#     print("Yes, you can!")

# print(True, 25 < 140 and 10 == 10)
# print(True, 100 >= 1 or 2 > 10)
# print(False, 25 < 14 and 10 != 10)
# print(False, -1 < 3 and not 2 < 9 or 10 == 15)
# print(True, 20.05 < 21 < 10 or -10 < 20 < 150 <= 150)
# print(False, 1 < 10 and 2 < 15 and -50 == 42)
# print(True, not 2 == 10)

# a = int(input("Input a number: "))
# b = int(input("Input a number: "))
# c = int(input("Input a number: "))
#
# did_a_is_max = a > b and a > c
# did_b_is_max = b > a and b > c
# did_c_is_max = not(did_a_is_max or did_b_is_max)
#
# print(did_a_is_max)
# print(did_b_is_max)
# print(did_c_is_max)
