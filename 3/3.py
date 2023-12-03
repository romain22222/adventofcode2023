import re
import reader
data = reader.read()


def parser(data):
	# Get all numbers with their positions
	# Data looks like this :
	"""
		467..114..
		...*......
		..35..633.
		......#...
		617*......
		.....+.58.
		..592.....
		......755.
		...$.*....
		.664.598..
	"""
	numbers = []
	# numbers is of form [(number, (xFrom, xTo, y))]
	symbols = {}
	starPos = []
	numbersBis = {}
	for i in range(len(data)):
		currentNUmber = ""
		xFrom = 0
		numbersBis[i] = {}
		for j in range(len(data[i])):
			if data[i][j] in "0123456789":
				if currentNUmber == "":
					xFrom = j
				currentNUmber += data[i][j]
				numbersBis[i][j] = data[i][j]
			else:
				if data[i][j] in "*=+/&#%-$@":
					if data[i][j] == "*":
						starPos.append((i, j))
					if i not in symbols:
						symbols[i] = []
					symbols[i].append(j)
				if currentNUmber != "":
					numbers.append((int(currentNUmber), (xFrom, j, i)))
					currentNUmber = ""
		if currentNUmber != "":
			numbers.append((int(currentNUmber), (xFrom, len(data[i]), i)))
	return numbers, symbols, starPos, numbersBis


numbers, symbols, starPos, numberBis = parser(data)

# P1

adjacency = []

# Find all numbers which are not adjacent to any symbol (diagonal included)
for v in numbers:
	xFrom, xTo, y = v[1]
	adj = False
	for i in range(y-1, y+2):
		if i in symbols:
			for j in range(xFrom-1, xTo+1):
				if j in symbols[i]:
					adj = True
					break
	if adj:
		adjacency.append(v[0])

print("P1:", sum(adjacency))

# P2
# Check for each star if it is adjacent to exactly 2 numbers
# If so, multiply them and add to the result
s = []
for star in starPos:
	x, y = star
	adj = 0
	onCn = False
	prox = []
	for i in range(x-1, x+2):
		if i in numberBis:
			onCn = False
			for j in range(y-3, y+4):
				if j in numberBis[i]:
					prox.append((i, j, numberBis[i][j]))
					if not onCn and i in range(x-1, x+2) and j in range(y-1, y+2):
						adj += 1
						onCn = True
				else:
					onCn = False
	if adj == 2:
		s.append([star, prox])

sumProx = 0

# For each star, recompose the numbers that are adjacent to it
for star in s:
	prox = star[1]
	# Find the numbers that are adjacent to the star
	proxNum = []
	currentProx = prox[0][2]
	lastX = prox[0][0]
	lastY = prox[0][1]
	valid = lastX in range(star[0][0]-1, star[0][0]+2) and lastY in range(star[0][1]-1, star[0][1]+2)
	for p in prox[1:] + [(-1, -1, "")]:
		x, y, n = p
		# Check if the digit is on the same line and if it is adjacent to the previous one
		if x == lastX and y == lastY+1:
			currentProx += n
			lastY = y
		else:
			if valid:
				proxNum.append(int(currentProx))
			currentProx = n
			lastX = x
			lastY = y
			valid = x in range(star[0][0]-1, star[0][0]+2) and y in range(star[0][1]-1, star[0][1]+2)
		if x in range(star[0][0]-1, star[0][0]+2) and y in range(star[0][1]-1, star[0][1]+2):
			valid = True
	sumProx += proxNum[0] * proxNum[1]

print("P2:", sumProx)


