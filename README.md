# Hypothesis Testing | CSIS 344

## Hypothesis

I hypothesize that the passenger count of international flights
is greater than the passenger counts of domestic flights in 
San Francisco International Airport

## Dependent Variable (y axis)

* Passenger count per flight

## Independent Variable(s) (x axis)

* International vs Domestic flights

## Controlled Variable(s)

* Airlines at SFO confirmed that these flights were recorded per month between 1999 and 2025.
* Airline category

## Uncontrolled Variable(s)

* Accurate flight count? What if passengers miss their flight?
* What if some flights were canceled?

## Planned t-Test

* One-tailed or two-tailed: one-tailed - International passenger count is greater than domestic passenger count.
* Independent or paired samples: independent - International passenger count vs domestic passenger count.

## Results

I'm using a threshold of p < 0.05 to determine the normality of both group A & B

### Normality Tests

#### International Group
D'Agostino's for International: p=0.0
The probability of the International passengers being from a normal distribution is exactly zero;
therefore, we can resonably conclude that the data is likely not normally distributed

Shapiro-Wilk for International: p=4.05302e-115
The probability of the International passengers being from a normal distribution is less than zero;
therefore, we can resonably conclude that the data is likely not normally distributed

#### Domestic Group
D'Agostino's for Domestic: p=0.0
The probability of the Domestic passengers being from a normal distribution is exactly zero;
therefore, we can resonably conclude that the data is likely not normally distributed

Shapiro-Wilk for Domestic: p=2.01562e-97
The probability of the Domestic passengers being from a normal distribution is less than zero
therefore, we can resonably conclude that the data is likely not normally distributed

Overall, I conclude that both of these groups are not equally distributed

### T Test

#### Mann-Whitney U test: p = 1.0

Used the Mann-Whitney U test because my data is not normally distributed and
they're independent samples

It is unlikely enough that international and domestic are from different distributions,
so I can reject the null hypothesis and accept my alternative hypothesis

## Conclusion
The passenger count of international flights **is greater** than the passenger counts of 
domestic flights in San Francisco International Airport.
