cups = [1,2,3,4,5,6,7,8,9,]

for x in range(10,10001):
	cups.append(x)

curr_index=0

#picked_up = []

def make_move(cup_list, curr):
	d = len(cup_list)
	curr_val = cup_list[curr]
	#print(f"cups: {cup_list}")
	picked_up_ind = [(curr+i)%d for i in range(1,4)]
	if cup_list[picked_up_ind[0]]!=1 and cup_list[picked_up_ind[1]]!=1 and cup_list[picked_up_ind[2]]!=1:
		return cup_list
	picked_up = [cup_list[x] for x in picked_up_ind]
	#print(f"picked up: {picked_up}")

	dest = curr_val-1

	#del cup_list[picked_up_ind[2]]
	#del cup_list[picked_up_ind[1]]
	#del cup_list[picked_up_ind[0]]
	cup_list.remove(picked_up[0])
	cup_list.remove(picked_up[1])
	cup_list.remove(picked_up[2])

	while dest in picked_up or dest<1:
		dest-=1
		if dest < 1:
			dest = max(cup_list)
	#print(f"destination: {dest}")
	
	dest_ind = cup_list.index(dest)
	cup_list.insert((dest_ind+1)%d, picked_up[2])
	cup_list.insert((dest_ind+1)%d, picked_up[1])
	cup_list.insert((dest_ind+1)%d, picked_up[0])
	
	while cup_list[curr] != curr_val:
		cup_list.append(cup_list[0])
		del cup_list[0]

	return cup_list


for x in range(0,100000):
	#if x%100 == 0:
		#print(".")
	#print(f"-- move {x+1} --")
	cups = make_move(cups, x%len(cups))
	#print("\n")

ind_of_one = cups.index(1)

factor1 = cups[(ind_of_one+1)%len(cups)]
factor2 = cups[(ind_of_one+2)%len(cups)]

#print(f"The result is: {factor1*factor2}")


#for x in range(20):
#	print(f"{cups[x]}, ")

#print(f"index of 1: {ind_of_one}")
#print(cups)
print(f"1: {factor1}\n2: {factor2}")
print(f"index of 1: {ind_of_one}")