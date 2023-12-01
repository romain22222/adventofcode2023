import re
import reader
data = reader.read()

# P1
sum = 0
for line in data:
	# search for the 1st and last digit of the line
	match = re.search(r"^\D*\d", line)
	first = int(match.group(0)[-1])
	match = re.search(r"\d\D*$", line)
	last = int(match.group(0)[0])
	sum += first * 10 + last
print(sum)

# P2
sum = 0
for line in data:
	digs = []
	for i in range(len(line)):
		if line[i].isdigit():
			digs.append(line[i])
		for d, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
			if line[i:].startswith(val):
				digs.append(str(d + 1))
	sum += int(digs[0] + digs[-1])

print(sum)