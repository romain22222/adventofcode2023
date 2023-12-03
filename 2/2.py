import re
import reader
data = reader.read()


def parser(line):
	# Line example : "Game 1: 7 blue, 5 red; 10 red, 7 blue; 5 blue, 4 green, 15 red; 4 green, 6 red, 7 blue; 5 green, 8 blue, 4 red; 5 red, 4 blue, 3 green"
	# Get the game number, then a list of tuples (color(0 for blue, 1 for red and 2 for green), number)
	game = re.search(r"Game (\d+): (.*)", line)
	game_number = int(game.group(1))
	game = game.group(2)
	game = game.split("; ")
	res = []
	for g in game:
		g = g.split(", ")
		tmp = []
		for m in g:
			m = re.search(r"(\d+) (\w+)", m)
			tmp.append((m.group(2), int(m.group(1))))
		res.append(tmp)
	return game_number, res


games = [parser(line) for line in data]

# P1

impossibles = set()
maxR = 12
maxG = 13
maxB = 14
possibles = set()

for g in games:
	game_number, game = g
	for turn in game:
		for color, number in turn:
			if color == "red" and number > maxR:
				impossibles.add(game_number)
				break
			elif color == "blue" and number > maxB:
				impossibles.add(game_number)
				break
			elif color == "green" and number > maxG:
				impossibles.add(game_number)
				break
	if game_number not in impossibles:
		possibles.add(game_number)

print("P1:", sum(possibles))

# P2

s = 0
for g in games:
	game_number, game = g
	minR = 0
	minG = 0
	minB = 0
	for turn in game:
		for color, number in turn:
			if color == "red":
				minR = max(minR, number)
			elif color == "blue":
				minB = max(minB, number)
			elif color == "green":
				minG = max(minG, number)
	s += minR * minB * minG

print("P2:", s)
