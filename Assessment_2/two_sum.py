
def is_valid_list(input_str):
    if input_str.startswith('[') and input_str.endswith(']'):
        list = input_str[1:-1].split(',')
        try:
            return [int(num) for num in list]
        except Exception:
            print('Error! Numbers list is not valid, please try again. ')
            return []

    else:
        print('Error! Numbers list is not valid, please try again. ')
        return []

def is_valid_int(target_sum):
    try:
        return int(target_sum)
    except Exception:
        print('Error! The target number is not integer, please try again. ')
        return 0


if __name__ == '__main__':
    numbers_list_input = input('Please input an array of numbers: ')
    target_sum = input('Please input target sum: ')

    target_sum_int = is_valid_int(target_sum)
    numbers_list = is_valid_list(numbers_list_input)
    numbers_seen_set = set() 

    if numbers_list and target_sum_int:
        for num1 in numbers_list:
            num2 = target_sum_int - num1
            if num2 in numbers_seen_set:
                print([num1, num2])
                break
            else:
                numbers_seen_set.add(num1)

    
