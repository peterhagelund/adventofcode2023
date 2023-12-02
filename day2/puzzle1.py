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
    bag = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    sum = 0
    for game_id, reveals in games.items():
        possible = True
        for reveal in reveals:
            for color in ["red", "green", "blue"]:
                if color in reveal and reveal[color] > bag[color]:
                    possible = False
                    # print(f"reveal {reveal} in game {game_id} not possible")
                    break
            if not possible:
                break
        if possible:
            sum += game_id

    print(f"sum = {sum}")


if __name__ == "__main__":
    main()
