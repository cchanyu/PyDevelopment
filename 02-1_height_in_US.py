'''
Week 2: First Machine Learning Example
Reading: Chapter 1. The Machine Learning Landscape

What is Machine Learning?
Machine Learning is the science of programming computers so they can perform certain task with knowledge learned from data.

Example: spam filter

Task: to flag spam for new emails
Data: existing emails with labels (either spam or non-spam)
Performance measure:
percentage of correctly labeled emails
percentage of a spam email being labeled correctly.
percentage of a non-spam email being labeled correctly.
Classification efficiency
...
Why Use Machine Learning?
Traditional approach for spam filter:

Choose features of spam emails manually: "4U", "credit card", "free", "amazing"
Write an program to detect exactly the features you chose
Test the program and modify the features until satisfactory
Drawbacks of traditional approach:

A large amount of features are needed - hard to maintain
Spammers may change their writing to avoid explicit rules: change "4U" to "For U".
For some complex problems, manually-engineered features are not good enough: hand-written digits
Machine Learning models:

Automatically learns which words and phrases are good predictors of spam.
Since the program is not a stack of explicit rules, it is much shorter, easier to maintain, and most likely more accurate.
With new training data, the Machine Learning model can update automatically to capture new indicators of spam emails.
What Machine Learning is great for:

Problems for which existing solutions require a lot of hand-tuning or long lists of rules: one Machine Learning algorithm can often simplify code and perform better.
Complex problems for which there is no good solution at all using a traditional approach: the best Machine Learning techniques can find a solution.
Fluctuating environments: a Machine Learning system can adapt to new data.
Large amount of data: With Machine Learning, computers process big data faster than human.
First Example: Men's Height in the United States
As an illustration of machine learning practice, let's consider the task of understanding the trend of American men's height in the 20th century. This project requires the following stages:

Data preparation
Data exploration
Model training
Model evaluation
Model application
1. Download Data
Go to website: https://ourworldindata.org/human-height
Find the interactive chart "Increase of human height over two centuries"
Click the "Download" tab, and download a CSV (comma-separated-values) file containing height data.
After downloading, you can open it a text editor to view its content.

2. Upload the CSV file to Google Colab
Click "Files" icon on the left column.
Click "Upload to session storage"
Upload the CSV file.
Afterwards, you should see the file listed in the files tab.
'''

#%%
# Bash command "!ls" will show the files

'''
3. Load Data into Python
Import numpy, pandas, and matplotlib.
Load the data as a DataFrame using the following statement: raw_data = pd.read_csv(filename, sep=',')
Now the data in the .csv file are loaded to the DataFrame raw_data. You can display its first 5 rows using raw_data.head().
'''

#%%
import numpy as np  # scientific computation
import pandas as pd  # data handling
import matplotlib.pyplot as plt  # plotting
# The following "magic command" allows figures to be displayed automatically in notebook

raw_data = pd.read_csv("average-height-of-men-for-selected-countries.csv", sep=',')
raw_data.head()

'''
DataFrame
Data frame is a way to store data in rectangular grids that can easily be overviewed. Each row of these grids corresponds to measurements or values of an instance, while each column is a vector containing data for a specific variable. A data frame's row may contain different types of values: numeric, character, logical, etc.

Data frames in Python come with the Pandas libarary, and they are defined as a two-dimensional labeled data structures with columns of potentially different types.

4. Extract US Data
Create a filter on the rows with condition "Entity = United States"
Use the filter to select rows related to US.
Create another filter with condition "Year >= 1900", and use it to filter the data.
Display the resulting data frame.
'''
# %%
filter1 = (raw_data['Entity'] == "United States")
print(filter1)

filter1 = (raw_data['Entity'] == "United States")
data = raw_data[filter1]
data

# You can combine the two steps in one statement
data = raw_data[raw_data['Entity'] == "United States"]
data.head()

# Exercise:
# Extract USA data since 1900.
filter1 = (data['Entity'] == "United States")
filter2 = (data["Year"] >= 1900)
data = data[filter1]
data = data[filter2]
data

# We can apply both conditions in one statement
# use bitwise operator: &(and), |(or), ~(not)
filter3 = (raw_data['Entity'] == "United States") & (raw_data['Year'] >= 1900)
data = raw_data[filter3]
data

'''
5. Clean the Dataset
Reset the index.
Remove Entity and Code column.
Give a proper name to height column
'''

# %%
data = data.set_index(["Year"])
data.head()

data.drop(['Entity', 'Code'], axis=1, inplace=True) 
# axis specifies row drop or column drop
# axis = 0 means row drop
# axis = 1 means column drop

# inplace determines whether the modification is done to the original data frame
# inplace = true means modifying the original data
# inplace = false means creates a new data for the modification
data.head()

# Example: drop the first row and keep the results as a new data frame
# data
data_new = data.drop([1900, 1910, 1920], axis=0, inplace=False)
data_new

data = data.rename(columns={'Human Height (University of Tuebingen (2015))': "Height(cm)"})
data.tail()

'''
6. Plot height vs. year
Extract the list of heights.
Extract the list of years.
Use plt.plot() to create a scatter plot.
'''

# %%
heights = data['Height(cm)']
years = data.index
plt.plot(years, heights, 'g.')

'''
How would you describe the trend?

Is there a trend?
Answer: Yes

Is the trend upward or downward?
Answer: Upward

It the trend consistent?
Answer: Yes, it's constant growth over time.

Conclusion: During the 20th century, US men's height increases at a steady rate.

7. Modeling
Since we haven't studied any modeling method yet, let's use our intuition to find a function that describes the relation between year and height.

Linear model (height=m⋅year+b) seems a good fit to the data.
What is a good value for m?
What is a good value for b?
Plot the line represented by the linear model
Create a list of x-coordinates using np.linspace
Calculate the corresponding y-coordinates
Use these two lists to plot the line.
'''

# %%
# Calculate the average increase per year between 1900 and 1980
# Two points (1900, 170.0) and (1980, 179.0)
# What is the slope?

m = (179 - 170) / (1980 - 1900)
print("Slope:", m)

# Let the slope be the average rate of increase.
# If the model is height = m * year + b, 
# find the value of b so that point (1900, 170.0) lies on the line.

height = 170
year = 1900
b = height - m * year
print("Y-Intercept:", b)

# Now our linear model is: height = 0.1125 * year - 43.75
# Plot the model line.
years = np.array([1900,1980])
heights = 0.1125 * years - 43.75

plt.plot(years, heights, 'r-')

# show the data points on this plot
plt.plot(data.index, data['Height(cm)'],'g.')

# Can you find another line that fits the model better?
m2 = 0.112
b2 = -42.2

plt.plot(years, heights, 'r-')
plt.plot(data.index, data['Height(cm)'],'g.')

# plot the second line on this graph
heights2 = m2 * years + b2
plt.plot(years, heights2, 'b-')

'''
8. Model Evaluation
Objective: find a linear model whose predictions are close to the actual values.
Metric on closeness: mean squared error (MSE):
MSE=1number of data∑(x, y) in dataset(mx+b−y)2 
Now that we have multiple model candidates, which one gives the smallest MSE?
'''

# %%
# Example: Calculate the error for 1930
m = 0.1125
b = -43.75

# For the data point about 1930:
x = 1930
y = 173.4

# Prediction of the model for 1930:
prediction = m * x + b
print("prediction for 1930:", prediction)

# Squared error for 1930:
error = (prediction - y) ** 2
print("Error for 1930:", error)

# Calculate errors for each year

# all the years are contained in data.index

errors = []
errors2 = []

for year in data.index:
    # Calculate the squared error for that year
    x = year
    y = data.loc[x, 'Height(cm)']
    prediction = m * x + b
    error = (prediction - y) ** 2
    prediction2 = m2 * x + b2
    error2 = (prediction2 - y) ** 2

    # append the error to the error list
    errors.append(error)
    errors2.append(error2)

# Now you should have a list of errors.
print(errors)
print(errors2)

# Calculate the mean squared error, use np.mean() function
print(np.mean(errors))

# The MSE should be evaluated relatively.
print(np.mean(errors2))

'''
9: Use the Model
What is your prediction on the average height in 1890?, 2000? 2050?
Check with the raw dataset and see if your 1890 prediction is close.
'''

# %%
# Calculate the model prediction for year = 1890

# height = m * year + b
# height = 0.1125 * year - 43.75

# What is the prediction for 1890?
height_prediction_1890 = 0.1125 * 1890 - 43.75
print(height_prediction_1890)

# Find the actual average height for year 1890.

raw_data[(raw_data['Entity'] == "United States") & (raw_data['Year'] == 1890)]