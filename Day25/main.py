public_keys = (8184785,5293040)
subject_number = 7
loop_sizes = [0,0]

print(f"Assume that door's public key is:")
print(f"{public_keys[0]}")
print(f"and card public key is:")
print(f"{public_keys[1]}")

ready = 0
current = 1
it=0
while ready<2:
	it+=1
	current*=subject_number
	current%=20201227
	if current==public_keys[0]:
		ready+=1
		loop_sizes[0]=it
	if current==public_keys[1]:
		ready+=1
		loop_sizes[1]=it

print(f"Loop sizes: {loop_sizes}")


encryption_keys=[1,1]
for x in range(loop_sizes[0]):
	encryption_keys[0]*=public_keys[1]
	encryption_keys[0]%=20201227
for x in range(loop_sizes[1]):
	encryption_keys[1]*=public_keys[0]
	encryption_keys[1]%=20201227

if encryption_keys[0]==encryption_keys[1]:
	print("The encryption key is:")
	print(f"{encryption_keys[0]}")

else:
	print("Something went wrong...")
	print("The encryption keys are:")
	print(f"{encryption_keys[0]}")
	print(f"{encryption_keys[1]}")