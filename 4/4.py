import re
import reader
data = reader.read()


def parser(data):
	cardsWN = []
	cardsPN = []
	for line in data:
		tmp = line.split(" ")
		tmp = [tmp for tmp in tmp if tmp != ""][2:]
		# numbers before the pipe are WN, the rest are PN
		for i in range(len(tmp)):
			if tmp[i] == "|":
				cardsWN.append([int(x) for x in tmp[:i]])
				cardsPN.append([int(x) for x in tmp[i+1:]])
				break

	return cardsWN, cardsPN


WN, PN = parser(data)

# P1
s = 0
for i in range(len(WN)):
	tmpWN = set(WN[i])
	tmpPN = set(PN[i])
	intersect = tmpWN.intersection(tmpPN)
	if len(intersect) > 0:
		s += 2**(len(intersect)-1)

print("P1:", s)

# P2
cards = [1 for i in range(len(WN))]
for i in range(len(WN)):
	tmpWN = set(WN[i])
	tmpPN = set(PN[i])
	intersect = tmpWN.intersection(tmpPN)
	if len(intersect) > 0:
		for j in range(intersect.__len__()):
			cards[i+j+1] += cards[i]

print("P2:", sum(cards))
