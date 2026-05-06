# Calculate pooled mean and standard deviation of ages in anderson_2024
c1_age_mean = 38.92
c2_age_mean = 34.89
c3_age_mean = 37.48

c1_age_sd = 14.86
c2_age_sd = 13.89
c3_age_sd = 13.39

n1 = 38
n2 = 28
n3 = 25

pooled_mean = (c1_age_mean * n1 + c2_age_mean * n2 + c3_age_mean * n3) / (n1 + n2 + n3)

# 37.28
print(f"Pooled mean: {pooled_mean:.2f}")

c1_age_var = c1_age_sd ** 2
c2_age_var = c2_age_sd ** 2
c3_age_var = c3_age_sd ** 2

pooled_var = (c1_age_var * (n1 - 1) + c2_age_var * (n2 - 1) + c3_age_var * (n3 - 1)) / (n1 + n2 + n3 - 3)

pooled_sd = pooled_var ** 0.5

# 14.18
print(f"Pooled sd: {pooled_sd:.2f}")
