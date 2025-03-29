import numpy as np
import matplotlib.pyplot as plt

# alternate model:
# give shape, rows, function for each shape generates objects in dict where each object has spin and neighbor list

class ising: 
	def __init__(self, rows, temp, num_steps):
		self.temp = temp
		self.rng = np.random.default_rng()
		self.size = rows
		self.num_steps = num_steps # num steps

		# constants
		self.j = 1
		# kt 0 - 10 
		# self.kt = self.rng.random() * 10
		self.kt = 2

		# past magnetization
		self.past_mag = []

		self.matrix = self.rng.choice([-1, 1], size=(self.size, self.size))
		self.past_mag.append(self.magnetization())

	def plot_mag(self):
		plt.plot(list(range(0, self.num_steps + 1)), self.past_mag)
		plt.show()
		
	def rand_index(self):
		row_idx = self.rng.integers(0, self.size)
		col_idx = self.rng.integers(0, self.size)
		
		return row_idx, col_idx
	
	def calc_energy(self, row_idx, col_idx):
		energy = 0
		curr_spin = self.matrix[row_idx][col_idx]

		# sum all neighbor spins * current spin
		energy += curr_spin * self.matrix[(row_idx - 1) % self.size][col_idx]
		energy += curr_spin * self.matrix[(row_idx + 1) % self.size][col_idx]
		energy += curr_spin * self.matrix[row_idx][(col_idx - 1) % self.size]
		energy += curr_spin * self.matrix[row_idx][(col_idx + 1) % self.size]

		energy *= -self.j

		return energy

	def metro(self):
		# pick lattice site
		row_idx, col_idx = self.rand_index()
		
		# calc initial energy 
		e_i = self.calc_energy(row_idx, col_idx)

		# flip spin
		self.matrix[row_idx][col_idx] = -self.matrix[row_idx][col_idx]

		# calc final energy, change in energy
		e_f = self.calc_energy(row_idx, col_idx)
		e_change = e_f - e_i


		# print("E_change: ", e_change, "        prob: ",  np.exp(-e_change / self.kt))
		if (e_change < 0) or self.rng.random() < np.exp(-e_change / self.kt):
			# accept move
			pass
		else:
			# flip back
			self.matrix[row_idx][col_idx] = -self.matrix[row_idx][col_idx]

		self.past_mag.append(self.magnetization())

	def magnetization(self):
		output = 0
		for row in range(self.size):
			for col in range(self.size):
				output += self.matrix[row][col]
		output = float(output) / (self.size ** 2)

		return output
	
	def simulate(self):
		j = 0
		for i in range(self.num_steps):
			if i % 10000 == 0:
				print(str(j) + "% - step " +  str(i) + ", mag: " + str(self.past_mag[-1]))
				j += 1
			self.metro()


sim = ising(50, 10, 1000000)

print("Initial mag: ", sim.magnetization())
sim.simulate()
print("Final mag: ",sim.magnetization())
sim.plot_mag()
