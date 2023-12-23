import math

def harmonic_mean(*args):
    if args:
        number_of_arguments = len(args)
        count = 0
        for i in args:
            count += 1/i

        return number_of_arguments/count

    else:
        return None


if __name__ == "__main__":
    arguments = list(map(int, input("Введите аргументы: ").split()))
    result = harmonic_mean(*arguments)

    print(f"Среднее гармоническое ввёденных вами аргументов равно: "
          f"{result}")