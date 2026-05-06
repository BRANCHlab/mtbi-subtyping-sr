import numpy as np

# time since injury

x1 = 9.9
s1 = 7.6
n1 = 316

x2 = 9.1
s2 = 5.6
n2 = 40

x3 = 10.8
s3 = 12.1
n3 = 52

x4 = 8.8
s4 = 6.8
n4 = 115

x5 = 7.2
s5 = 9.9
n5 = 57

x6 = 6.3
s6 = 6.6
n6 = 17

x7 = 8.3
s7 = 6.5
n7 = 66

x8 = 9.0
s8 = 7.7
n8 = 95


means = np.array([x1, x2, x3, x4, x5, x6, x7, x8])
sds = np.array([s1, s2, s3, s4, s5, s6, s7, s8])
ns = np.array([n1, n2, n3, n4, n5, n6, n7, n8])

pooled_mean = sum(means*ns) / sum(ns)
print(pooled_mean) # 9.2

pooled_var = sum(sds ** 2 * (ns - 1)) / (sum(ns) - 3)
pooled_sd = pooled_var ** 0.5
print(pooled_sd) # 7.9
