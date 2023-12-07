import math
import re
import reader

data = reader.read()


def parser(data):
	# Each line is 5 cards labeled 2-9 then T, J, Q, K, A followed by a bid (int)

	cards = []
	bids = []
	for line in data:
		cards.append(line[:5])
		bids.append(int(line[6:]))

	return cards, bids


cards, bids = parser(data)


# P1
def get_id(hand):
	unique_values = set(hand)
	match len(unique_values):
		case 5:
			return 0
		case 4:
			return 1
		case 3:
			for value in unique_values:
				if hand.count(value) == 2:
					return 2
			return 3
		case 2:
			for value in unique_values:
				if hand.count(value) == 3:
					return 4
			return 5
		case _:
			return 6

cardsCopy = cards.copy()
for i in range(len(cards)):
	# Transform each card so that it can be sorted
	string = cards[i]
	string = string.replace("J", "B")
	string = string.replace("Q", "C")
	string = string.replace("K", "D")
	string = string.replace("A", "E")
	string = string.replace("T", "A")
	cardsCopy[i] = str(get_id(cards[i])) + string


cardsSorted = cardsCopy[:]
cardsSorted.sort()

s = 0
for i in range(len(cardsSorted)):
	s += bids[cardsCopy.index(cardsSorted[i])] * (i + 1)

print("P1:", s)

# J is now the joker and also the weakest card
def get_id2(hand):
	unique_values = set(hand)
	unique_values.discard("J")
	match len(unique_values):
		case 5:
			return 0
		case 4:
			return 1
		case 3:
			if "J" in hand:
				return 3
			for value in unique_values:
				if hand.count(value) == 2:
					return 2
			return 3
		case 2:
			if "J" in hand:
				if all(hand.count(value) == 2 for value in unique_values):
					return 4
				return 5
			for value in unique_values:
				if hand.count(value) == 3:
					return 4
			return 5
		case _:
			return 6

cardsCopy = cards.copy()
for i in range(len(cards)):
	# Transform each card so that it can be sorted
	string = cards[i]
	string = string.replace("J", "1")
	string = string.replace("Q", "B")
	string = string.replace("K", "C")
	string = string.replace("A", "D")
	string = string.replace("T", "A")
	cardsCopy[i] = str(get_id2(cards[i])) + string


cardsSorted = cardsCopy[:]
cardsSorted.sort()

s = 0
for i in range(len(cardsSorted)):
	s += bids[cardsCopy.index(cardsSorted[i])] * (i + 1)

print("P2:", s)