import matplotlib.pyplot as plt

# give complete control of properties of the plot, customize and control precise of your visualization

# we can make a program automatically generate visualization

# first step to define the blank table
fig, ax = plt.subplots()
#plt.show()

import pandas as pd
import numpy as np

dic_list11 = [
    {"id": 13, "salary": 99, "nickname":"Aa2"},
{"id": 24, "salary": 150, "nickname":"Bb2"},
{"id": 37, "salary": 210, "nickname":"Cc2"},
{"id": 40, "salary": 330, "nickname":"Ea2"},
{"id": 51, "salary": 420, "nickname":"LA2"}]

dic_dataframe11 = pd.DataFrame(dic_list11)

# second phase, defining the dataset
ax.plot(dic_dataframe11['salary'], dic_dataframe11['id'], marker="v", linestyle="--", color ='b')
ax.set_xlabel('Salary')
ax.set_ylabel('Id')
ax.set_title("Company")
# for mark and line read the reference

plt.show()


#-----------------------------------------------Multiples------>

fig, ax2 = plt.subplots(1,2)

# Notice ax shape is 1D array
ax2[0].plot(dic_dataframe11['salary'], dic_dataframe11['id'])
ax2[0].set_xlabel('Salary')
ax2[0].set_ylabel('Id')
ax2[0].set_title("Company")
plt.show()

# Notice ax shape is 2D array
fig , ax3 = plt.subplots(2,2, sharey=True,sharex=True)
ax3[0, 1].plot(dic_dataframe11['salary'], dic_dataframe11['id'])
ax3[0, 1].set_xlabel('Salary')
ax3[0, 1].set_ylabel('Id')
ax3[0, 1].set_title("Company")
plt.show()

#-----------------------------------------------Time-series------>

import pandas as pd

# Load the CSV and set the index column
climate_change = pd.read_csv("climate_change.csv", index_col="date")

# Parse index as a date like below: (We make sure the index array type is datetime64  (pandas)
climate_change.index = pd.to_datetime(climate_change.index)

#OR:   climate_change = pd.read_csv("climate_change.csv", parse_dates =["date"], index_col ="date")

# Print the DataFrame
print(climate_change.index)

fig4, ax4 = plt.subplots()
ax4.plot(climate_change.index, climate_change["co2"])
ax4.set_xlabel("Time")
ax4.set_ylabel("Co2")
plt.show()


# application of time-series, to specify the time:

seventies = climate_change["1970-01-01":"1979-12-31"]
fig5, ax5 = plt.subplots()
ax5.plot(seventies.index, seventies["co2"])
ax5.set_xlabel("Time")
ax5.set_ylabel("Co2")
plt.show()

#-----------------------------------Twin method-Two time-series together (When values are not same scale)
fig6, ax6 = plt.subplots()
ax6.plot(climate_change.index, climate_change["co2"], color ="blue")
ax6.set_xlabel("Time")
ax6.set_ylabel("Co2")
ax6.tick_params('y', colors="blue") # y value become blue
ax7 = ax6.twinx()
ax7.plot(climate_change.index, climate_change["relative_temp"], color = "red")
ax7.set_ylabel("Relative Temperature", color ="red")
ax7.tick_params('y', colors="red") # y value become red
plt.show()

# Define a function called plot_timeseries ( it would shorten the code)
def plot_timeseries(axes, x, y, color, xlabel, ylabel):

  # Plot the inputs x,y in the provided color
  axes.plot(x, y, color=color)

  # Set the x-axis label
  axes.set_xlabel(xlabel)

  # Set the y-axis label
  axes.set_ylabel(ylabel, color=color)

  # Set the colors tick params for y-axis
  axes.tick_params('y', colors=color)


# ------------------------------------------- Annotating time-series
fig8, ax8 = plt.subplots()

# Plot the CO2 levels time-series in blue
plot_timeseries(ax8, climate_change.index, climate_change["co2"],"black", "Time (years)", "CO2 levels")

# Create a twin Axes object that shares the x-axis
ax9 = ax8.twinx()

# Plot the relative temperature data in red
plot_timeseries(ax9, climate_change.index, climate_change["relative_temp"],"green", 'Time (years)',"Relative temperature (Celsius)")
ax9.annotate(
    ">1 degree",
    xy=(pd.Timestamp("2015-10-06"), 1),
    xytext=(pd.Timestamp("2008-10-06"), -0.2),
    arrowprops={"arrowstyle": "->", "color": "red"}
)

plt.show()


# ------------------------------------------------------------Quantitative Comparisons--------------------------------->

# ---------------------------------- Bar charts----->

import pandas as pd
import matplotlib.pyplot as plt
medals = pd.read_csv('medals_by_country_2016.csv', index_col=0)
print(medals)

fig10, ax10 = plt.subplots()
ax10.bar(medals.index, medals["Gold"], label="Gold")
ax10.bar(medals.index, medals["Silver"], bottom=medals["Gold"], label="Silver")
ax10.bar(medals.index, medals["Bronze"], bottom=medals["Gold"]+medals["Silver"], label = "Bronze")
ax10.set_xticklabels(medals.index, rotation=90)
ax10.set_ylabel("Number of medals")
ax10.legend() #shows which colors represents which medal
plt.show()

# ------------------------------------ Histogram Charts --->
import pandas as pd
summer2016 = pd.read_csv('summer2016.csv')
mens_rowing = summer2016[(summer2016["Sex"] == "M") & (summer2016["Sport"] == "Rowing")]
mens_gymnastics = summer2016[(summer2016["Sex"] == "M") & (summer2016["Sport"] == "Gymnastics")]

# bar example for comparison:

fig11, ax11 = plt.subplots()
ax11.bar("Rowing", mens_rowing["Height"].mean())
ax11.bar("Gymnastics", mens_gymnastics["Height"].mean())
ax11.set_ylabel("Height (cm)")
plt.show()

fig12, ax12 = plt.subplots()
ax12.hist(mens_rowing["Height"], label= "Rowing",alpha=0.7, bins=15, histtype="step")
ax12.hist(mens_gymnastics["Height"], label = "Gymnastics",alpha=0.7, bins=15, histtype="step")
ax12.set_xlabel("Height (cm)")
ax12.set_ylabel('# of observations')
plt.legend()
plt.show()

# ------------------------------Statistical plotting / for comparision

# Adding error bars to bar charts and plots

# charts
fig13, ax13 = plt.subplots()
ax13.bar("Rowing", mens_rowing["Height"].mean(), yerr=mens_rowing["Height"].std())
ax13.bar("Gymnastics", mens_gymnastics["Height"].mean(), yerr=mens_gymnastics["Height"].std())
ax13.set_ylabel("Height (cm)")
plt.show()

# plots

seattle_weather = pd.read_csv('seattle_weather.csv')
austin_weather = pd.read_csv('austin_weather.csv')

"""fig15, ax15 = plt.subplots()

# Add Seattle temperature data in each month with error bars
ax15.errorbar(seattle_weather["MONTH"],
              seattle_weather["MLY-TAVG-NORMAL"],
              seattle_weather["MLY-TAVG-STDDEV"])
ax15.errorbar(austin_weather["MONTH"],
              austin_weather["MLY-TAVG-NORMAL"],
              austin_weather["MLY-TAVG-STDDEV"])
ax15.set_ylabel("Temperature (Fahrenheit)")

plt.show()"""

# Adding boxplots/Axes object

fig14, ax14 = plt.subplots()
ax14.boxplot([mens_rowing["Height"], mens_gymnastics["Height"]])
ax14.set_xticklabels(["Rowing", "Gymnastics"])
ax14.set_ylabel('Height (cm')
plt.show()


# ---------------------------------------Scatter plots---->
# bi variate comparison -Two different variables

fig16, ax16 = plt.subplots()

ax16.scatter(climate_change["co2"], climate_change["relative_temp"])
ax16.set_xlabel("CO2 (ppm)")
ax16.set_ylabel("Relative temperature (Celsius)")
plt.show()

# two scatter plots together:

eighties = climate_change["1980-01-01":"1989-12-31"]
nineties = climate_change["1990-01-01":"1999-12-31"]

fig17, ax17 = plt.subplots()

ax17.scatter(eighties["co2"], eighties["relative_temp"], color="red", label="eighties")
ax17.scatter(nineties["co2"], nineties["relative_temp"], color="blue", label="nineties")
ax17.legend()
ax17.set_xlabel("CO2 (ppm)")
ax17.set_ylabel("Relative temperature (Celsius)")
plt.show()

# Encoding
fig18, ax18 = plt.subplots()

ax18.scatter(climate_change["co2"], climate_change["relative_temp"], c=climate_change.index)
ax18.set_xlabel("CO2 (ppm)")
ax18.set_ylabel("Relative temperature (Celsius)")
plt.show()


# ----------------------------------------------------Preparing your figures to share with others---------------------->

# choosing different style
# changing colors, fonts and background are changed

plt.style.use('ggplot')
#plt.style.use("default")
#plt.style.use("bmh")
#plt.style.use("grayscale")
#plt.style.use("seaborn-colorblind")    # more for colorful design
#plt.style.use("tableau-colorblind10")    # more for colorful design

fig19, ax19 = plt.subplots()

ax19.scatter(climate_change["co2"], climate_change["relative_temp"])
ax19.set_xlabel("CO2 (ppm)")
ax19.set_ylabel("Relative temperature (Celsius)")
#fig19.set_size_inches([5, 3])
fig19.savefig("Relative_temperature_(Celsius).png", dpi=300)
#fig19.savefig("Relative_temperature_(Celsius).jpg", quality =50)
fig19.savefig("Relative_temperature_(Celsius).svg")
plt.show()


# -------------------------------------------------Automation:

fig20, ax20 = plt.subplots()

sports = summer2016["Sport"].unique()
print(sports)
for sport in sports:
    sport_df = summer2016[summer2016["Sport"] == sport]
    ax20.bar(sport, sport_df["Height"].mean(),
             yerr=sport_df["Height"].std())
ax20.set_ylabel("Height (cm)")
ax20.set_xticklabels(sports, rotation=90)
plt.show()