# What does this piece of code do?
# Answer: The code simulates a process where it draws random numbers between 1 and 10, adds them up, and keeps track of the total until it has drawn 10 numbers. Finally, it prints the total sum of the drawn numbers.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

total_rand = 0
progress=0
while progress<=10:
	progress+=1
	n = randint(1,10)
	total_rand+=n

print(total_rand)

