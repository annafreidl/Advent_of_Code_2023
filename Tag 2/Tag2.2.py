# 12 red cubes, 13 green cubes, and 14 blue cubes

input1 = open('Tag 2/input.txt', 'r')
lines = input1.readlines()

gesamtsumme = 0

for line in lines:

    line2 = line.strip("\n")
    game_out = False

    first_split = line2.split(": ")

    draws = first_split[1]
    game = first_split[0]

    draw = draws.split("; ")
    numer_of_draws = len(draw)

    game_number = game.split(" ")[1]

    min_green = 0
    min_red = 0
    min_blue = 0

    for i in range(0, numer_of_draws):

        cubes = draw[i].split(", ")

        for j in range(len(cubes)):

            color = cubes[j].split(" ")[1]
            number = cubes[j].split(" ")[0]

            match color:
                case "green":
                    if int(number) > min_green:
                        min_green = int(number)
                case "blue":
                    if int(number) > min_blue:
                        min_blue = int(number)
                case "red":
                    if int(number) > min_red:
                        min_red = int(number)

    summe = min_green * min_red * min_blue
    gesamtsumme += summe

print("Gesamtsumme: " + str(gesamtsumme))
