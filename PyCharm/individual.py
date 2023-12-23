def sum_of_absolute_values_after_zero(*args):
    if not args:
        return None

    zero_index = -1

    # Находим индекс первого аргумента, равного нулю
    for i, arg in enumerate(args):
        if arg == 0:
            zero_index = i
            break

    # Если нулевого элемента нет, возвращаем None
    if zero_index == -1:
        return None

    # Суммируем модули аргументов после первого аргумента, равного нулю
    result = sum(abs(arg) for arg in args[zero_index + 1:])

    return result

# Получаем аргументы от пользователя
user_input = input("Введите аргументы через пробел: ")
arguments = [float(arg) for arg in user_input.split()]

# Вызываем функцию с введенными аргументами
result = sum_of_absolute_values_after_zero(*arguments)

print("Результат:", result)
