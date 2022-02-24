class space():
	def __init__(self):
		self.cords = dict()
		self.x_range=range(-1,2)
		self.y_range=range(-1,2)
		self.z_range=range(-1,2)
		self.w_range=range(-1,2)
		self.active = 0

	def set_cube(self, xyzw, active):
		if active==True or active=="#":
			self.cords[xyzw] = "#"
			self.active += 1
		else:
			self.cords[xyzw] = "."
		
		if xyzw[0] >= self.x_range.stop-1:
			self.x_range = range(self.x_range.start, xyzw[0]+2)
		elif xyzw[0] < self.x_range.start+1:
			self.x_range = range(xyzw[0]-1, self.x_range.stop)
		
		if xyzw[1] >= self.y_range.stop-1:
			self.y_range = range(self.y_range.start, xyzw[1]+2)
		elif xyzw[1] < self.y_range.start+1:
			self.y_range = range(xyzw[1]-1, self.y_range.stop)
		
		if xyzw[2] >= self.z_range.stop-1:
			self.z_range = range(self.z_range.start, xyzw[2]+2)
		elif xyzw[2] < self.z_range.start+1:
			self.z_range = range(xyzw[2]-1, self.z_range.stop)

		if xyzw[3] >= self.w_range.stop-1:
			self.w_range = range(self.w_range.start, xyzw[3]+2)
		elif xyzw[3] < self.w_range.start+1:
			self.w_range = range(xyzw[3]-1, self.w_range.stop)

	def is_active(self, xyzw):
		if not xyzw in self.cords:
			return False
		if self.cords[xyzw] == ".":
			return False
		else:
			return True

	def _is_neighbour(self, c1,c2):
		if abs(c1[0]-c2[0]) > 1:
			return False
		if abs(c1[1]-c2[1]) > 1:
			return False
		if abs(c1[2]-c2[2]) > 1:
			return False
		if abs(c1[3]-c2[3]) > 1:
			return False
		return True

	def active_neighbours(self, xyzw):
		neighbours = 0
		for x in range(xyzw[0]-1, xyzw[0]+2):
			for y in range(xyzw[1]-1, xyzw[1]+2):
				for z in range(xyzw[2]-1, xyzw[2]+2):
					for w in range(xyzw[3]-1, xyzw[3]+2):
						if (x,y,z,w) == xyzw:
							continue
						if self.is_active((x,y,z,w)):
							neighbours += 1
		return neighbours

	def next_cycle(self):
		next_state = space()
		for x in self.x_range:
			for y in self.y_range:
				for z in self.z_range:
					for w in self.w_range:
						neighbours = self.active_neighbours((x,y,z,w))
						if self.is_active((x,y,z,w)):
							if neighbours==2 or neighbours==3:
								next_state.set_cube((x,y,z,w),1)
							else:
								next_state.set_cube((x,y,z,w),0)
						else:
							if neighbours==3:
								next_state.set_cube((x,y,z,w),1)
							else:
								next_state.set_cube((x,y,z,w),0)
		return next_state


initial_state = space()

with open("input.txt", "r") as f:
	y=0
	for line in f:
		x=0
		for state in line.strip(" \n"):
			initial_state.set_cube((x,y,0,0),state)
			x+=1
		y+=1

print(initial_state.next_cycle().next_cycle().next_cycle().next_cycle().next_cycle().next_cycle().active)