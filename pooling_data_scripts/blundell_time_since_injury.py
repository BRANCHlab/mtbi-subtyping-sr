import numpy as np

x1 = 5.2
s1 = 4.8
n1 = 24

x2 = 7.5
s2 = 10.7
n2 = 35

x3 = 6.8
s3 = 6.2
n3 = 25

means = np.array([x1, x2, x3])
sds = np.array([s1, s2, s3])
ns = np.array([n1, n2, n3])

pooled_mean = sum(means*ns) / sum(ns)
print(pooled_mean) # 6.63

pooled_var = sum(sds ** 2 * (ns - 1)) / (sum(ns) - 3)
pooled_sd = pooled_var ** 0.5
print(pooled_sd) # 8.12








