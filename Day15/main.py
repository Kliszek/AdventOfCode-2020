start = [0,8,15,2,12,1,4]

#game = []
num_memory = dict()
last_spoken = 0

for x in range(1,30000000+1):
	if x % 1000000 == 0:
		print(f"{x//300000}%")
	if x <= len(start):
		#game.append(start[x-1])
		num_memory[start[x-1]] = (x,x)
		last_spoken = start[x-1]
		continue
	
	
	dif = num_memory[last_spoken][1]-num_memory[last_spoken][0]
	#game.append(dif)
	last_spoken = dif
	if not dif in num_memory:
		num_memory[dif] = (x,x)
	else:
		num_memory[dif]=(num_memory[dif][1],x)

print(f"2020th number said is: {last_spoken}")