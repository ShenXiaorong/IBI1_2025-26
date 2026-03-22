heart_rates=[72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]
print('The number of patients is:', len(heart_rates))
print('The average heart rate is:', sum(heart_rates) / len(heart_rates))
Low=0
Normal=0
High=0
for rate in heart_rates:
    if rate < 60:
        Low += 1
    elif 60 <= rate <= 120:
        Normal += 1
    else:
        High += 1
print('Number of patients with low heart rate:', Low)
print('Number of patients with normal heart rate:', Normal)
print('Number of patients with high heart rate:', High)
if Low > Normal and Low > High:
    largest = "Low"
elif Normal > Low and Normal > High:
    largest = "Normal"
elif High > Low and High > Normal:
    largest = "High"
elif Low == Normal == High:
    largest = "There is a tie between categories"
elif Low == Normal and Low > High:
    largest = "Low and Normal are tied"
elif Low == High and Low > Normal:
    largest = "Low and High are tied"
elif Normal == High and Normal > Low:
    largest = "Normal and High are tied"
print("The category with the largest number of patients is:", largest)
# Pie chart
import matplotlib.pyplot as plt
labels = ["Low", "Normal", "High"]
sizes = [Low, Normal, High]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Heart Rate Categories")
plt.show()
