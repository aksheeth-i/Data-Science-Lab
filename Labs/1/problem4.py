# Authors: William, Aksheeth
# Assignment: Data Science Lab, Lab 1, Problem 4
import numpy as np 

means = [-5, 5]
cov = [[20, .8], [.8, 30]]

samples = np.random.multivariate_normal(means, cov, 10000)

est_mean = []
est_mean_x = 0
est_mean_y = 0
for sample in samples:
  est_mean_x += sample[0]
  est_mean_y += sample[1]
est_mean_x /= len(samples)
est_mean_y /= len(samples)
est_mean = [est_mean_x, est_mean_y]
print("Here is the vector estimating the means: \n" + str(est_mean))

cov = []
x = [sample[0] for sample in samples]
y = [sample[1] for sample in samples]
x_centered = [i - est_mean[0] for i in x]
y_centered = [i - est_mean[1] for i in y]
D_cent = []
for i in range(len(samples)):
  D_cent.append([x_centered[i], y_centered[i]])
D_cent = np.matrix(D_cent)
cov = np.multiply((1/(len(samples) - 1)), np.matmul(D_cent.transpose(), D_cent))
print("\nThe Covariance Matrix: \n" + str(cov))