def main():
    games = {}
    with open("puzzle_input.txt") as f:
        for line in f:
            game_name, reveals = line[:-1].split(":")
            game_id = int(game_name[5:])
            games[game_id] = []
            reveals = [reveal.strip() for reveal in reveals.split(";")]
            for reveal in reveals:
                cubes = [cube.strip() for cube in reveal.split(",")]
                game = {}
                for cube in cubes:
                    count, name = cube.split(" ")
                    game[name] = int(count)
                games[game_id].append(game)
    sum = 0
    for game_id, reveals in games.items():
        minimums = {
            "red": 1,
            "green": 1,
            "blue": 1,
        }
        for reveal in reveals:
            for color in ["red", "green", "blue"]:
                if color in reveal:
                    if reveal[color] > minimums[color]:
                        minimums[color] = reveal[color]
        power = 1
        for color in ["red", "green", "blue"]:
            power *= minimums[color]
        sum += power
    print(f"sum = {sum}")


if __name__ == "__main__":
    main()
