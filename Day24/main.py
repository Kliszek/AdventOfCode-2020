tiles = list()

with open("input.txt", "r") as f:
	for line in f:
		cords = list()
		bef = ""
		for char in line.strip(" \n"):
			if char=="s":
				bef="s"
			elif char=="n":
				bef="n"
			elif char=="e":
				cords.append(bef+"e")
				bef=""
			elif char=="w":
				cords.append(bef+"w")
				bef=""
		tiles.append(cords)

black_tiles = set()

for tile in tiles:
	x=0
	y=0
	for cord in tile:
		if cord=="e":
			x+=2
		elif cord=="se":
			y-=1
			x+=1
		elif cord=="sw":
			y-=1
			x-=1
		elif cord=="w":
			x-=2
		elif cord=="nw":
			y+=1
			x-=1
		elif cord=="ne":
			y+=1
			x+=1

	if (x,y) in black_tiles:
		black_tiles.remove((x,y))
	else:
		black_tiles.add((x,y))

print(f"Black tiles: {len(black_tiles)}")

def black_neighbours(cord, space):
	neighbours=0
	if (cord[0]+2,cord[1]) in space:
		neighbours+=1
	if (cord[0]-2,cord[1]) in space:
		neighbours+=1
	if (cord[0]+1,cord[1]+1) in space:
		neighbours+=1
	if (cord[0]+1,cord[1]-1) in space:
		neighbours+=1
	if (cord[0]-1,cord[1]+1) in space:
		neighbours+=1
	if (cord[0]-1,cord[1]-1) in space:
		neighbours+=1
	return neighbours

def next_day(space):
	most_left=0
	most_right=0
	most_top=0
	most_bottom=0

	for tile in space:
		if tile[0]<most_left:
			most_left=tile[0]
		if tile[0]>most_right:
			most_right=tile[0]
		if tile[1]<most_bottom:
			most_bottom=tile[1]
		if tile[1]>most_top:
			most_top=tile[1]
	
	new_space = set()
	for x in range(most_left-1,most_right+2):
		for y in range(most_bottom-1,most_top+2):
			if x%2 != y%2:
				continue
			if not (x,y) in space and black_neighbours((x,y), space) == 2:
				new_space.add((x,y))
			if (x,y) in space and 0<black_neighbours((x,y), space)<=2:
				new_space.add((x,y))

	return new_space


current_space = black_tiles
for x in range(0,100):
	current_space = next_day(current_space)

print(f"Black tiles at 100th day: {len(current_space)}")