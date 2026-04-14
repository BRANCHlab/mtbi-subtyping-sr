import numpy as np

x1 = 54.6
s1 = 23.5
n1 = 20

x2 = 51.5
s2 = 27.7
n2  = 31

x3 = 43.3
s3 = 24.0
n3 = 27

means = np.array([x1, x2,x3])
sds = np.array([s1, s2, s3])
ns = np.array([n1, n2, n3])

pooled_mean = sum(means*ns) / sum(ns)
print(pooled_mean) # 49.5

pooled_var = sum(sds ** 2 * (ns - 1)) / (sum(ns) - 3)
pooled_sd = pooled_var ** 0.5
print(pooled_sd) # 25.4
