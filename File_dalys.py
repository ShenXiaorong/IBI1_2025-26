import os
import pandas as pd # type: ignore
import matplotlib.pyplot as plt
import numpy as np
dalys_data=pd.read_csv('dalys-rate-from-all-causes.csv')
first_10 = dalys_data.iloc[0:10, 2:4]
print(first_10)
print(first_10.describe())
# Across the first 10 years recorded for Afghanistan, the maximum DALYs were recorded in: 1998.

zimbabwe_rows = dalys_data["Entity"] == "Zimbabwe"
zimbabwe_years = dalys_data.loc[zimbabwe_rows, "Year"]
print("Years for Zimbabwe:")
print(zimbabwe_years)
first_year=zimbabwe_years.min()
last_year=zimbabwe_years.max()
print(f"The first year is {first_year}, the last year is {last_year}")
# For Zimbabwe, DALYs were recorded from 1990 to 2019.

recent_data = dalys_data.loc[dalys_data["Year"] == 2019, ["Entity", "DALYs"]]
max_country = recent_data.loc[recent_data["DALYs"].idxmax()]
min_country = recent_data.loc[recent_data["DALYs"].idxmin()]

print("Country with maximum DALYs in 2019:", max_country["Entity"])
print("Country with minimum DALYs in 2019:", min_country["Entity"])

# The country with the maximum DALYs in 2019 was: Lesotho.
# The country with the minimum DALYs in 2019 was: Singapore.


country_name = max_country["Entity"]
country_data = dalys_data.loc[dalys_data["Entity"] == country_name]

plt.figure()
plt.plot(country_data["Year"], country_data["DALYs"], "bo-")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title("DALYs over time in " + country_name)
plt.xticks(country_data["Year"], rotation=-90)
plt.tight_layout()
plt.show()

# Question: How has the relationship between the DALYs in China and the UK changed over time? Are they becoming more similar or less similar?
china_data = dalys_data.loc[dalys_data["Entity"] == "China"]
uk_data = dalys_data.loc[dalys_data["Entity"] == "United Kingdom"]

china_data = china_data.rename(columns={"DALYs": "China_DALYs"})
uk_data = uk_data.rename(columns={"DALYs": "UK_DALYs"})
merged_data = pd.merge(china_data[["Year", "China_DALYs"]], uk_data[["Year", "UK_DALYs"]], on="Year", how="inner")
merged_data["Difference"] = merged_data["China_DALYs"] - merged_data["UK_DALYs"]

# plot DALYs over time
plt.figure(figsize=(8, 5))
plt.plot(merged_data["Year"], merged_data["China_DALYs"], label="China")
plt.plot(merged_data["Year"], merged_data["UK_DALYs"], label="United Kingdom")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title("DALYs in China and the UK over time")
plt.legend()
plt.show()

# plot difference over time
plt.figure(figsize=(8, 5))
plt.plot(merged_data["Year"], merged_data["Difference"])
plt.xlabel("Year")
plt.ylabel("Absolute difference in DALYs")
plt.title("Difference in DALYs between China and the UK over time")
plt.show()

# print summary
print(merged_data[["Year", "China_DALYs", "UK_DALYs", "Difference"]])
