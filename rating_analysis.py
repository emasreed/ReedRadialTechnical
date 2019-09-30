import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

with open("Hospital General Information.csv") as csv_file:
    input_file = pd.read_csv(csv_file)

for col in input_file.columns:
    print(col)

np.random.seed(19680801)

# fake up some data
spread = np.random.rand(50) * 100
center = np.ones(25) * 50
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100
data = np.concatenate((spread, center, flier_high, flier_low))
print(data.dtype)

input_file['Hospital overall rating'] = pd.to_numeric(input_file['Hospital overall rating'],
                                                      errors='coerce')

input_file=input_file.dropna(subset=['Hospital overall rating', 'Mortality national comparison', 'Readmission national comparison'])
print(input_file['Mortality national comparison'].head())

below_df = input_file.loc[input_file['Mortality national comparison'].str.contains('Below the national average')]
same_df = input_file.loc[input_file['Mortality national comparison'].str.contains('Same as the national average')]
above_df = input_file.loc[input_file['Mortality national comparison'].str.contains('Above the national average')]
data=[below_df['Hospital overall rating'], same_df['Hospital overall rating'], above_df['Hospital overall rating']]

fig, ax = plt.subplots()
ax.boxplot(data)


ax.set(xlabel='Comparison to National Average', ylabel='Rating',
       title='Mortality National Comparison')
ax.grid()

fig.savefig("Mortality.png")
plt.show()


below_df = input_file.loc[input_file['Readmission national comparison'].str.contains('Below the national average')]
same_df = input_file.loc[input_file['Readmission national comparison'].str.contains('Same as the national average')]
above_df = input_file.loc[input_file['Readmission national comparison'].str.contains('Above the national average')]
data=[below_df['Hospital overall rating'], same_df['Hospital overall rating'], above_df['Hospital overall rating']]

fig, ax = plt.subplots()
ax.boxplot(data)


ax.set(xlabel='Comparison to National Average', ylabel='Rating',
       title='Readmission National Comparison')
ax.grid()

fig.savefig("Readmission.png")
plt.show()