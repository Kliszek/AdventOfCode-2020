instructions = list()
with open("input.txt", "r") as f:
	for line in f:
		instructions.append((line[0], int(line[1:])))

x_cord = 0
y_cord = 0
facing = 0 #E-0, S-1, E-2, N-3
waypoint = [10,1]

for x in instructions:
	if x[0] == "N":
		waypoint[1] += x[1]
	elif x[0] == "S":
		waypoint[1] -= x[1]
	elif x[0] == "E":
		waypoint[0] += x[1]
	elif x[0] == "W":
		waypoint[0] -= x[1]
	elif x[0] == "L":
		for a in range(0,x[1]//90):
			t = waypoint[0]
			waypoint[0] = -1 * waypoint[1]
			waypoint[1] = t
	elif x[0] == "R":
		for a in range(0,x[1]//90):
			t = waypoint[0]
			waypoint[0] = waypoint[1]
			waypoint[1] = -1 * t
	elif x[0] == "F":
		x_cord += x[1]*waypoint[0]
		y_cord += x[1]*waypoint[1]

print(f"Manhatan distance: {abs(x_cord)+abs(y_cord)}")