# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Start coding here! Use as many cells as you like
print(netflix_df.shape)
print(netflix_df.columns.tolist())
# part 1
duration_list = netflix_df[['duration', 'release_year']]
#print(duration_list)
print(type(duration_list))
print(duration_list.shape)
duration_list_90s = duration_list[(duration_list['release_year'] >= 1990) & (duration_list['release_year'] < 2000)]
#print(duration_list_90s)
duration_repeat = duration_list_90s["duration"].mode()
print(duration_repeat)
duration = duration_repeat[0]
print(duration)

# part 2
genre_list = netflix_df [['release_year','genre', 'duration']]
#print(genre_list)
genre_action = genre_list[genre_list['genre'] == 'Action']
genre_action_short = genre_action[genre_action['duration'] < 90]
genre_action_short_90s = genre_action_short[(genre_action_short['release_year'] >= 1990) & (genre_action_short['release_year'] < 2000)]

print(genre_action_short_90s)
short_movie_count_array = genre_action_short_90s.count()
short_movie_count =  short_movie_count_array [0]
print(short_movie_count)