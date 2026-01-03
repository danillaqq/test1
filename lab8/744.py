import math

# відкриваємо файл з вхідними даними
with open("input.txt", "r") as fin:
    numbers = fin.readlines()

# відкриваємо файл для результату
with open("output.txt", "w") as fout:
    for line in numbers:
        x = float(line.strip())

        # дробова частина
        fractional = x - math.floor(x)

        if fractional < 0.5:
            result = math.floor(x)
        else:
            result = math.ceil(x)

        fout.write(str(result) + "\n")