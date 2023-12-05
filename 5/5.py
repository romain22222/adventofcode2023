import re
import reader
data = reader.read()


def parser(data):
	# 1st line is a line of seeds
	seeds = data[0].split()[1:]
	mappers = []
	i = 3
	while i < len(data):
		mapper = []
		while i < len(data) and data[i] != '\n':
			mapper.append(data[i].split())  # 1st is destStart, 2nd is srcStart, 3rd is length
			i += 1
		mappers.append(mapper)
		i += 2
	return seeds, mappers


seeds, mappers = parser(data)

