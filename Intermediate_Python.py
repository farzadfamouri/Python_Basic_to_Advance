# I am uploading these scripts for my future reference.
# Starting with basic functions, I will gradually develop more advanced scripts (I have an ML approach)
# These will be uploaded to my GitHub for personal use only.
# Thank you for your attention.

# Visualization - Data Structure - Control Structures

# Data Visualization: 1- Explore Data 2- Report Insights
# The mother of all visualization libraries is Matplotlib!!!
#------------------------------------------------------------Scatter and Linear --------------------------------------->
import matplotlib.pyplot as plt
year = [1950, 1970, 1990, 2010]
pop = [2.5, 3.7, 5.2 , 6.9]

# with lines
#plt.plot(year, pop)
# with dots
"""
S = [10,1,3,7] 
plt.scatter(year, pop, S) # controls the size of each marker, 
#potentially representing population size or some other metric.

# How to make it logarithmic scale:
plt.xscale('log')
plt.show()"""

# -------------------------------------------------------Histogram----------------------------------------------------->
# Explore and idea about distribution
# it makes some range by having bins like 0-2 2-4 4-6 ....

values = [0,0,1.4,22,11,12,13,13,15,6,7,19,25,1,1 ]
S = [40,10,33,75]
#plt.hist(values, bins =10)
#plt.scatter(year, pop, S, alpha=0.5) # s for dot size, alpha for transparency
#plt.xlabel('x')
#plt.ylabel('y')
#plt.title('histogram')
#plt.yticks([-2, 0, 5, 12], ["-2B", "0", "5B", "12B"])
#plt.text(1950,2.5, "Start")
#plt.text(2010,6.5, "End")
#plt.grid(True)
#plt.show()


# -------------------------------------------------------- Dictionary ------------------------------------------------->

# Not intuitive and Not convinient and we have digit and string for that digit:

world = {"iran": 90, "canada": 40, "USA": 400}
print("Dictionary defined: ", world)
print(world["iran"])
print(world.keys())

# keys in the dictionary should be immutable (unchangeable), SO LIST CAN"T BE KEY

# The way to add item to dic:

world["England"] = 80
print("Dictionary after adding a value: ", world)

print("England" in world)
del(world['iran'])
print("After del iran from dic: ", world)



#---------------------------------------Dictionary inside a dictionary:

europe = { 'spain': { 'capital':'madrid', 'population':46.77, 'flag': 'blue'},
           'france': { 'capital':'paris', 'population':66.03, 'flag': 'red'},
           'germany': { 'capital':'berlin', 'population':80.62, 'flag': 'gray'},
           'norway': { 'capital':'oslo', 'population':5.084, 'flag': 'red'}}


# Print out the capital of France

print(europe['france']["capital"])

#---------------------------------------------------------------Pandas------------------------------------------------->

# rectangular data structure like 2D numpy array! but all data should be same type like str or int so Pandas is the best

# Pandas: High level data manipulation tool! ( by Wes McKinney) it is built on NumPy

# Data be saved on DataFrame

# to create DataFrame we need to use dictionary! : 1-Keys (column lables) 2- values (data, column by column)

import pandas as pd

brics = pd.DataFrame(europe)

print(type(brics))
print(brics.shape)

brics.index = ["CAPITAL: ", "Population: ", "FLAG"]

print(brics)

# import:

# brics = pd.read_csv("path", index_col=0)

print(type(brics["spain"]))

# type of one column of a DataFrame is series like 1D laballed array but now:

print(type(brics[["spain"]]))

#-------------------DataFrame Slice------------------------------------------------------------------------------------:
# 1. based on the row slicing
print("Slice by row: ", brics[1:2])
print("Type: ", type(brics[1:]))

#OR -------------------------------------------------loc and iloc------>

print("OR: ", brics.loc[['Population: ']]) # Notice this is showing the row not a column!
# in other words:
print(brics.loc[["Population: "], :])

#OR with Iloc and index instead of the name
print("OR: ", brics.iloc[[1]])
# in other words:
print(brics.iloc[[1], :])
#----------------------------------------------------------------------->
# 2. based on the column slicing
print("Column but as series: ", brics["spain"])
print( "Type: ", type(brics["spain"]))
# type of one column of a DataFrame is series like 1D laballed array but now:
print("Column but as a DataFrame: ", brics[["spain"]])
print("Type: ",type(brics[["spain"]]))

# The best way is with loc and iloc!



#--------------------------------------NumPy Boolean Operators -------------------------------------------------------->

# np.logical_and() - logical_or() - logical_not() / for NUmPy 2D array, we can't use regular operations!


# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10

print(np.logical_or(my_house>18.5, my_house<10))
# Both my_house and your_house smaller than 11

print(np.logical_and(my_house<11, your_house<11))

#------------------------------------------------------------------------------------------------------------Conditions:
# Summary: # comparison operators: < , > , ==, !=
# Booleam Operators: and, or,not
# Conditional Statements: if, else, elif

# ------------------------------------------Filtering Pandas DataFrame--------------------------------------------------
import numpy as np
print("Now time for Pandas filtering: ")

print("The Pandas DataFrame Example: ", brics)
print("The column chosen: ", brics["spain"])
cut = np.logical_or(brics["spain"] == "blue", brics["spain"] == 46.77)
print("cut:", cut)
brics_cut = brics[cut]
print('cut dataframe without capital:', brics_cut, "vs.original: ", brics)

# -----------------------------------------------------------------------------------------------------------While & For

#---------------------------------------------------------while:
error  = 50
i=0
while error > 1:
    error = error /4
    print(i)
    i+=1

#----------------------------------------------------------for:

for v in values:
    print(v)

# In Python, enumerate() is a built-in function that is used to iterate over a sequence (like a list or tuple)
# and get both the index and the value of each item.
# It is commonly used in loops to access both the index and the value of elements in a collection.

#---------------------- for over list:
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

#-------------------- loop over string:

for c in "family":
    print(c.capitalize())
#-------------loop over data structures:

# loop over dictionaries and 2D NumPy arrays: (For Dictionary .item() method and for the 2D array np.nditer() function

# Dictionary: items() method!
for a, b in europe.items():
    print(a, b)

# Numpy array, 1D:

import numpy as np

np_height = np.array([1.73, 1.8, 1.9, 2, 2.3])
for v in np_height:
    print("height: ", v)

# numpy 2D: # np.nditer() function to see each elemnt in the 2D array!



np_weight = np.array([65, 78, 89, 87, 120])

np_2D = np.array([np_height, np_weight])

for i in np.nditer(np_2D):
    print("To see each element inside the 2D array: ", i)


# ----------------------------Dictionary loop:

world2 = { 'BR': {'country': 'Brazil', 'capital':'madrid', 'population':46.77, 'flag': 'blue'},
           'FR': {'country': 'France', 'capital':'paris', 'population':66.03, 'flag': 'red'},
           'GR': {'country': 'Germany', 'capital':'berlin', 'population':80.62, 'flag': 'gray'},
           'NW': {'country': 'Norway', 'capital':'oslo', 'population':5.084, 'flag': 'red'}}

brics2 = pd.DataFrame(world2)
print("New Dictionary: ", brics2)
print("New Dictionary shape: ", brics2.shape)
print("New Dictionary keys:(column headers) ", brics2.keys())

# The simple loop, it will only print the headers(keys):
for i in brics2:
    print(i) # here only prints column headers

# Now, we want to itterate over the rows:  (iterrows() method!) it make each row as a series!

for i, j in brics2.iterrows():
    print(i) # here only prints row headers
    print(j) # print columns info

# Now, imagine we only want to print the Germany info:(only one column)

for i, j in brics2.iterrows():
    print(j["GR"]) # notice because each j is a series, it shows column info

# Now, we want to add a new column new country as same as Germany

for i, j in brics2.iterrows():
    brics2.loc[i, "GR2"] = j["GR"] # add new columns with header's name: "GR2"

print("Updated Pandas DataFrame: ", brics2)


#  OR:
def my_function(x):
    return x + x

# apply function is for vectorized functions like what I did here:
brics2["GR3"] = brics2["GR"].apply(my_function)
print(brics2)

# ------------------------------------------------------- hacker statistics ------------------------------------------->

# ---------------------------------Random generators:
print("random1: ",np.random.rand())
print("random2: ",np.random.rand())
np.random.seed(123)

# setting seed to a specific number, you can find the exact random numbers for the repetition numbers:
# to ensures reproducibility
print(np.random.rand())

np.random.seed(123)
for i in range(10):
    print(np.random.randint(0, 2))# randomly generate 0 , 1


# Random Step / Random Walk: 1.Path of molecules 2. Gambler's financial status

np.random.seed(123)
outcome = []
for i in range(10):
    coin = np.random.randint(0,2)
    if coin ==0:
        outcome.append("heads")
    if coin == 1:
        outcome.append("tails")

print(outcome)


np.random.seed(123)
outcome2 = [0]
for i in range(10):
    coin = np.random.randint(0,2)
    outcome2.append(outcome2[i] + coin)

print(outcome2)


#-------------------------------- Random walk visualization:

# Initialization

np.random.seed(123)
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot random_walk
#plt.plot(random_walk)

# Show the plot
#plt.show()


# ------------------------------------------------------Distribution--------------------------------------------------->

np.random.seed(123)

final_tails = []

for x in range(1000):
    tails = [0]
    for y in range(10):
        coin = np.random.randint(0,2)
        tails.append(tails[y] + coin)
    final_tails.append(tails[-1])
plt.hist(final_tails, bins =10)
plt.show()

# How to clear a plot:
plt.clf()
