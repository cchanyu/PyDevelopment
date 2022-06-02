'''
Name: Chanyu Choung

Class: CMP414

Homework due date: Feb 17th, 2021 (Wednesday)

Week 2 Homework
Build a linear model (height = m * year + b) to describe the trend of height increase for United Kingdom between 1900 and 1980. Compute the mean square error of your model, and display the model line together with the data points.

Linear model: (height=m⋅year+b) (y = mx + b)
Metric on closeness: mean squared error (MSE):
MSE=1number of data∑(x, y) in dataset(mx+b−y)2
'''

# %%
import numpy as np  # scientific computation
import pandas as pd  # data handling
import matplotlib.pyplot as plt  # plotting

# The following "magic command" allows figures to be displayed automatically in notebook
# %matplotlib inline
url = "https://raw.githubusercontent.com/cchanyu/MachineLearning/main/SheetData/average-height-of-men-for-selected-countries.csv"
raw_data = pd.read_csv(url, sep=',')

# %%
# Filtering the dataset
filter = (raw_data["Entity"] == "United Kingdom") & (raw_data['Year'] >= 1900)
data = raw_data[filter]

# Cleaning the dataset
data = data.set_index(["Year"]) # Setting year tab as index tab
data.drop(['Entity', 'Code'], axis=1, inplace=True) # Deleting Entity and Code tab
data = data.rename(columns={'Human Height (University of Tuebingen (2015))': "Height(cm)"}) # Renaming Heights tab

# Displaying the dataset
print(data.head(10))
heights = data['Height(cm)']
years = data.index
plt.plot(years, heights, 'g.')

# %%
m2 = 0.0925
b2 = -5.25

# Finding the value of M
m = (176.8 - 169.4) / (1980 - 1900)
print("Slope(m)(RED):", m)
print("Slope(m)(BLUE):", m2)

# Finding the value of B
height = 169.4
year = 1900
b = height - m * year
print("Y-Intercept(b)(RED):", b)
print("Y-Intercept(b)(BLUE):", b2)

# plot the new model
years = np.array([1900,1980])
heights = m * years + b

plt.plot(years, heights, 'r-')
plt.plot(data.index, data['Height(cm)'],'g.')

# plot the second line on this graph
heights2 = m2 * years + b2
plt.plot(years, heights2, 'b-')

# %%
# Calculate errors for each year
errors = []
errors2 = []

for year in data.index:
    # For the data point:
    x = year
    y = data.loc[x, 'Height(cm)']

    # Calculate the squared error for that year
    prediction = m * x + b
    error = (prediction - y) ** 2
    prediction2 = m2 * x + b2
    error2 = (prediction2 - y) ** 2

    # append the error to the error list
    errors.append(error)
    errors2.append(error2)

# Now you should have a list of errors.
print("List of Errors(RED):",errors)
print("List of Errors(BLUE):",errors2)

# Calculate the mean squared error, use np.mean() function
print("Mean Squared Error(RED):",np.mean(errors))
print("Mean Squared Error(BLUE):",np.mean(errors2))

# %%
