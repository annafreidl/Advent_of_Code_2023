
input2 = open('Tag 1/input.txt', 'r')
lines = input2.readlines()

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

gesamtsumme = 0


def index_of_first_digit(string):
    counter = 0
    for char in string:
        counter += 1
        if char.isdigit():
            return counter
    return None


def index_of_last_digit(string):
    rev_line = string[::-1]
    counter = 0
    for char in rev_line:
        counter += 1
        if char.isdigit():
            return len(string) - counter + 1


def find_first_digit(substring):
    len_of_five = len(substring) - 5
    if len_of_five < 0:
        for j in numbers:
            if substring.__contains__(j):
                return numbers.index(j) + 1
    for i in range(0, len_of_five + 1):
        five_string = substring[i: i + 5]
        for j in numbers:
            if five_string.__contains__(j):
                return numbers.index(j) + 1
    return None


def find_last_digit(substring):
    len_of_five = len(substring) - 5
    if len_of_five < 0:
        for j in numbers:
            if substring.__contains__(j):
                return numbers.index(j) + 1
    for i in range(0, len_of_five + 1):
        five_string = substring[len_of_five - i: len(substring) - i]
        for j in numbers:
            if five_string.__contains__(j):
                return numbers.index(j) + 1
    return None


for line in lines:

    first_number = ""
    last_number = ""

    # finde die erste Zahl in der Zeile
    first_digit_index = index_of_first_digit(line)
    last_digit_index = index_of_last_digit(line)

    # extrahiere den String vor der ersten Zahl
    substring_before_digit = line[0:first_digit_index - 1]

    # wenn der String kleiner als 3 ist, dann kann direkt ausgeschlossen werden das vor der
    # ersten Zahl eine ausgeschriebene Zahl ist
    if len(substring_before_digit) < 3:
        first_number = line[first_digit_index - 1]

    # sonst Testen, ob im substring vor der ersten Ziffer bereits eine ausgeschriebene Zahl ist
    else:
        first_digit = find_first_digit(substring_before_digit)
        if first_digit is not None:
            first_number = first_digit
        else:
            first_number = line[first_digit_index - 1]

    # erste Zahl festlegen

    last_digit_index = index_of_last_digit(line)

    # extrahiere den String vor der ersten Zahl
    substring_after_digit = line[last_digit_index: len(line) - 1]

    # wenn der String kleiner als 3 ist, dann kann direkt ausgeschlossen werden das vor der
    # ersten Zahl eine ausgeschriebene Zahl ist
    if len(substring_after_digit) < 3:
        last_number = line[last_digit_index - 1]
    # sonst Testen, ob im substring vor der ersten Ziffer bereits eine ausgeschriebene Zahl ist
    else:
        last_digit = find_last_digit(substring_after_digit)
        if last_digit is not None:
            last_number = last_digit
        else:
            last_number = line[last_digit_index - 1]

    nummer = str(first_number) + str(last_number)
    gesamtsumme += int(nummer)
    print("Gesamtsumme: " + str(gesamtsumme))
