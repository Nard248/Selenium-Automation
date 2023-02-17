data(ChickWeight)
print(head(ChickWeight))

x <- ChickWeight[ChickWeight$Diet == 1,]$weight
y <- ChickWeight[ChickWeight$Diet == 2,]$weight

median_x = median(x)
median_y = median(y)
cat("Diet 1 Median: ", median_x, "Diet 2 Median: ", median_y)

mean_x = mean(x)
mean_y = mean(y)
cat("Diet 1 Mean: ", mean_x, "Diet 2 Mean: ", mean_y)
cat("The difference is: ", mean_y - mean_x)

library(scales)
hist(x, col = alpha("green", 0.2))
par(new=TRUE)
hist(y, col = alpha("red", 0.2))

## From those histograms we can deduce that Diet 1 works better, as till value of 100, values for the both diets are the same(Distribution of weights)
# But after the bin 50-100 wee see that red part is more, thus there are more rows with values in that range, thus the weight of chicks with diet 2 is higher
# Thus the first diet works better.

#Problem 3
x1 <- c(0, 3, 4, 5, -1)
y1 <- c(2, -1, 2, 5, 2)

plot(x1, y1)


data(pressure)
pressure_ <- pressure$pressure
temperature_ <- pressure$temperature
plot(pressure_, temperature_)
plot(log(pressure_), temperature_)
plot(log(pressure_), log(temperature_))

#Problem 4
aapl <- read.csv("R/aapl.csv")
print(head(aapl))
print(tail(aapl))
adj_prices = aapl$Adj.Close
first = adj_prices[1:length(adj_prices) -1]
last = adj_prices[2:length(adj_prices)]
print(first)
print(last)
returns <- (last - first)/first
print(returns)

hist(returns, col = alpha("green", 0.2))
# Most of the time weekly returns were positive in range from 0.00 to 0.05


data(airquality)
oz <- airquality$Ozone
hist(oz, breaks=20)
print(median(oz[!is.na(oz)]))


# Load the mtcars dataset
data("mtcars")

# Extract the mpg values for each group of cars
mpg_4cyl <- mtcars$mpg[mtcars$cyl == 4]
mpg_6cyl <- mtcars$mpg[mtcars$cyl == 6]
mpg_8cyl <- mtcars$mpg[mtcars$cyl == 8]

# Calculate the standard deviation of each group of cars
a <- sd(mpg_4cyl)
b <- sd(mpg_6cyl)
c <- sd(mpg_8cyl)

# Print the results
cat("Standard Deviation of 4-cylinder cars' mpg:", a, "\n")
cat("Standard Deviation of 6-cylinder cars' mpg:", b, "\n")
cat("Standard Deviation of 8-cylinder cars' mpg:", c, "\n")

# Load the cars dataset
data("cars")
median_ = median(cars$dist)
# Calculate the MAD from the Median for the dist variable
mad_dist <- mad(cars$dist, center = median_)

# Round the result to 2 decimal places
result <- round(mad_dist, 2)

# Print the result
cat("The Median Absolute Deviation from the Median for the dist variable in the cars dataset is:", result)

# Define the dataset
x <- c(2, 6, 6, 6, 4, 7, 5, 3, 8, 4, 2, 3, 3, 3, 6, 3, 6, 5, 2, 6)

# Calculate the quartiles using the quantile function
quartiles <- quantile(x, probs = c(0.25, 0.5, 0.75))

# Sum up Q1, Q2, and Q3
result <- sum(quartiles)

# Print the result
cat("Q1 + Q2 + Q3 is:", result)

# Set the random numbers seed to 1
set.seed(1)

# Generate a Dataset of 50 random numbers from the Unif[-5,4] distribution
x <- runif(50, min = -5, max = 4)

# Calculate the quantile of order 34%
quantile_34 <- quantile(x, probs = 0.34)

# Round the result to two decimal points after the period
result <- round(quantile_34, 2)

# Print the result
cat("The quantile of order 34% of the generated dataset is:", result)

# Calculate the 30% and 80% quantiles of the N(0,1) distribution
quantiles <- qnorm(c(0.3, 0.8))

# Calculate the sum of the quantiles
result <- sum(quantiles)

# Print the result
cat("The sum of the 30% and 80% quantiles of the N(0,1) distribution is:", result)

