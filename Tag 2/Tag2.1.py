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

    for i in range(0, numer_of_draws):

        cubes = draw[i].split(", ")

        for j in range(len(cubes)):

            color = cubes[j].split(" ")[1]
            number = cubes[j].split(" ")[0]

            match color:
                case "green":
                    if int(number) > 13:
                        game_out = True
                        break
                case "blue":
                    if int(number) > 14:
                        game_out = True
                        break
                case "red":
                    if int(number) > 12:
                        game_out = True
                        break

    if not game_out:
        gesamtsumme += int(game_number)

print("Gesamtsumme: " + str(gesamtsumme))
