import re
import reader
data = reader.read()


def parser(data):
	# 1st line is a line of seeds
	seeds = [int(d) for d in data[0].split()[1:]]
	mappers = []
	i = 3
	while i < len(data):
		mapper = []
		while i < len(data) and data[i] != '\n':
			mapper.append([int(d) for d in data[i].split()])  # 1st is destStart, 2nd is srcStart, 3rd is length
			i += 1
		mappers.append(mapper)
		i += 2
	return seeds, mappers


seedsInitial, mappers = parser(data)


# P1
seeds = seedsInitial.copy()
for instruction in mappers:
	for i, s in enumerate(seeds):
		for r in instruction:
			if r[1] <= s < r[1] + r[2]:
				seeds[i] = r[0] + (s - r[1])
				break

print("P1:", min([int(s) for s in seeds]))

# P2
seedRanges = []
i = 0
while i < len(seedsInitial):
	seedRanges.append([seedsInitial[i], seedsInitial[i] + seedsInitial[i + 1]])
	i += 2
for instruction in mappers:
	newSeedRanges = []
	for s in seedRanges:
		tmp = s
		for r in instruction:
			if r[1] <= tmp[0] <= tmp[1] <= r[1] + r[2]:
				newSeedRanges.append([r[0] + (tmp[0] - r[1]), r[0] + (tmp[1] - r[1])])
				break
			elif r[1] <= tmp[0] < r[1] + r[2] < tmp[1]:
				newSeedRanges.append([r[0] + (tmp[0] - r[1]), r[0] + r[2]])
				tmp = [r[2] + r[1], tmp[1]]
			elif tmp[0] < r[1] <= tmp[1] <= r[1] + r[2]:
				newSeedRanges.append([r[0], r[0] + (tmp[1] - r[1])])
				tmp = [tmp[0], r[1]]
		else:
			newSeedRanges.append(tmp)
	seedRanges = newSeedRanges[:]

print("P2:", min([s[0] for s in seedRanges]))
