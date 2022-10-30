# Authors: William, Aksheeth
# Assignment: Data Science Lab, Lab 1, Problem 2
import numpy as np
import math
import matplotlib.pyplot as plt
def z_distribution(n): 
  z = []
  for i in range(0, 1000):
    # Compute a z_n
    z_n = 0
    for i in range(0, n):
      x = np.random.binomial(n = 1, p = .5, size = 1)
      if x == 0:
        z_n += -1
      else:
        z_n += 1
      z.append((1 / math.sqrt(n)) * z_n)
  plt.hist(z, density=True, bins=20)  # density=False would make counts
  plt.show()

z_distribution(n = 5)
z_distribution(n = 100)
z_distribution(n = 250)
