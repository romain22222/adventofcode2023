import math
import re
import reader
data = reader.read()


def parser(data):
	# 1st line are times
	# 2nd line are distances

	# Parse times
	times = [int(n) for n in re.findall(r"\d+", data[0])]

	# Parse distances
	distances = [int(n) for n in re.findall(r"\d+", data[1])]

	return [(times[i], distances[i]) for i in range(len(times))]


records = parser(data)
print(records)

# P1
# For a time T, you can hold a button for x seconds and then go x*(T-x) distance
# You thus want to solve for x in x*(T-x) = D
# Solve for x
# x^2 - Tx + D = 0
# x = (T +- sqrt(T^2 - 4D)) / 2
waysToBeatDistance = 1
for record in records:
	time, distance = record
	x1 = (time - (time**2 - 4*distance)**0.5) / 2
	x2 = (time + (time**2 - 4*distance)**0.5) / 2
	amountOfSolution = len(range(math.ceil(x1), math.ceil(x2)))
	waysToBeatDistance *= amountOfSolution

print("P1:", waysToBeatDistance)


# P2

# Concatenate all the distances and times
# Same reasoning as P1

time = ""
distance = ""
for record in records:
	time += str(record[0])
	distance += str(record[1])

time = int(time)
distance = int(distance)

x1 = (time - (time**2 - 4*distance)**0.5) / 2
x2 = (time + (time**2 - 4*distance)**0.5) / 2
amountOfSolution = len(range(math.ceil(x1), math.ceil(x2)))

print("P2:", amountOfSolution)
