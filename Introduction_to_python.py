# I am uploading these scripts for my future reference.
# Starting with basic functions, I will gradually develop more advanced scripts (I have an ML approach)
# These will be uploaded to my GitHub for personal use only.
# Thank you for your attention.

# Advantage: •	Open Source, Free, Packages (For data science): different applications and fields



# The very basic function---------------------------------------------------------------------------------------> print:
# Addition
print(4+5)
# Subtraction
print(5-5)
# Multiplication
print(3*5)
# Division
print(10/2)

#-----------------------------------------------------------------------------------------------------------> variables:
A = 100

half = 0.5

intro = "Hello! How are you?"

is_good = True
print("A variable type: ", type(A))
print("half variable type: ", type(half))
print("intro variable type: ", type(intro))
print("is_good variable type: ", type(is_good))

double_intro = intro + intro
print("How to add two strings together: ", double_intro)

#----------------------------------------------------------------------------------------------> Python List: [a, b , C]
list_example = [1.73, 1.72, 1.83, 1.90]

# list can contain different types of values and even other sub_lists
list_different_values = ["farzad", 1.70, 2000, True, list_example]
print("List presentation: ", list_different_values)
print("List type: ", type(list_different_values))

# to call list items, you need to use the index and index starts from 0.
print("index of a list: ",list_different_values[3]) # you can also use negative index

# we can also do list slicing:
print("range inside a list: ", list_different_values[0:2]) # [inclusive, exclusive]

# the way to read a list index inside another list:
print("index inside another list:", list_different_values[-1][1])

#--------------------------------------------------------------------------------------------------->Manipulating lists:

list_example[2] = 99999999999

print("list example after changes: ", list_example)


# notice this copying method, if you say x = y any change would be applied to both
x = [1,2,3]
y = x
y[2] = 0

print("new x: ", x, "y: ", y)

# to avoid this problem:

x = [1,2,3]
z = list(x)
# or z = x[:]
z[1] = 9

print("new x: ", x, "z: ", z)

test = [1, 20, 300]

test_ext = test + [4000]

print("test:", test, "test_ext: ", test_ext)

del test[2]
print("test after delete: ", test)

#---------------------------------------------------> Functions: 1. built_in like max() or type or peint() & 2. you code

print("example for round: ", round(2.88888, 3))
# if not specify the decimal, it will round to the digit so:
print("example for round without decimal specifying: ", round(2.88888))

print("example for max: ", max(test))

help(print)
print("sorted function example for test_ext: ", len(test_ext))
int()
print("pow function example ", pow(2, 3))
print("sorted function example for test: ", sorted(test, reverse=True))

#----------------------------------------------------------> Python Methods such as (kind of functions for the objects!)
# For the objets of str: capitslize(), replace(),
# For the objects of float: bit_length(), conjugate(),
# For the objetcs of list: index(), count()

print("Example of using methods for the object of list:", test.index(20))
print("Example of using methods for the object of list: ")
test.append(1000000)
print(test)
letter_like = "like"
print("Example of using methods for the object of string", letter_like.capitalize())
print("Example of using methods for the object of string", letter_like.replace("like", 'example'))

# for now only these packages are useful: NumPy, Matplotlib, scikit-learn

# ------------------------------------------------NumPy---------------------------------------------------------------->
# in python list there is a limitation in mathematical operations and speed so NumPy is preferred in data science:
# On Python List you can't do calculation!

# NumPy array is similar to python list
# do calculation on each array inside the numpy.array instead of python list

import numpy as np

np_weight = np.array([120, 80])
np_height = np.array([1.78, 1.78])

bmi = np_weight/np_height ** 2
print(bmi)

# remark: NumPy arrays contain only one type!!!

print("Numpy array type: ", type(np_height))

random_array = np.array([True, "farzad", 213])
print("Notice it made all array with different types be similar and string: ", random_array)

print(" np.array([120, 80]) + np.array([120, 80]) is different= ", np_weight + np_weight,

      " from list test[1, 20, 300] + list test[1, 20, 300] = :", test + test)


print("To check the numpy shape: ", np_weight.shape) #.shape is called attribute and it is different from methods

# for attribute there is no () like previous .shape and it shows more info about the data structure

# ---------------------------------2D Numpy shape----------------------------------->

two_d_shape = np.array([[1, 2, 3], [4, 5, 6]])
print("We want to see the 2D numpy shape: ", two_d_shape.shape)

print("how to access the array inside a numpy list: ", two_d_shape[1][0], "Or: ", two_d_shape[1,0])

# ---------------------------------Numpy Statistics----------------------------------->
# methods are drastically faster to enforce
print(np.average(np_weight))
print(np.median(np_height))
"""np.corrcoef() # correlation between data
np.std() # standard deviation
np.random.normal() # random number with normal distribution
np.column_stack() # attach two columns together!"""
