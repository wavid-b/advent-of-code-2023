with open("day1.txt") as file:
    total = 0
    lines = file.readlines()
    numbers_map = {
        "zero": "z0o",
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e"
    }
    for line in lines:
        #replace written out numbers with their numbers_map equivalent
        for k, v in numbers_map.items():
            line = line.replace(k, v)
        first_digit = 0
        second_digit = 0
        for i, v in enumerate(line):
            if v.isdigit():
                first_digit = int(v)
                break
        for i, v in enumerate(reversed(line)):
            if v.isdigit():
                second_digit = int(v)
                break
        first_digit *= 10
        total += first_digit + second_digit
    print(total)