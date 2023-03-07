a = 5
b = 10

c = "Moje"
d = "imie"

print(a + a)  # Same as a+=a
print(b - a)  # Same as b-=a
print(a * b)
print(a ** a)
print(a / b)
print(a // b)
print(b % a)

# comment

"""
multi lane
comment
text
"""

# STRINGS

print("Moje imie")
print(f"{c} {d}")  # f-string
print(c, d)
print(c + " " + d)  # If you want to use it, you are not a programmer.

# SLICING OPERATOR
print("\n")

text = "text"
text2 = "12121212121212"

print(text[0])  # call for a symbol from index
print(text[1:4])
print(text[0:4])
print(text2[0:-1:2])
print(text2[1::2])

# IN BUILD FUNCTIONS
print("\n")

test_list = [1, 2, 3, 4, 5]
str_list = ["asadsa", "bdasdsad", "zdasdsada"]

maximum = max(str_list)
minimum = min(str_list)
rounded = round(1.4)
length = len(str_list)

print(f"Max = {maximum}, Min = {minimum}, {rounded}, {length}")
