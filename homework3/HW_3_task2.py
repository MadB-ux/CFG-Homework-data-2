# Task 2

# Question 1
# shopping_list = [
# 	"oranges",
# 	"cat food",
# 	"sponge cake",
# 	"long-grain rice",
# 	"cheese board",
# ]
# print(shopping_list[1])

# Question 2
# chocolates = {
# 	'white': 1.50,
# 	'milk': 1.20,
# 	'dark': 1.80,
# 	'vegan': 2.00,
# }

# choice = input('Please choose chocolate one type: white, milk, dark, vegan. ')
# try:
#     price = chocolates[choice]
#     print(f'The price of {choice} chocolate is ${price}')
# except Exception:
#     print('There is no such option. Please try again')

# # Question 3
# import random
# lottery_ticket = {23, 1, 43, 62, 9, 47, 96} #given lottery ticket

# #generating list of 7 unique random numbers
# rand_list = []
# i = 0
# while i < 7:
#     num = random.randint(1, 100)
#     if num not in rand_list:
#         rand_list.append(num)
#         i += 1

# #counting number of matches
# match_count = 0
# for num in rand_list:
#     if num in lottery_ticket:
#         match_count += 1

# #prize allocation
# prize = '£0'
# if match_count == 3:
#     prize = '£20'
# elif match_count == 4:
#     prize = '£40'
# elif match_count == 5:
#     prize = '£100'
# elif match_count == 6:
#     prize = '£10000'
# elif match_count == 7:
#     prize = '£1000000'

# print(f'You have {match_count} matches, your prize is {prize}! ')



