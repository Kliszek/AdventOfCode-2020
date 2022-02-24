def get_seat_id(seat):
	front = 0
	bottom = 127
	row = 63
	for x in seat[:7]:
		if x == "F":
			bottom = row
			row = (bottom+front) // 2
		elif x == "B":
			front = row + 1
			row = (front+bottom) // 2
	left = 0
	right = 7
	column = 3
	for x in seat[7:]:
		if x == "L":
			right = column
			column = (left+right) // 2
		else:
			left = column + 1
			column = (left+right) // 2
	return row,column,row*8+column

maximum = 0
occupied = set()
with open("input.txt", "r") as f:
	for line in f:
		rci = get_seat_id(line.strip("\n"))
		occupied.add( (rci[0], rci[1]) )
		id = rci[2]

		if id > maximum:
			maximum = id

print(f"Max ID: {maximum}")

for r in range(1,126):
	for c in range(0,8):
		if not (r,c) in occupied:
			print(f"Free seat: ({r}, {c}) - ID: {r*8+c}")