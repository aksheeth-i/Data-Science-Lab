# Authors: William, Aksheeth
# Assignment: Data Science Lab, Lab 1, Problem 3
import numpy as np
import math

samples = np.random.normal(0, 5, 25000)
mean  = sum(samples) / len(samples)
var = (1/(len(samples) - 1)) * sum((samples - mean) ** 2)
std = math.sqrt(var)

print("The approx. mean of the distribution is: ", mean)
print("The approximate standard deviation is ", std)