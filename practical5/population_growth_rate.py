import matplotlib.pyplot as plt

# Population data (millions)
population_2020 = {
    'UK': 66.7,
    'China': 1426,
    'Italy': 59.4,
    'Brazil': 208.6,
    'USA': 331.6
}

population_2024 = {
    'UK': 69.2,
    'China': 1410,
    'Italy': 58.9,
    'Brazil': 212.0,
    'USA': 340.1
}

# Calculate percentage change
population_change = {}

for country in population_2020:
    change = ((population_2024[country] - population_2020[country]) / population_2020[country]) * 100
    population_change[country] = change

# Print percentage change for each country
print("Percentage population change for each country:")
for country, change in population_change.items():
    print(country, ":", round(change, 2), "%")

# Sort from largest increase to largest decrease
sorted_changes = sorted(population_change.items(), key=lambda x: x[1], reverse=True)

print("\nPopulation changes in descending order:")
for country, change in sorted_changes:
    print(country, ":", round(change, 2), "%")

# Identify largest increase and decrease
largest_increase = sorted_changes[0]
largest_decrease = sorted_changes[-1]

print("\nCountry with the largest increase:", largest_increase[0], "(", round(largest_increase[1], 2), "%)")
print("Country with the largest decrease:", largest_decrease[0], "(", round(largest_decrease[1], 2), "%)")

# Bar chart
countries = list(population_change.keys())
changes = list(population_change.values())

plt.bar(countries, changes)
plt.title("Population Change by Country (2020 to 2024)")
plt.xlabel("Country")
plt.ylabel("Percentage Change (%)")
plt.axhline(0)
plt.show()
