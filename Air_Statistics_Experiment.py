import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
flight_data = pd.read_csv("Air_Traffic_Passenger_Statistics.csv")

# filter out invalid rows
flight_data = flight_data[flight_data['Passenger Count'] > 0]

# Split into group A and group B
# for me, group A is the international flights
# group B is the domestic flights

# International flights only
international_flights = flight_data[flight_data['GEO Summary'].str.startswith('International')]
print('International')
print(international_flights)

# Domestic flights only
domestic_flights = flight_data[flight_data['GEO Summary'].str.startswith('Domestic')]
print('Domestic')
print(domestic_flights)

# now, keep just the passenger count for each group
international_passengers = international_flights['Passenger Count']
domestic_passengers = domestic_flights['Passenger Count']


# verify the normality of the data

# plot a histogram of the international flights
plt.figure()
international_passengers.plot.hist(xlabel='Count', title='International Flight Passenger Count', bins=25)

# add a vertical line at the mean of the international samples
international_mean_passenger = international_passengers.mean()
plt.axvline(x=international_mean_passenger, color='red')

# Adding the limits for x and y
plt.xlim(0,110000)
plt.ylim(0,9500)
plt.show()

# plot a histogram of the domestic flights
plt.figure()
domestic_passengers.plot.hist(xlabel='Count', title='Domestic Flight Passenger Count', bins=25)

# Adding the limits for x and y
plt.xlim(0,700000)
plt.ylim(0,8000)
# add a vertical line at the mean of the domestic samples
domestic_mean_passenger = domestic_passengers.mean()
plt.axvline(x=domestic_mean_passenger,color='red')
plt.show()

#
# great, visually inspected the histogram, and for my data, it looks like they are both
# probably not normally distributed.
# Let's go further, and run actual statistical tests to determine whether it was likely
# or not that the data is from a normal distribution

# first test: D'Agostino's test
# International passenger
stat, pvalue_dagostino_international = scipy.stats.normaltest(international_passengers)
print(f"D'Agostino's for International: p={pvalue_dagostino_international:.6}")
# D'Agostino's for International: p=0.0

# more generally: If your p-value is < 0.05 (that is, less that 5% likely),
# then you can reasonably conclude that the data is not normally distributed

# second test: Shapiro-Wilk test
# again, for international passengers
stat, pvalue_shapiro_international = scipy.stats.shapiro(international_passengers)
print(f"Shapiro-Wilk for International: p={pvalue_shapiro_international:.6}")
# Shapiro-Wilk for International: p=4.05302e-115


# first test: D'Agostino's test
# Domestic passengers
stat, pvalue_dagostino_domestic = scipy.stats.normaltest(domestic_passengers)
print(f"D'Agostino's for Domestic: p={pvalue_dagostino_domestic:.6}")
# D'Agostino's for Domestic: p=0.0

# second test: Shapiro-Wilk test
# again, for domestic passengers
stat, pvalue_shapiro_domestic = scipy.stats.shapiro(domestic_passengers)
print(f"Shapiro-Wilk for Domestic: p={pvalue_shapiro_domestic:.6}")
# Shapiro-Wilk for Domestic: p=2.01562e-97

# Once you know if your data is normally distributed or not,
# determine which t-test is appropiate
# ths will based on two things:
# 1) normal vs not normal data
# 2) independent vs paired samples

'''
            +-----------------------+----------------------+
            | normal                | not normal           |
------------+-----------------------+----------------------+
independent | scipy.stats.ttest_ind | scipy.mannwhitneyu   |
------------+-----------------------+----------------------+
paired      | scipy.stats.ttest_rel | scipy.stats.wilcoxon |
------------+-----------------------+----------------------+
'''

# for my data. it is:
# 1) not normally distributed
# 2) independent samples (passengers are either international or domestic...none in both groups)

# ...so: not normal + independent samples = man-whitney y test

# run the actual t-test

# recall my hypothesis: international > domestic
# first group is international
# second group is domestic
# alternative: greater than
result = scipy.stats.mannwhitneyu(international_passengers, domestic_passengers, alternative='greater')
ttest_pvalue = result.pvalue
print(f'Mann-Whitney U test: p = {ttest_pvalue:.6}')

# remember:
# the "null hypothesis" is that the two piles of data are from the same distribution
# our hypothesis is the "alternative"---that the data is from two different distributions,

# so, if the result p-value from the t-test is < 0.05, we can reject the null hypothesis.
# and accept our alternative hypothesis that they are actually from two different distributions,
# and futhermore, that the distributions are related in the way we supposed in our t-test and hypothesis
# for example, that international and domestic are not only different, but also that international
# is greater that domestic

# Mann-Whitney U test: p = 1.0

# so, for me, it is unlikely enough that international and domestic are from different distributions,
# so I can reject the null hypothesis and accept my alternative hypothesis

# i.e., my hypothesis is supported

# i.e., my hypothesis is correct