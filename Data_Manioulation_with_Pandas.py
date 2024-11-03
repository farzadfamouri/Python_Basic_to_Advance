# Manipulation + Visualization:

# DataFrames + Aggregating Data + Slicing and Indexing Data + Creating and visuallizing

# Pandas is made on NumPy and Matplotlib

# NumPy provide multidimensional array objects

# Pandas DataFrame : Rectangular data or tabular data VS SQL tabase tables!

# In Pandas DataFrame, each column data type can be different from othe column type


world2 = { 'BR': {'country': 'Brazil', 'capital':'madrid', 'population':46.77, 'flag': 'blue'},
           'FR': {'country': 'France', 'capital':'paris', 'population':66.03, 'flag': 'red'},
           'GR_w': {'country': 'Germany_west', 'capital':'berlin', 'population':80.62, 'flag': 'gray'},
           'NW': {'country': 'Norway', 'capital':'oslo', 'population':5.084, 'flag': 'red'},
           "NW2": {'country': 'Norway2', 'capital':'oslo', 'population':6.084, 'flag': 'red'},
           'GR_e': {'country': 'Germany East', 'capital':'berlin', 'population':78, 'flag': 'gray_white'}}

import pandas as pd

data = pd.DataFrame(world2).T
print("Shape of the data: ", data.shape) #attribute
print("Data: ", data)
print("column headers: ", data.columns) #attribute
print("Two first rows: ", data.head(2)) #method
print(data.info()) #method
print(data.describe()) #method
print(data.values) #attribute
print(data.index) #attribute
# Sorting DayaFrame---------------------------------------->

print(data.sort_values("country", ascending=False)) # if True descending
print(data.sort_values(["country", "capital"], ascending= [True, False]))

# Subsetting ---------------------------------------------->
print(type(data["country"]))
print(type(data[["country", "capital"]]))
# How to subset with condition:
print(data[data['population'] > 50.0])
print(data[data["capital"] == "paris"])
# More than two conditions:
is_flag = data["flag"] == "red"  # Create a boolean mask for flags that are "red"
is_pop = data["population"] < 70  # Create a boolean mask for population < 70
print(data[is_pop & is_flag])  # Apply both conditions

# isin() method-------------------------------------------->
print(data[data["capital"].isin(['paris', 'berlin'])])

# Addiding a new column from old columns ------------------>

data["population_k"] = data["population"] / 100

print(data)

# Summary Statistics:

print("mean: ", data["population"].mean())
# other methods: .mode() .max(), .min(), .median() , .var(), .std(),
# .sum() .quantile() (charak) .cumsum() (cumulative sum), .cummax() , .cummin() , .cumprod()

# .agg() method

def pct30(column):
    return column.quantile(0.3)

print("Aggregate function: ", data['population'].agg(pct30))

def min_value(column):
    return column.min()

print("Aggregate function and min function: ", data['population'].agg([pct30, min_value]))

#----------------------------Counting---------------------------------------------------------------------------------->
# .drop_duplicates() method! ------------>

print("data before deleting doublication: ", data)
print("after removing: (we are going to lose one of the germany because they share the capital)", data.drop_duplicates(subset="capital"))
print('with more than two criteria:(both germany will remain in the list) ', data.drop_duplicates(['capital', 'population']))

# .value_counts() method
print("Count countries: ", data['country'].value_counts(sort=True))
print("Count capitals: ", data['capital'].value_counts(sort=True))
print("Percentage : ", data['capital'].value_counts(normalize=True))

# Grouped By method --------groupby()---------------------------------------------------------------------------------->

print(data.groupby("capital")["population"].sum()) # it says, group them by their capital and then take the summation of
# their population seprately and return in dataFrame!

# sometime, you need to use python's built_in functions like sum(), when you are using the Pandas library

print("Python sum built_in function: ", sum(data.groupby("capital")["population"].sum()))

# for more aggregate functions:

print(data.groupby("capital")["population"].agg(['sum', 'max', 'min']))

print(data.groupby(["country", "capital"])["population"].agg(['sum', 'max', 'min']))



# ---------------------------- Pivot tables --------------------------------------------------------------------------->

# Similar to groupby!
# Pivot table by defult calculate the mean

print("Pivot Table Example: ", data.pivot_table(values = "population", index="capital"))
import numpy as np
print("Pivot Table Example: ", data.pivot_table(values = "population", index="capital", aggfunc="max"))
# columns="flag", fill_value=0 can be added

# ---------------------------- Explicit indexes ----------------------------------------------------------------------->

# DataFrame composed three parts: NumPy array for the data and two indexes: row and column details
print("DataFrame columns: ", data.columns)
print("DataFrame index: ", data.index)
""" bullshit
data["new"] = range(len(data))  # Add a new column with index values
data_new_index = data.set_index("new")
print(data_new_index)
data.new_index.reset_index()
print(data_new_index)"""

# the easiest way to subset with index
# intersect by column (look at previous course)
print(data[data["country"].isin(["Norway"])])
# intersect by row(look at the previous course)
print(data.loc[["NW"]])
#print(data.sort_index())

# since my dataset was single index, I want to make it multi index:
data_multi = data.set_index(["country", "capital"])
print(data)
print(data_multi)
print(data_multi.loc[["France"]])
#print(data_multi.sort_index(level=["country", "capital"], ascending=[True, False]))

# -------------------------------- Slicing and Subsetting with .loc and .iloc ----------------------------------------->
# Technique for selecting consecutive (in order) elements from objects

#-------------------------------------------Slicing LIST

breeds = ["A", "B", "C", "D", "E", "F", "G"] # list
print("Slicing the list (note that the last element wouldn't be included): ", breeds[1:3])

#---------------------------------------Slicing DataFrame

#------------------------------------------ Slicing rows
print("Before sorting: ", data_multi)

# sorting is necessary

data_multi = data_multi.sort_index()

print("After sorting: ", data_multi)
print(data_multi.loc["Germany_East":"Norway2"]) # the same technique doesn't work for inner index level

# there are two differences with list slicing:
# 1. the end value is included
# 2. the index should be sorted and determined

print("For inner index level use tuples: ", data_multi.loc[("Germany_west, berlin"):("Norway2", "oslo")])

# ----------------------------------------Slicing columns

print(data_multi.loc[:, "population"])


# -------------------------------Slicing rows and columns

print(data_multi.loc[("France", "paris"):("Norway", "oslo"), "population"])

# ------------Advantage of slicing for dates and numbers

data_multi = data_multi.reset_index()

data_multi = data_multi.set_index("population").sort_index()

print(data_multi)

print(data_multi.loc[66.03: 80.62])

# FOR Iloc:

print(data_multi.iloc[1:3, 1:2])



# ------------------------------------------Workinh with pivot table--------------------------------------------------->

# first argument, column to aggregate, second one is index, the third one
data_pivot = data.pivot_table("population", index="country", columns="capital")

print("Pivot table: ", data_pivot)

print("Sectioning pivot table by loc: ", data_pivot.loc["Brazil":"Germany_East"])

# The methods used in DataFrame, such as mean, have an axis argument!

print("Aggregate functions in pivot: ", data_pivot.mean(axis="index"))
print("Aggregate functions in pivot: ", data_pivot.mean(axis="columns"))



#----------------------------------------------------------------Visualization----------------------------------------->
import matplotlib.pyplot as plt

dog = {
    "sp1": ["A1", "A2", "A3", "A4", "A5", "A6", "A1"],  # Grouped values in a list
    "height": [12, 24, 43, 11, 7, 56, 100],      # Grouped values in a list
    "weight": [2, 4, 4, 11, 7, 12, 20],
    "sex": ["f", "m", "m", "f", "m", "f", "f"]
}

import pandas as pd
dog_dataframe = pd.DataFrame(dog)
dog_dataframe["height"].hist(bins=3)
plt.show()

avg_dog_weight = dog_dataframe.groupby("sp1").mean(numeric_only=True)
print(avg_dog_weight)

avg_dog_weight.plot(kind="bar", title = "Graph")
plt.show()

dog_dataframe["weight"].plot(x="X", y= "Y", kind ="line", rot =45)
plt.show()

dog_dataframe.plot(x="weight", y="height", kind="scatter", title="Scatter Plot of Weight vs Height")
plt.xlabel("Weight")
plt.ylabel("Height")
plt.show()

# Separate histograms for 'height' by 'sex'
dog_dataframe[dog_dataframe["sex"] == "f"]["height"].hist(alpha=0.5, label="Female")
dog_dataframe[dog_dataframe["sex"] == "m"]["height"].hist(alpha=0.5, label="Male")
plt.xlabel("Height")
plt.ylabel("Frequency")
plt.title("Histogram of Heights by Sex")
plt.legend()
plt.show()

# Missing Values:

print(dog_dataframe.isna()) # all data in dataset
print(dog_dataframe.isna().any()) # columns in dataset
print(dog_dataframe.isna().sum()) # summation of missing values in each column
dog_dataframe.isna().sum().plot(kind="bar") # we can visualize them as well
plt.show()

# How can we treat:

dog2 = {
    "sp1": ["A1", "A2", "A3", "A4", "A5", "A6", "A1", "A2"],  # Grouped values in a list
    "height": [12, 24, 43, 11, 7, 56, 100, None],      # Grouped values in a list
    "weight": [2, 4, 4, 11, 7, 12, 20, None],
    "sex": ["f", "m", "m", "f", "m", "f", "f", "m"]
}

print("Key in a dictionary", dog2["sp1"])


dog_dataframe2 = pd.DataFrame(dog2)
print(dog_dataframe2.isna().sum())
# remove them:

dog_dataframe2_edited= dog_dataframe2.dropna()

print(dog_dataframe2_edited)

## replacing missing values:

dog_dataframe2_edited2 = dog_dataframe2.fillna(0)
print(dog_dataframe2_edited2)

# Two ways to create dictionariesL:   1. From lis of dictionaries - row by row 2. Dictionary of lists - column by column

# Row by row:

dic_list = [
    {"name": "A", "family": "a", "nickname":"Aa"},
{"name": "B", "family": "b", "nickname":"Bb"},
{"name": "C", "family": "c", "nickname":"Cc"}
]

dic_dataframe = pd.DataFrame(dic_list)
print("Row by row dictionary: ", dic_dataframe)

# COlumn by column

dic2 = {
    "name": ["A", "B", "C"],
    "family": ["a", "b", "c"],
    "nickname": ["Aa", "Bb", "Cc"]
}
dic_dataframe2 = pd.DataFrame(dic2)
print("Row by row dictionary: ", dic_dataframe2)