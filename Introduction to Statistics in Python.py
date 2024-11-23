# collecting and analyzing data
# summary of data (Count or AVG)

# 1. descriptive statistics (describe and summarize data) 2. inferential statistics (By sample inferences about larger)

# 1. Numeric data (continuous, discrete)
# 2. Categorical data (Nominal / no inherent ordering like married= 1 /unmarried= 0,
# Ordinal/ has inherent like survey= very good 4 good 3 bad 2 very bad 1)

# Type of data --> 1.summary 2. visualization
# for example: numeric: mean and plot scatter categorical: count and plot bar


# ----------------------------------------------------------Summary --------------------------------------------------->
# mean, median, mode
# np.mean()

# median : .pd.sort_values().iloc[] OR np.median()

# mode : .pd.value_counts().head(1) OR statistics.mode()
# mode is more for categorical variables

# mean is more sensitive to extreme values than the median!
# mean is better for symmetric dataset and data is skewed we would prefer median,
# the mean would be pulled in the direction of the skew

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dic_list11 = [
    {"id": 13, "salary": 99, "nickname":"Aa2"},
{"id": 24, "salary": 150, "nickname":"Bb2"},
{"id": 37, "salary": 210, "nickname":"Cc2"},
{"id": 40, "salary": 330, "nickname":"Ea2"},
{"id": 51, "salary": 420, "nickname":"LA2"}
]

dic_dataframe11 = pd.DataFrame(dic_list11)


salary = dic_dataframe11[dic_dataframe11["salary"] > 200]

# Histogram of co2_emission for rice and show plot
#plt.figure()
#salary.hist()
#plt.show()

print("mean example: \n", np.mean(dic_dataframe11["salary"]))

# Calculate median consumption in USA
print("median example: \n", np.median(dic_dataframe11["salary"]))


# -----------------------------------------Spread: How close or apart data points are: -------------------------------->
# 1 Variance

# variance: dist = a[]-np.mean(a[]) and dist**2 and np.sum()and /(n-1)
# OR np.var(, ddof=1) , without ddof=1 is used for a full population

# 2 Standard devation : np.sqrt(np.var( ,ddof=1)) OR np.std( ,ddof=1)

# 3 Mean absolute deviation: dists and np.mean(np.abs(dists)
# SD is more common than MAD and is more sensitive to outliers


# ----------------------------------------Quantiles-------------------------------------------------------------------->
# np.quantile( , 0.5) = mean or np.quantile( ,[0,0.25,0.5,0.75,1])

#plt.boxplot(dic_dataframe11["salary"])
plt.show()

arr, step = np.linspace(0, 10, num=5, endpoint=False, retstep=True)
print("Example of making Array with numpy linspace:", arr)
print("Step size:", step)

print("Example of finding quantiles: ", np.quantile(dic_dataframe11["salary"], np.linspace(0,1,5)))

# ----------------------------- Interquartile Range (IQR)------------->
# Distance between 25th and 75th percentile = height of the box in a boxplot
# np.quantile( , 0.75) - np.quantile( , 0.25)

# OR
from scipy.stats import iqr

iqr = iqr(dic_dataframe11["salary"])
print("Example of IQR: ", iqr)


# definition of outlier: data < Q1 - 1.5x IQR  OR data> Q3+ 1.5X IQR

# Finding outliers:

lower_threshold = np.quantile(dic_dataframe11["salary"], 0.25)-1.5*iqr

upper_threshold = np.quantile(dic_dataframe11["salary"], 0.25)+1.5*iqr

print("Outliers: \n", dic_dataframe11[(dic_dataframe11["salary"] < lower_threshold) | (dic_dataframe11["salary"] > upper_threshold)])


#------------------------------------------------------------------Summary--------------------------------------------->
print(dic_dataframe11["salary"].describe())

# ----------------------------------------------------------chances --------------------------------------------------->

# measure by chances p = # ways event happen/ #total possible outcomes

# make sure everytime the result of random number is same:

np.random.seed(24)

# sampling:

print("Sample example: ", dic_dataframe11.sample())

# sampling without replacement (dependent):

print("Sample example2 without replacement: ", dic_dataframe11.sample(2))

# sampling with replacement (independent):

print("Sample example3 with replacement: ", dic_dataframe11.sample(2, replace=True))


# Independent events: when the probability of the second event isn't affected by the outcome of the first event

# ------------------------------------------------------Probability Distributions / Discrete -------------------------->

# expected value: mean of a distribution
# rolling die (having 1,2,3,4,5,6) it calls discrete uniform distribution

# ------------------------------------------------------------------Continuous Distributions--------------------------->
from scipy.stats import uniform

# -------------------------------------------------------------uniform.cdf(n, min, max) ----->

# the probability of having a number between 0 and 7 if the range is 0 to 12
print("probability of having a number between 0 and 7 if the range is 0 to 12: \n", uniform.cdf(7, 0, 12))

print("probability of having a number between 4 and 7 if the range is 0 to 12: \n", uniform.cdf(7, 0, 12) - uniform.cdf(4, 0, 12))

# generating random numbers according to uniform distribution:

# unifrom.rvs(min, max, n)

print("5 random numbers between 0 an 10: \n", uniform.rvs(0,5, size= 10))

# the area beneath of the probability graph is always equal to one (continuous uniform, normal, exponential, ...)


# -------------------------------------------------------------The binomial distribution ------------------------------>
# probability distribution of the number of successes in a sequence of independent trials
from scipy.stats import binom

# binom.rvs(number of coins, possibility, number of trials)

print("binomial distribution example: \n", binom.rvs(1, 0.5, size=10))

print("binomial distribution example2 with 3 coins : \n", binom.rvs(3, 0.5, size=10))

print("binomial distribution example3 with  bias coin : \n", binom.rvs(1, 0.75, size=10))


# other words: binom.rvs( number of coins, p , n)

# probability of getting 7 heads:

# bionom.pmf(trials = 7,n = 10,p = 0.5)

print("probability of getting 7 heads out of 10 times flipping the coin: \n", binom.pmf(7,10,0.5))

# probability of getting fewer than 7 heads:

# bionom.cdf(trials = 7,n = 10,p = 0.5)

print("probability of getting 7 heads and fewer out of 10 times flipping the coin: \n", binom.cdf(7,10,0.5))

# more than 7 heads:
print(1-binom.cdf(7,10,0.5))

# For bionomial distribution, trials should be independent generally!

#---------------------------------------------------------The Normal Distribution/ Bell curve-------------------------->
# 1. mean 2. STD
# Standard normal distribution: std=1 and mean = 0

# 67, 95 and 97 rule ( empirical rule):
# 68% within 1 STD of the mean, 95% within 2 STD of the mean, 99.7 percent within 3 STD of the mean

from scipy.stats import norm

# to calculate the probability: norm.cdf(value, mean, std)

print("In normal distribution, what is the probability of events happen for less than 154,\
 where the MEAN = 161, std =7? \n", norm.cdf(154,161, 7))

print("In normal distribution, what is the probability of events happen for above than 154,\
 where the MEAN = 161, std =7? \n", 1 - norm.cdf(154,161, 7))

print("In normal distribution, what is the probability of events happen for between 154 and 157,\
 where the MEAN = 161, std =7? \n", norm.cdf(157, 161, 7) - norm.cdf(154, 161, 7))

# to calculate the value: norm.ppf(probability, mean, std)


print("In normal distribution, what is the  events with probability of 90 percent,\
 where the MEAN = 161, std =7? \n", norm.ppf(0.9, 161, 7))

print("In normal distribution, what is the  events with probability of 10 percent,\
 where the MEAN = 161, std =7? \n", norm.ppf(0.1, 161, 7))

# Generating random numbers for the normal distribution: norm.rvs(mean, std, size =n)

print("random: \n", norm.rvs(161, 7, size=10))

#---------------------------------------------------------The central limit theorem ----------------------------------->

# the sampling distribution becomes closer to normal as the trials increases, samples should be random and independent

roll = pd.Series([1, 2, 3, 4, 5, 6])
sample = roll.sample(5, replace=True)
print("sample: \n", sample.mean())
sample_mean = []
for i in range(100):
    sample = roll.sample(5, replace=True)
    sample_mean.append(np.mean(sample))

print(sample_mean, pd.Series(sample_mean).mean())

import matplotlib.pyplot as plt

# to see the sampling distribution
plt.figure()
plt.hist(sample_mean, bins=10)
plt.title('sampling distributions which is getting closer\
 to normal distribution by increasing the trials')

#plt.show()

# Mean (of sample means) gives an accurate estimate of the true mean.
# Standard deviation (of sample means) indicates how much sample means will vary around the true mean,\
# with larger samples leading to less variation.


# ------------------------------------------------------------- The Poisson distribution ------------------------------>

# events appear happen at a certain rate, but completely random: #earthquakes per year/ #customer per hour ....
# probability of # events occurring over a fixed period of time --> \
# Example: Calculating probability of having less than 20 earthquakes per year
# Lambda is sign for the poisson distribution = average number of events per time interval
# it could be a discrete distribution or continuous distribution
# the distribution is always at peak in lambda value

# poisson.mdf(event, lamda) and poisson(event, lambda)

from scipy.stats import poisson
print("poisson example lambda = 8 and event =5 : \n", poisson.pmf(5, 8))

print("poisson example2 lambda = 8 and event =< 5 : \n", poisson.cdf(5, 8))

print("poisson example3 lambda = 8 and event => 5 : \n", 1 - poisson.cdf(5, 8))

# sample: poisson.rvs(lambda, size=n)

print("Poisson example4 samples lambda = 5 and n=8 : \n", poisson.rvs(mu=5, size=8))

# ------------------------------------------ More probability distributions ------------------------------------------->

# -----------------------------------------Exponential distribution:
# probability between Poisson events
# Example:  probability between 6-8 months between earthquakes
# same Lambda value(rate), -- > So time between events = 1 / lambda
# Unlike Poisson, it is continuous

from scipy.stats import expon

# time less than< time value: expon.cdf(time value, scale=(1/lambda))

# time more than > time value: 1 - expom.cdf(time, scale=(1/lambda))

print("exp example lambda = 0.5 and wait time < 1 min : \n", expon.cdf(1, scale=2))

print("exp example2 lambda = 0.5 and wait time > 4 min : \n", 1 - expon.cdf(4, scale=2))

print("exp example3 lambda = 0.5 and wait 4min >time > 1 min : \n", expon.cdf(4, scale=2) - expon.cdf(1, scale=2))


# -----------------------------------------T-distribution (Student's t-distribution):

# shape similar to normal but not exatly same, lower pick but wider (thicker tails)

# the parameter here is called freedom, when freedom is larger, the pick increases
# in other words = lower df = thicker tails, higher standard deviation
# higher df, would be closer to normal distribution

#------------------------------------------ Lag-normal distribution:
# Variable whose logarithm is normally distributed

# distribution is skewed, \
# examples: 1. length of chess game 2. adult blood pressure 3. Number of hospitalized patients in 2003


# ------------------------------------- Correlation and Experimental Design ------------------------------------------->

# scatter plot to explicit it, correlation coefficient \
# (negative would be decreasing, zero would be no relation, +-0.5 mild and above +-0.75 would be strong)

import seaborn as sns
plt.figure()
# scatter
sns.scatterplot(x= "id", y ='salary', data=dic_dataframe11[["id", "salary"]])
# linear
sns.lmplot(x= "id", y ='salary', data=dic_dataframe11[["id", "salary"]], ci=None)
#plt.show()
# correlation (Pearson product-monet correlation method)
print("correlation: \n", dic_dataframe11["id"].corr(dic_dataframe11["salary"]))

from pandas import read_csv

world_happiness_excel = read_csv("world_happiness.csv",index_col=0)

world_happiness = pd.DataFrame(world_happiness_excel)
print(world_happiness)
plt.figure()
sns.scatterplot(x='life_exp', y='happiness_score', data=world_happiness)

# Show plot
#plt.show()

# ------------------------------------- Correlation caveats ----------------------------------------------------------->
# we might have a non-linear relationships which makes the correlation value useless! ---> So, visualize always

# sometimes we need to apply transformation before calculating the correlation\
# like log(x), log(y), sqrt(x), sqrt(y), 1/x, 1/y ,...

# application: linear regression!

# notice correlation doesn't imply causation
# Confounding: maybe two variables have a correlation, but there might be a third factor which relates them\
# like drinking coffee, (smoking), cancer --> somking is confounding

plt.figure()
sns.scatterplot(x="gdp_per_cap", y="life_exp", data=world_happiness)
plt.show()
cor = world_happiness['gdp_per_cap'].corr(world_happiness['life_exp'])
print("The correlation1 of two variables with non-linear relation: \n", cor)

plt.figure()
sns.scatterplot(x="happiness_score", y="gdp_per_cap", data= world_happiness)
plt.show()

cor = world_happiness['happiness_score'].corr(world_happiness['gdp_per_cap'])
print("The correlation2 of two variables with non-linear relation: \n", cor)

# Create log_gdp_per_cap column
world_happiness['log_gdp_per_cap'] = np.log(world_happiness['gdp_per_cap'])

sns.scatterplot(x='log_gdp_per_cap',y="happiness_score",data=world_happiness)
plt.show()
cor = world_happiness['log_gdp_per_cap'].corr(world_happiness['happiness_score'])
print("The correlation3 of two variables with non-linear relation after transforming: \n", cor)

