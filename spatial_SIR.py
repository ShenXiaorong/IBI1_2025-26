# import necessary libraries
import numpy as np
import matplotlib . pyplot as plt
S=0
I=1
R=2
# make array of all susceptible population
population = np. zeros( (100, 100) )
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1
beta = 0.3
gamma = 0.05

# plot at selected times
plot_times = [0, 10, 50, 100]

for t in range(101):
    if t in plot_times:
        plt.figure(figsize=(6, 4), dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f"Time = {t}")
        plt.show()

    # make a copy so updates do not affect the same step immediately
    new_population = population.copy()

    # find all infected individuals
    infected_positions = np.argwhere(population == 1)

    for pos in infected_positions:
        row = pos[0]
        col = pos[1]

        # check 8 neighbours
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue

                nr = row + dr
                nc = col + dc

                # make sure neighbour is inside the grid
                if 0 <= nr < 100 and 0 <= nc < 100:
                    if population[nr, nc] == 0:
                        if np.random.random() < beta:
                            new_population[nr, nc] = 1

        # infected person may recover
        if np.random.random() < gamma:
            new_population[row, col] = 2

    population = new_population