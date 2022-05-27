# figures to display within notebook
#%%

# imports of pip installed libraries
from ast import increment_lineno
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# this only works in Jupyter Notebook
# %matplotlib inline

#%%
# data url from my public github
url = "https://raw.githubusercontent.com/empathy87/The-Elements-of-Statistical-Learning-Python-Notebooks/master/data/mixture.txt"
# read csv file using pandas extension, seperate data by comma.
raw_data = pd.read_csv(url, sep=",")
raw_data.head()

#%%
raw_data.shape
raw_data.dtypes
raw_data.isnull().sum()
raw_data.columns

# %%
temp = pd.DataFrame({
    "Midterm": [100, 90, 80],
    "Final": [80, 90, 100],
    "Grade": ['A', np.nan, 'A']
})
temp
temp.isnull().sum()

# %%
numeric_cols = ['x1','x2']
raw_data[numeric_cols].hist()


# %%
raw_data[numeric_cols].describe()

# %%
raw_data['y'].value_counts()
raw_data['y'].value_counts().plot.bar()

# %%
# Plot data as points on a 2D plane
blue_pts = raw_data[raw_data['y'] == 0]
red_pts = raw_data[raw_data['y'] == 1]
plt.plot(blue_pts['x1'], blue_pts['x2'], 'b.', label='y = 0')
plt.plot(red_pts['x1'], red_pts['x2'], 'r.', label='y = 1')
plt.title('Visualization of Data Set')
plt.xlabel('x1')
plt.ylabel('x2')
plt.legend(loc='lower left')
plt.show()

# save the image in google temp folder (folder icon at left side)
plt.savefig('Week3Fig.png')
# %%
# Import Library

import matplotlib.pyplot as plt
import numpy as np

# Define Data Coordinate

x = np.linspace(0,15,150)
y = np.sin(x)

# Plot

plt.plot(x,y)

# Display


plt.show()
# %%
