import math

def geometric_mean(*args):
    if args:
        number_of_arguments = len(args)
        count = 1
        for i in args:
            count *= i

        solution = math.pow(count, 1 / number_of_arguments)
        return solution

    else:
        return None


if __name__ == "__main__":
    arguments = list(map(int, input("Введите аргументы: ").split()))
    result = geometric_mean(*arguments)
    print(f"Среднее геометрическое ввёденных вами чисел равно: "
          f"{result}")
