number_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# Version 1
print('\n\t\t\t\tVersion 1')
print('\nThis is the original list:', number_list,
      '\b, memory location:', id(number_list))

ordered_list = [number_list[-5], number_list[3], number_list[4], number_list[-4], number_list[-2],
                number_list[-1], number_list[0], number_list[1], number_list[2], number_list[-3]]

print('This is the ordered list:', ordered_list,
      '\b, memory location:', id(ordered_list))
print('This is the ordered list, but in reverse:', ordered_list[::-1],
      '\b, memory location:', id(ordered_list))
print('These are the even numbers in the ordered list:', ordered_list[1::2],
      '\b, memory location:', id(ordered_list))
print('These are the odd numbers in the ordered list:', ordered_list[::2],
      '\b, memory location:', id(ordered_list))
print('These are the multiples of 3 from our ordered list:', ordered_list[2::3],
      '\b, memory location:', id(ordered_list))

print('The original list is the same:', number_list,
      '\b, memory location:', id(number_list))


# Version 2
print('\n\n\t\t\t\tVersion 2')
print('\nThis is the original list:', number_list,
      '\b, memory location:', id(number_list))

formatted_list = list(number_list)  # formatted_list = number_list[:]
print('This is a copy of the original list:', formatted_list,
      '\b, memory location:', id(formatted_list))

formatted_list.sort()
print('This is the copied list, ordered:', formatted_list,
      '\b, memory location:', id(formatted_list))
formatted_list.reverse()
print('This is the copied list, ordered in reverse:', formatted_list,
      '\b, memory location:', id(formatted_list))

print('The original list is the same:', number_list,
      '\b, memory location:', id(number_list))

number_list.sort()
print('These are the even numbers of the original ordered list:', number_list[1::2],
      '\b, memory location:', id(number_list))

print('These are the odd numbers of the original ordered list:', number_list[::2],
      '\b, memory location:', id(number_list))

print('These are the multiples of 3 from our ordered list:', number_list[2::3],
      '\b, memory location:', id(number_list))

print('The original list is the same:', number_list,
      '\b, memory location:', id(number_list))