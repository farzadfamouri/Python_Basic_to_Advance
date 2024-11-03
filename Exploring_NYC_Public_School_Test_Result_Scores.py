# Re-run this cell
import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

# Preview the data
schools.head()

# Start coding here...
# Add as many cells as you like...
best_math_schools = schools[schools['average_math']>= (0.8*800)][["school_name","average_math"]].sort_values("average_math", ascending =False)
print(best_math_schools)

schools["total_SAT"] = schools["average_reading"] + schools["average_math"] + schools["average_writing"]
top_10_schools = schools.sort_values("total_SAT", ascending=False).head(10)[["school_name", "total_SAT"]]
print(top_10_schools)

# Calculate the standard deviation of 'total_SAT' for each school
# Use a single transform call for each statistic
schools['std_SAT'] = schools.groupby("borough")["total_SAT"].transform('std')
schools['num_schools'] = schools.groupby("borough")["total_SAT"].transform('count')
schools['average_SAT'] = schools.groupby("borough")["total_SAT"].transform('mean')

# Create a DataFrame to store the borough with the largest standard deviation of SAT scores
largest_std_dev = pd.DataFrame()

# Find the borough with the largest standard deviation of SAT scores
largest_borough = schools.sort_values("std_SAT", ascending=False).head(1)

# Assign the borough and its corresponding std_SAT to the 'largest_std_dev' DataFrame
largest_std_dev["borough"] = largest_borough["borough"].values
largest_std_dev["std_SAT"] = largest_borough["std_SAT"].values.round(2)
largest_std_dev["num_schools"] = largest_borough["num_schools"].values
largest_std_dev["average_SAT"] = largest_borough["average_SAT"].values.round(2)

# Display the result
largest_std_dev.head()