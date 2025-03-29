import numpy as np
import matplotlib.pyplot as plt

row_length = 50
n = row_length * row_length
rng = np.random.default_rng()

# Initialize the spin lattice
arr = rng.choice([-1, 1], size=n)
print("Initial state:")
print(arr.reshape(row_length, row_length))
plt.matshow(arr.reshape(row_length, row_length), cmap='bwr', vmin=-1, vmax=1)
plt.colorbar()
plt.show()

def create_adjacency_matrix(row_length):
    n = row_length * row_length
    A = np.zeros((n, n), dtype=int)
    for i in range(n):
        row = i // row_length
        col = i % row_length

        # Glued left neighbor:
        left_col = (col - 1) % row_length
        left_index = row * row_length + left_col
        A[i, left_index] = 1

        # Glued right neighbor:
        right_col = (col + 1) % row_length
        right_index = row * row_length + right_col
        A[i, right_index] = 1

        # Glued top neighbor:
        up_row = (row - 1) % row_length
        up_index = up_row * row_length + col
        A[i, up_index] = 1

        # Glued bottom neighbor:
        down_row = (row + 1) % row_length
        down_index = down_row * row_length + col
        A[i, down_index] = 1

    return A

A = create_adjacency_matrix(row_length)
print("Adjacency matrix")
print(A)

def neighbor_energy(i):
    return arr[i] * np.dot(A[i], arr)

print("Neighbor energy at index 0:", neighbor_energy(0))

def metropolis_step(T):
    i = rng.integers(0, n)
    dE = 2 * neighbor_energy(i)
    if dE <= 0 or rng.random() < np.exp(-dE / T):
        arr[i] *= -1

def total_energy():
    return -0.5 * np.sum(A * np.outer(arr, arr))

def magnetization():
    # Return the average magnetization per spin (range between -1 and 1)
    return np.sum(arr) / n

def simulate(steps, T):
    energies = []
    mags = []
    for step in range(steps):
        metropolis_step(T)
        if step % 500 == 0:
            energy = total_energy()
            mag = magnetization()
            energies.append(energy)
            mags.append(mag)
            print(f"Step: {step} Energy: {energy} Magnetization: {mag}")
    print("Final state:")
    print(arr.reshape(row_length, row_length))
    plt.matshow(arr.reshape(row_length, row_length), cmap='bwr', vmin=-1, vmax=1)
    plt.colorbar()
    plt.show()
    return energies, mags

T = 2.0  # Temperature
steps = 100000  # Increase number of steps to allow the system to equilibrate
energies, mags = simulate(steps, T)
