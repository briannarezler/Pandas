import pandas as pd

grades = pd.Series([87, 100, 94])

# print(grades)

same_grade = pd.Series(98.6, range(3))

# print(same_grade)

# 0  98.6
# 1  98.6
# 2  98.6
#dtype: float64

# print(grades[0])
grades.count()
grades.mean()
grades.min()
grades.max()
grades.std()

# print(grades.describe())

# You can specify custom indices with
#grades = pd.Series([87, 100, 94], indexes=["wally", "Eva", "Sam"])

# print(grades)

# If you initialize a series with a dictionary, its keys become
# the series' indices, and its values become the series' element values:

grades = pd.Series({'Wally': 87, "Eva": 100, "Sam": 94})

# You can access individual elements via square brackets containing a
# custom index value
grades['Eva']
# 100

# print(grades.Wally)

# print(grades.dtype)

# print(grades.values)


grades.values
# array([87,100,94])

# Series of strings
hardware = pd.Series(["Hammer", "Saw", "Wrench"])

""" 
    0 Hammer
    1 Saw
    2 Wrench
    dtype: object 
"""

answer = hardware.str.contains('a')

print(answer)

hardware_upper = hardware.str.upper()

print(hardware_upper)
