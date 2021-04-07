# Perform the following tasks with pandas Series:
import random
import pandas as pd

# Create a Series from the list [7, 11, 13, 17].
series1 = pd.Series([7, 11, 13, 17])

print("Series 1 \n", series1, "\n")

# Create a Series with five elements that are all 100.0.
series2 = pd.Series(100.0, range(5))

print("Series 2 \n", series2, "\n")

# Create a Series with 20 elements that are all random numbers in the range 0 to 100.
# Use method describe to produce the Series’ basic descriptive statistics.

series3 = pd.Series((random.randint(0, 100) for x in range(20)), range(20))

print("Series 3 \n", series3, "\n")

print(series3.describe(), "\n")

# Create a Series called temperatures of the floating-point values 98.6, 98.9, 100.2 and 97.9.
# Using the index keyword argument, specify the custom indices 'Julie', 'Charlie', 'Sam' and 'Andrea'.

temperatures = pd.Series([98.6, 98.9, 100.2, 97.9])

temperatures.index = ['Julie', 'Charlie', 'Sam', 'Andrea']

index = temperatures.index

print("Series 4 \n", temperatures, "\n")

# Form a dictionary from the names and values in Part (4), then use it to initialize a Series.

dictionary = temperatures.to_dict()
print("Series 5 \n", dictionary)

series5 = pd.Series(dictionary)
print(series5)
