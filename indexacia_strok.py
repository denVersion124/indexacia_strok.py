example = "Python"
first_char = example[0]
print("Первый символ:", first_char)
last_char = example[-1]
print("Последний символ:", last_char)
half_index = len(example) // 2
if len(example) % 2 == 0:
    second_half = example[half_index:]  # Четное количество символов
else:
    second_half = example[half_index + 1:]  # Нечетное количество символов
print("Вторая половина строки:", second_half)
reversed_example = example[::-1]
print("Слово наоборот:", reversed_example)
every_second_char = example[::2]
print("Каждый второй символ:", every_second_char)
