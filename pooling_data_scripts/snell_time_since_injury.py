import numpy as np

x1 = 32.3
s1 = 20.8
n1 = 53

x2 = 43.6
s2 = 25.5
n2 = 56

x3 = 48.8
s3 = 23.4
n3 = 37


means = np.array([x1, x2,x3])
sds = np.array([s1, s2, s3])
ns = np.array([n1, n2, n3])

pooled_mean = sum(means*ns) / sum(ns)
print(pooled_mean) # 40.8

pooled_var = sum(sds ** 2 * (ns - 1)) / (sum(ns) - 3)
pooled_sd = pooled_var ** 0.5
print(pooled_sd) # 23.4
