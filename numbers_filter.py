n = int(input())

numbers = []

for _ in range(n):
    current_number = int(input())
    numbers.append(current_number)

command = input()

filtrered_numbers = []

if command == 'even':
    for num in numbers:
        if num % 2 == 0:
            filtrered_numbers.append(num)

elif command == 'odd':
    for num in numbers:
        if num % 2 != 0:
            filtrered_numbers.append(num)

elif command == 'positive':
    for num in numbers:
        if num >= 0:
            filtrered_numbers.append(num)

elif command == 'negative':
    for num in numbers:
        if num < 0:
            filtrered_numbers.append(num)

print(filtrered_numbers)