# Task 1 (Conditional flow)

# Question 1 
# rain = input("Is it raining today? Please enter 'y' for yes 'n' for no. ")
# if rain in ('y','Y'):
#     print('Take an umbrella')
# elif rain in ('n', 'N'):
#     print("You don't need an umbrella")
# else:
#     print("Invaid input. Good bye!")

# Question 2
# my_money = int(input('How much money do you have? '))
# boat_cost = 20 + 5

# if my_money >= boat_cost:
# 	print('You can afford the boat hire')
# else :
# 	print('You cannot afford the board hire')

# #Question 3
# year = input("Please enter a year: ")

# #century check
# def century_check(year):
#     if year[:2] == '18':
#         century = 'Nineteenth'
#     else:
#         century = 'Twentieth'
#     return century

# #decade check
# def decade_check(year):
#     if year[2] == '1':
#         decade = 'Tens'
#     elif year[2] == '2':
#         decade = 'Twenties'
#     elif year[2] == '3':
#         decade = 'Thirties'
#     elif year[2] == '4':
#         decade = 'Fourties'
#     elif year[2] == '5':
#         decade = 'Fifties'
#     elif year[2] == '6':
#         decade = 'Sixties'
#     elif year[2] == '7':
#         decade = 'Seventies'
#     elif year[2] == '8':
#         decade = 'Eighties'
#     elif year[2] == '9':
#         decade = 'Nineties'
#     else:
#         decade = 'Aughts'
#     return decade

# # range check
# def year_range_is_valid(year, year_min, year_max):
#     return year_min <= int(year) <= year_max

# # main program
# try:
#     if year_range_is_valid(year, 1800, 1950):
#         century = century_check(year)
#         decade = decade_check(year)
#         print(f'{century} Century, {decade}')
#     else:
#         raise ValueError
# except Exception:
#     print("Please enter valid year in range 1800-1950")

