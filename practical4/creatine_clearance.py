# First, let the user enter the age, weight, gender, and creatine concentration.
# Second, check for valid input and prints error messages if the input is invalid.
# Third, calculate the creatine clearance using the appropriate formula based on the gender of the person.
# Finally, print the creatine clearance in µmol/l.

age=int(input("please enter your age in years:"))                                              # store the age of the person in years.
while age<=0 or age>=100:                                                                      # if the age is less than or equal to 0 or greater than or equal to 100, print an error message.
    print("Error: age must be greater than 0 and less than 100.")
    age=int(input("please enter your age in years:"))                                          # ask the user to enter the age again until a valid age is entered.

weight=float(input("please enter your weight in kg:"))                                         # store the weight of the person in kg.
while weight<=20 or weight>=80:                                                                # if the weight is less than or equal to 20 or greater than or equal to 80, print an error message.
    print("Error: weight must be greater than 20 and less than 80.")
    weight=float(input("please enter your weight in kg:"))                                     # ask the user to enter the weight again until a valid weight is entered.

gender=input("please enter your gender (male or female):")                                     # store the gender of the person.
while gender!="male" and gender!="female":                                                     # if the gender is not male or female, print an error message.
    print("Error: please enter a valid gender (male or female).")
    gender=input("please enter your gender (male or female):")                                 # ask the user to enter the gender again until a valid gender is entered.

Cr=float(input("please enter the creatine concentration in blood in µmol/l:"))                 # store the creatine concentration in blood in µmol/l.
while Cr<=0 or Cr>=100:                                                                        # if the creatine concentration is less than or equal to 0 or greater than or equal to 100, print an error message.
    print("Error: creatine concentration must be greater than 0 and less than 100.")
    Cr=float(input("please enter the creatine concentration in blood in µmol/l:"))             # ask the user to enter the creatine concentration again until a valid creatine concentration is entered.

if gender=="male":                                                                             # if the person is male, calculate the creatine clearance using the formula for males.
        CrCl=(140-age)*weight/(72*Cr)                                                          # calculate the creatine clearance in µmol/l.
elif gender=="female":                                                                         # if the person is female, calculate the creatine clearance using the formula for females.
        CrCl=(140-age)*weight/(72*Cr)*0.85                                                     # calculate the creatine clearance in µmol/l.
print("The creatine clearance is " + str(CrCl) + "µmol/l.")                                    # print the creatine clearance in µmol/l.
    



