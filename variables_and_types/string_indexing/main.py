grocery_item = "Grilled Chicken Salad"

# length using len()
length_of_item = len(grocery_item)

# first character of each word (positive indexes)
first_char  = grocery_item[0]   # 'G'
second_char = grocery_item[8]   # 'C'
third_char  = grocery_item[16]  # 'S'

# last character of each word (negative indexes)
last_char1 = grocery_item[-1]   # 'd' from "Salad"
last_char2 = grocery_item[-7]   # 'n' from "Chicken"
last_char3 = grocery_item[-15]  # 'd' from "Grilled"

# For manual verification
print(length_of_item)      # 22
print(first_char, second_char, third_char)  # G C S
print(last_char1, last_char2, last_char3)   # d n d