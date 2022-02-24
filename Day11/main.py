seatmap = []
with open("input.txt", "r") as f:
	for line in f:
		seatmap.append(line.strip(" \n"))

def adjacent(smap, x, y, b=0):
	adj = 0
	for t in range(x+1, len(smap[0])):
		if smap[y][t] == "L":
			break
		if smap[y][t] == "#":
			adj += 1
			if b==1:
				print("right")
			break
	for t in range(x-1, -1, -1):
		if smap[y][t] == "L":
			break
		if smap[y][t] == "#":
			adj+=1
			if b==1:
				print("left")
			break
	for t in range(y+1, len(smap)):
		if smap[t][x] == "L":
			break
		if smap[t][x] == "#":
			adj+=1
			if b==1:
				print("down")
			break
	for t in range(y-1, -1, -1):
		if smap[t][x] == "L":
			break
		if smap[t][x] == "#":
			adj+=1
			if b==1:
				print("up")
			break
	for t in range(1, len(smap[0])):
		if x+t >= len(smap[0]) or y+t >= len(smap):
			break
		if smap[y+t][x+t] == "L":
			break
		if smap[y+t][x+t] == "#":
			adj+=1
			if b==1:
				print("rightdown")
			break
	for t in range(1, len(smap[0])):
		if x+t >= len(smap[0]) or y-t < 0:
			break
		if smap[y-t][x+t] == "L":
			break
		if smap[y-t][x+t] == "#":
			adj+=1
			if b==1:
				print("rightup")
			break
	for t in range(1, len(smap[0])):
		if x-t < 0 or y-t < 0:
			break
		if smap[y-t][x-t] == "L":
			break
		if smap[y-t][x-t] == "#":
			adj+=1
			if b==1:
				print("leftup")
			break
	for t in range(1, len(smap[0])):
		if x-t < 0 or y+t >= len(smap):
			break
		if smap[y+t][x-t] == "L":
			break
		if smap[y+t][x-t] == "#":
			adj+=1
			if b==1:
				print("leftdown")
			break
	return adj


def simulate(smap):
	newmap = []
	for y in range(len(smap)):
		newmap.append("")
		for x in range(len(smap[0])):
			if smap[y][x] == ".":
				newmap[y] += "."
				continue
			adj = adjacent(smap,x,y)
			if smap[y][x] == "L" and adj==0:
				newmap[y] += "#"
			elif smap[y][x] == "#" and adj>=5:
				newmap[y] += "L"
			else:
				newmap[y] += smap[y][x]
	return newmap	


result = seatmap

while True:
	occ_1 = 0
	for x in result:
		occ_1 += x.count("#")
	#print(f"Before: {occ_1}")

	result = simulate(result)

	occ_2 = 0
	for x in result:
		occ_2 += x.count("#")

	#print(f"After: {occ_2}\n\n")

	if occ_1 == occ_2:
		print(f"The result is {occ_1}")
		break


