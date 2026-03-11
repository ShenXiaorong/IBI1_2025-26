total_people=91
infected_people=float(input("please enter the number of infected people：")) # for example, if there are 10 infected people, please enter 10
infection_rate=float(input("please enter the 24 hours infection growth rate：")) # for example, if the infection growth rate is 10%, please enter 0.1
day=0 # day 0 is the day when the first person is infected.
while infected_people<total_people: # the loop will continue until all the people are infected.
    day+=1
    print("the total number of infected people is " + str(infected_people) + " after day" + str(day) ) # print the total number of infected people after each day.
    infected_people=infected_people*(1+infection_rate)
print("It needs " + str(day) + " days for all the people to be infected.") # print the total number of days needed for all the people to be infected.
