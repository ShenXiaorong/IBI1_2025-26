# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

N = 10000
beta = 0.3
gamma = 0.05

vaccination_rates = [i / 10 for i in range(11)]

plt.figure(figsize=(8, 5), dpi=150)

for v in vaccination_rates:
    # initial numbers for this vaccination rate
    V = int(N * v)
    if V == N:
        S = 0
        I = 0
    else:
        I = 1
        S = N - V - I
    R = 0

    # store infected values over time
    I_values = [I]

    t = 1
    while t <= 1000:
        infection_rate = beta * I / N
        recovery_rate = gamma

        if S > 0:
            new_infections = np.random.choice([0, 1], S, p=[1 - infection_rate, infection_rate])
        else:
            new_infections = np.array([0])

        if I > 0:
            new_recoveries = np.random.choice([0, 1], I, p=[1 - recovery_rate, recovery_rate])
        else:
            new_recoveries = np.array([0])

        S = S - new_infections.sum()
        I = I + new_infections.sum() - new_recoveries.sum()
        R = R + new_recoveries.sum()

        I_values.append(I)
        t += 1

    time = range(len(I_values))
    plt.plot(time, I_values, label=f"{int(v * 100)}%", color=cm.viridis(v))

plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model with different vaccination rates')
plt.legend()
plt.savefig('SIR_vaccination.png')
plt.show()
