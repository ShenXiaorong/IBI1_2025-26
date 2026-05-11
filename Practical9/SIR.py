# import necessary libraries
import numpy as np
import matplotlib . pyplot as plt
N=10000
S=9999
I=1
R=0
beta=0.3
gamma=0.05
S_values = [S]
I_values = [I]
R_values = [R]
#Repeat for 1000 time steps:
#    calculate infection probability
#    calculate recovery probability
#    randomly choose new infections from susceptible people
#    randomly choose new recoveries from infected people
#    update S, I, and R
#    record the new values of S, I, and R
#Plot S, I, and R over time
t=1
while t<=1000:
    infection_rate = beta*I/N
    recovery_rate = gamma
    new_infections = np.random.choice(range(2), S, p=[1-infection_rate, infection_rate])
    new_recoveries = np.random.choice(range(2), I, p=[1-recovery_rate, recovery_rate])
    S=S - new_infections.sum()
    I=I + new_infections.sum() - new_recoveries.sum()
    R=R + new_recoveries.sum()

    S_values.append(S)
    I_values.append(I)
    R_values.append(R)

    t += 1

time = range(len(S_values))
plt . figure ( figsize =(6,4),dpi=150)
plt.plot(time, S_values, label='susceptible')
plt.plot(time, I_values, label='infected')
plt.plot(time, R_values, label='recovered')
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.legend()
plt . savefig ('SIR_model.png')
plt.show()
