# Authors: William, Aksheeth
# Assignment: Data Science Lab, Lab 1, Problem 1
import numpy as np 
import matplotlib.pyplot as plt
import statistics as stat 
from scipy.stats import norm

def main():
    print("Problem 1 for 460J")
    mean_1 = - 10
    std_1 = 5 
    samples_1 = np.random.normal(mean_1, std_1, 1000)
    mean_2 = 10
    std_2 = 5    
    samples_2 = np.random.normal(mean_2, std_2, 1000)

    sums = [samples_1[i] + samples_2[i] for i in range(1000)] 
    # plt.plot([i for i in range(-500, 500)], )
    plt.hist(sums, density=True, bins=100)

    print("For part A: We observe that the histogram is about symmetrical around x = 0, and appears to also be a normal distribution\n we can see that the mean is approximately zero")
    
    print("\nFor part B: Estimating Variance")
    mean = np.mean(sums)
    var = stat.variance(sums)
    print("The estimation of the mean is: " + str(mean))
    print("The estimation of the variance is: " + str(var))
    plt.show()    


main()