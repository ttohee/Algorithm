number = list(map(int, list(input())))
number.sort(reverse = True)
number = list(map(str, number))
print(''.join(number))