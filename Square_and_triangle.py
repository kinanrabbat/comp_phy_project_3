import numpy as np
import matplotlib.pyplot as plt
import math

lattice_type = 'triangular' #square or triangular
row_length = 100
n = row_length * row_length
rng = np.random.default_rng()
arr = rng.choice([-1, 1], size=n)

def plot_lattice(arr, lattice_type, row_length):
    if lattice_type == 'square':
        plt.matshow(arr.reshape(row_length, row_length), cmap='bwr', vmin=-1, vmax=1)
        plt.colorbar()
        plt.show()
    elif lattice_type == 'triangular':
        xs = []
        ys = []
        colors = []
        for j in range(row_length):
            for i in range(row_length):
                x = i + j/2
                y = (math.sqrt(3)/2) * j
                xs.append(x)
                ys.append(y)
                colors.append('red' if arr[j * row_length + i] == 1 else 'blue')
        plt.figure(figsize=(8, 8))
        plt.scatter(xs, ys, c=colors, s=20)
        plt.title("Triangular Lattice (Parallelogram)")
        plt.show()
    elif lattice_type == 'hexagonal':
        plt.matshow(arr.reshape(row_length, row_length), cmap='bwr', vmin=-1, vmax=1)
        plt.colorbar()
        plt.show()

def create_adjacency_matrix_triangular(row_length):
    n = row_length * row_length
    A = np.zeros((n, n), dtype=int)
    for j in range(row_length):
        for i in range(row_length):
            idx = j * row_length + i
            left_i = (i - 1) % row_length
            right_i = (i + 1) % row_length
            up_j = (j - 1) % row_length
            down_j = (j + 1) % row_length
            A[idx, j * row_length + left_i] = 1
            A[idx, j * row_length + right_i] = 1
            A[idx, up_j * row_length + i] = 1
            A[idx, down_j * row_length + i] = 1
            A[idx, up_j * row_length + right_i] = 1
            A[idx, down_j * row_length + left_i] = 1
    return A

def create_adjacency_matrix_square(row_length):
    n = row_length * row_length
    A = np.zeros((n, n), dtype=int)
    for i in range(n):
        row = i // row_length
        col = i % row_length
        A[i, row * row_length + ((col - 1) % row_length)] = 1
        A[i, row * row_length + ((col + 1) % row_length)] = 1
        A[i, ((row - 1) % row_length) * row_length + col] = 1
        A[i, ((row + 1) % row_length) * row_length + col] = 1
    return A

def create_adjacency_matrix_hexagonal(row_length):
    return create_adjacency_matrix_square(row_length)

def get_adjacency_matrix(lattice_type, row_length):
    if lattice_type == 'square':
        return create_adjacency_matrix_square(row_length)
    elif lattice_type == 'triangular':
        return create_adjacency_matrix_triangular(row_length)
    elif lattice_type == 'hexagonal':
        return create_adjacency_matrix_hexagonal(row_length)
    else:
        raise ValueError("Unsupported lattice type.")

A = get_adjacency_matrix(lattice_type, row_length)
print("Adjacency matrix:")
print(A)

def neighbor_energy(i):
    return arr[i] * np.dot(A[i], arr)

def metropolis_step(T):
    i = rng.integers(0, n)
    dE = 2 * neighbor_energy(i)
    if dE <= 0 or rng.random() < np.exp(-dE / T):
        arr[i] *= -1

def total_energy():
    return -0.5 * np.sum(A * np.outer(arr, arr))

def magnetization():
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
    plot_lattice(arr, lattice_type, row_length)
    return energies, mags

T = 2.0 # Temperature
steps = 100000
energies, mags = simulate(steps, T)
