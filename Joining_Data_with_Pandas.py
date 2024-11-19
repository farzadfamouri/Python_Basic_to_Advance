import pandas as pd

# manipulate tables ---- mergin tables together------------------------------------------------------------------------>

# By table we mean DataFrame, by joining we mean mergin and joining

# Data = Chicago data portal dataset

# Defining DataFrame by list (row by row), each row is a dictionary itslef

dic_list = [
    {"name": "A", "family": "a", "nickname":"Aa"},
{"name": "B", "family": "b", "nickname":"Bb"},
{"name": "C", "family": "c", "nickname":"Cc"},
{"name": "E", "family": "e", "nickname":"Ea"},
{"name": "L", "family": "A", "nickname":"LA"}
]

dic_dataframe = pd.DataFrame(dic_list)
print("Row by row dictionary: ", dic_dataframe)
print("Shape of the table: ", dic_dataframe.shape)

# Column by column, we define one dictionary and convert to DataFrame later

dic2 = {
    "name": ["A", "B", "C", "D", "A"],
    "family": ["a2", "b2", "c2", "d2", "a22"],
    "family2": ["a", "b'", "c'", "d'", "a''"],
    "nickname2": ["Aa2", "Bb2", "Cc2", "Dd2", "Aa22"],
    "zip": [11, 12, 13, 14, None]
}
dic_dataframe2 = pd.DataFrame(dic2)
print("Row by row dictionary: ", dic_dataframe2)
print("Shape of the table: ", dic_dataframe2.shape)

# Inner Join: (only mutual records are going to remain)---------------------------------------------------------------->

dic_join = dic_dataframe.merge(dic_dataframe2, on ="name",  suffixes=("_data1", "_data2"))

print("Note E is removed: ")
print("dic_join: ", dic_join)

dic_join2 = dic_dataframe2.merge(dic_dataframe, on="name", suffixes=("_data2", "_data1"))

print("Note D is removed: ")
print("dic_join2: ", dic_join2)

print(dic_join2.columns)

print("Most repeated item", dic_join2.value_counts("name"))

# one-to-one relationships: every row in the left is related to only one row on the right table
# One-to-many relationships: Every row in the left table is related to one or more rows in the right table

# for one-to-many relationships no further process required like our example for record name "a"

dic3 = {
    "name": ["A", "A", "A", "B", "A"],
    "family": ["a", "a", "a3" ,  "b", 'a'],
    "business": ["CS", "Mech", "Eng", "Eng", "Elect"]
}
dic_dataframe3 = pd.DataFrame(dic3)

dic_join3 = dic_dataframe.merge(dic_dataframe3, on="name", suffixes=("_name", "_job"))
print("dic_join3: \n", dic_join3)

# --------------------------------------Merging multiple DataFrames: (More than two tables) .merge().merge().merge()....

dic_join4 = dic_dataframe.merge(dic_dataframe3, on=["name", "family"])

print("dic_join4: \n",dic_join4)

dic_join5 = dic_dataframe.merge(dic_dataframe2, on="name").merge(dic_dataframe3, on="name")
print("dic_join5: \n", dic_join5)


# ------------------------------------------------Left Join ----------------------------------------------------------->
# Return all info in the left table plus info of the right table that are mateches in both
# Dataset used in the course were The Movie DB dataset

dic_join6 = dic_dataframe.merge(dic_dataframe2, on="name", how="left")

print("Left join and this time E record is kept, dic_join6: \n", dic_join6)

# ------------------------------------------------Right Join ---------------------------------------------------------->
# Mirror opposite of left one

dic_join7 = dic_dataframe.merge(dic_dataframe2, on="name", how="right")

print("Left join and this time D record is kept, dic_join7: \n", dic_join7)

# if key names were different here is the approach:
dic_join8 = dic_dataframe.merge(dic_dataframe2, left_on="family", right_on="family2", how="right")

print("Different key names and result dic_join8: \n", dic_join8)

# ------------------------------------------------Outer Join ---------------------------------------------------------->
# Include everything

dic_join9 = dic_dataframe.merge(dic_dataframe2, on="name", how="outer")

print("Outer join and every record is kept, dic_join9: \n", dic_join9)

# ------------------------------------------------Self Join ----------------------------------------------------------->
# Mergin a table to itself
# Usually used for sequential relationships data (what happened next, Toy Story, Toy Story2, ... examples)
# Hierarchical relationships
# Graph data

dic_join_sequels = dic_dataframe.merge(dic_dataframe, left_on= "family", right_on="name")

print("self join: \n", dic_join_sequels)

#-----------------------------------------------Merging on Indexes----------------------------------------------------->

dic_dataframe_index = dic_dataframe.set_index("name")
print("Changing the index of dic_dataframe: \n", dic_dataframe_index)

dic_dataframe2_index = dic_dataframe2.set_index("name")

dic_join10 = dic_dataframe_index.merge(dic_dataframe2_index, on="name", how="left")
print(dic_join10)

dic_dataframe_index2 = dic_dataframe.set_index(["name", "family"])
#print("Changing the two index of dic_dataframe: \n", dic_dataframe_index2)

dic_dataframe2_index2 = dic_dataframe2.set_index(["name", "family"])
#print("Changing the two index of dic_dataframe: \n", dic_dataframe2_index2)
dic_join11 = dic_dataframe_index2.merge(dic_dataframe2_index2, on=["name", "family"], how="outer")
print(dic_join11)
print(dic_join11.shape)


dic_dataframe2_index3 = dic_dataframe2.set_index(["name", "family2"])
print(dic_dataframe2_index3)

dic_join12 = dic_dataframe_index2.merge(dic_dataframe2_index3,  left_index=True, right_index=True, how="outer")
print(dic_join12)

#-------------------------------------------------Filtering Join------------------------------------------------------->
# opposite of Mutating joins (above)
# Filter observations from table based on whether or not they match an observation in another table
# ----------------------------------------------------Semi join-------------------------------------------------------->
# Similar to inner join but only values of the left table would remain
# No duplication even with one-to-many relationships

dic_join13 = dic_dataframe.merge(dic_dataframe2, on="name")
print("Regular inner join: \n", dic_join13)

dic_join14 = dic_dataframe[dic_dataframe["name"].isin(dic_join13["name"])]
print("Semi_join:\n Notice The A record we are going to have one record and columns are from the left table:\n", dic_join14)

# ----------------------------------------------------Anti join-------------------------------------------------------->
# Opposite of the semi join to somehow
# Only left table values

dic_join15 = dic_dataframe.merge(dic_dataframe2, on="name", how="left", indicator=True)
dic_join15_2 = dic_join15.loc[dic_join15["_merge"] == "left_only", "name"]
dic_join15_3 = dic_dataframe[dic_dataframe["name"].isin(dic_join15_2)]
print("Anti join: \n", dic_join15_3)

#-------------------------------------------------Concatenation/merge tables vertically-------------------------------->

# concat(), axis=0

#-------------------------------------------------Basic---------------------------------------------------------------->
# same columns names
#pd.concat([])
dic_join16 = pd.concat([dic_dataframe[["name", "family"]],dic_dataframe2[["name", "family"]]], ignore_index=False,
                       keys=['First', 'Second'])

# if we don't mantion ignore_index = True, it would retain the original index
print("Vertically join: \n", dic_join16)

# Different columns names
dic_join17 = pd.concat([dic_dataframe,dic_dataframe2], ignore_index=False,
                       keys=['First', 'Second'])

# if we don't mantion ignore_index = True, it would retain the original index
print("Vertically join2: \n", dic_join17)

# inner join

dic_join18 = pd.concat([dic_dataframe, dic_dataframe2], join="inner")

# if we don't mantion ignore_index = True, it would retain the original index
print("Only culomns in common will be showed, Vertically join3: \n", dic_join18)

# ----------------------------------------------------- Verifying integrity-------------------------------------------->
# possible merging, one-to-many or many-to-many
# for .merge(validate=["one-to-one, one-to-many, many-to-many, many-to-one"]
dic_join19 = dic_dataframe.merge(dic_dataframe2, on="name", validate="one_to_many")

print(dic_join19)


# for .concat(verify_integrity=False) default is False, just check the duplication in index

dic_join20 = pd.concat([dic_dataframe, dic_dataframe2], verify_integrity=False)
print(dic_join20)


#-------------------------------------------------------Using pd.merge_ordered()------------------------------------------>

# Merge time-series and other ordered data ---- merge_ordered() & also for filling missing data
# same arguments as pd.merge() such as on, left_on, right_on, how, suffixes
# just default is outer instead of inner
# similar to outer join

dic_join21 = pd.merge_ordered(dic_dataframe, dic_dataframe2, on="name")

dic_join22 = dic_dataframe.merge(dic_dataframe2, how="outer", on="name")
print("Use merge_ordered(): \n", dic_join21, "\n Vs. from .merge() method: \n", dic_join22)

# By Forward fill, missing data will be filled

dic_join23 = pd.merge_ordered(dic_dataframe, dic_dataframe2, on="name", fill_method="ffill")
print("After forward fill: \n", dic_join23)

# reminder for correlation: .corr()

#-----------------------------------------------------------------------Using merge_asof()----------------------------->

# same for the time-series data
# similar as merge_ordered(how="left")
# match on the nearest key column and not exact matches

# !!!! notice: merged "on" columns must be sorted


dic_list10 = [
    {"id": 1, "salary": 100, "nickname":"Aa1"},
{"id": 4, "salary": 150, "nickname":"Bb1"},
{"id": 7, "salary": 200, "nickname":"Cc1"},
{"id": 10, "salary": 300, "nickname":"Ea1"},
{"id": 11, "salary": 400, "nickname":"LA1"}
]

dic_dataframe10 = pd.DataFrame(dic_list10)

dic_list11 = [
    {"id": 13, "salary": 99, "nickname":"Aa2"},
{"id": 24, "salary": 150, "nickname":"Bb2"},
{"id": 37, "salary": 210, "nickname":"Cc2"},
{"id": 40, "salary": 330, "nickname":"Ea2"},
{"id": 51, "salary": 420, "nickname":"LA2"}
]

dic_dataframe11 = pd.DataFrame(dic_list11)

dic_join24 = pd.merge_asof(dic_dataframe10, dic_dataframe11, on="salary")
dic_join25 = pd.merge_asof(dic_dataframe10, dic_dataframe11, on="salary", direction="forward")

#direction can be forward, nearest, backward

print("print merge_asof() excample: \n", dic_join24, "\n Vs. with direction: \n", dic_join25)

# .diff(), find the difference between each record and record in the next row
print(dic_join24.iloc[:, :2].diff())

#----------------------------------------------------------------.query()---------------------------------------------->

# .query() and need input string which ois similar to !!!"WHERE in SQL"!!!

print("An example of .query() method: \n",dic_dataframe11.query('id >=30 and id <50 or nickname == "LA2"'))

#----------------------------------------------------------------.melt()----------------------------------------------->

#unpivot a table from wide to long format ---- > more computer-freindly format
# wide format : one-to-one data   / long/tall format : one-to-many data (To me it's more like normalizing in SQL)

dic_join26 = dic_dataframe.melt(id_vars=["name"])
print("an example of melting: \n", dic_join26)

dic_join27 = dic_dataframe.melt(id_vars=["name"], value_vars=["family"], var_name="type", value_name="family_name")
print("another example of melting: \n", dic_join27)