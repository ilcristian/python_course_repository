# 1

def integer_sum(*args, **kwargs):
    number_sum = 0
    for integer_number in args:
        if isinstance(integer_number, int):
            number_sum += integer_number
    return number_sum


sum_of_integers = integer_sum(1, 5, -3, 'abc', [12, 56, 'cad'])
print('\nSum of only the integer arguments: ', sum_of_integers)

default_return = integer_sum()
print(f'Default value: {default_return}')

another_sum_of_integers = integer_sum(2, 4, 'abc', param_1=2)
print('Sum of only the integer arguments: ', another_sum_of_integers)


# 2

even_num_list = []
odd_num_list = []


def get_sum(number):
    if number == 0:
        return 0
    elif number % 2 == 0:
        even_num_list.append(number)
    else:
        odd_num_list.append(number)
    num_sum = number + get_sum(number - 1)
    return num_sum


even_num_sum = 0
odd_num_sum = 0

sum_get = get_sum(8)

for even_num in even_num_list:
    even_num_sum += even_num

for odd_num in odd_num_list:
    odd_num_sum += odd_num

print(f'\nSum of all numbers between 0 and the function argument: {sum_get}')
print(f'Sum of even numbers between 0 and the function argument: {even_num_sum}')
print(f'Sum of odd numbers between 0 and the function argument: {odd_num_sum}')


# 3


def value_return():
    value = input('\nPlease enter a value: ')
    try:
        value = int(value)
    except ValueError:
        return 0
    else:
        return value


int_value = value_return()
print(f'{int_value} --> type \'{type(int_value).__name__}\'')
