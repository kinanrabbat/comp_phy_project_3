
import numpy as np
import matplotlib.pyplot as plt


# alternate model:
# give shape, rows, function for each shape generates objects in dict where each object has spin and neighbor list

class ising: 
	def __init__(self, shape, size, temp):
		self.rng = np.random.default_rng()
		self.temp = temp
		self.size = size
		self.shape = shape
		
		# every atom has key (x, y) and val ist of [spin, neighbor_list]
		self.atoms = {} 
		
		if self.shape == "square": 
			self.gen_square()
		elif self.shape == "triangle": 
			self.gen_triangle()
			
		self.num_steps = 100000 # num steps

		# constants
		self.j = 1
		self.kt = temp 

		# past magnetization
		self.past_mag = []

		self.past_mag.append(self.magnetization())

	def valid(self, row, col):
		return row >= 0 and row < self.size and col >= 0 and col < self.size
		
	def gen_triangle(self):
		for row in range(self.size):
			for col in range(self.size):
				spin = int(self.rng.choice([-1, 1]))
				neighbor_list = []
				if self.valid(row - 1, col - 1):
					neighbor_list.append(((row - 1, col - 1)))
				if self.valid(row - 1, col):
					neighbor_list.append(((row - 1, col)))
				if self.valid(row, col + 1):
					neighbor_list.append(((row, col + 1)))
				if self.valid(row + 1, col + 1):
					neighbor_list.append(((row + 1, col + 1)))
				if self.valid(row + 1, col):
					neighbor_list.append(((row + 1, col)))
				if self.valid(row, col - 1):
					neighbor_list.append(((row, col - 1)))

				self.atoms[(row, col)] = [spin, neighbor_list]

	def gen_square(self):
		for row in range(self.size):
			for col in range(self.size):
				spin = int(self.rng.choice([-1, 1]))
				neighbor_list = (((row - 1) % self.size, col), 
					 			 ((row + 1) % self.size, col), 
								 ((row, (col - 1) % self.size)), 
								 ((row, (col + 1) % self.size)))
				self.atoms[(row, col)] = [spin, neighbor_list]
		
	def plot_mag(self):
		plt.plot(list(range(0, self.num_steps + 1)), self.past_mag)
		plt.show()
		
	def rand_index(self):
		row_idx = self.rng.integers(0, self.size)
		col_idx = self.rng.integers(0, self.size)
		
		return row_idx, col_idx
	
	def calc_energy(self, row_idx, col_idx):
		energy = 0
		curr_spin = self.atoms[(row_idx, col_idx)][0]

		# sum all neighbor spins * current spin
		for neighbor in self.atoms[(row_idx, col_idx)][1]:
			energy += curr_spin * self.atoms[neighbor][0]

		energy *= -self.j

		return energy

	def metro(self):
		# pick lattice site
		row_idx, col_idx = self.rand_index()
		
		# calc initial energy 
		e_i = self.calc_energy(row_idx, col_idx)

		# flip spin
		self.atoms[(row_idx, col_idx)][0] *= -1

		# calc final energy, change in energy
		e_f = self.calc_energy(row_idx, col_idx)
		e_change = e_f - e_i

		if (e_change < 0) or self.rng.random() < np.exp(-e_change / self.kt):
			# accept move
			pass
		else:
			# flip back
			self.atoms[(row_idx, col_idx)][0] *= -1

		self.past_mag.append(self.magnetization())

	def magnetization(self):
		output = 0

		for atom in self.atoms.values():
			output += atom[0]
		output = float(output) / (self.size ** 2)

		if(output < 0):
			output = -1* output

		return output
	
	def simulate(self):
		for _ in range(self.num_steps):
			self.metro()


initial_list = []
final_list = []

for i in range (1, 10):
	sim = ising("triangle", 12, i)
	initial_list.append(sim.magnetization())
	sim.simulate()
	final_list.append(sim.magnetization())
	print(i)


# Assuming initial_list and final_list are already populated
temperatures = list(range(1, 10))  # Temperature range from 180 to 299

plt.figure(figsize=(8, 5))
plt.plot(temperatures, initial_list, label="Initial Magnetization", marker="o")
plt.plot(temperatures, final_list, label="Final Magnetization", marker="s")

plt.xlabel("Temperature")
plt.ylabel("Magnetization")
plt.title("Initial and Final Magnetization vs Temperature")
plt.legend()
plt.grid(True)

plt.show()



# print("Initial mag: ", sim.magnetization())
# sim.simulate()
# print("Final mag: ",sim.magnetization())
# sim.plot_mag()

