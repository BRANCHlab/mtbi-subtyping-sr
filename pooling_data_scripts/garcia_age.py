# Calculate pooled mean and standard deviation of ages in anderson_2024
c1_age_mean = 19.10
c2_age_mean = 19.16

c1_age_sd = 1.25
c2_age_sd = 1.30

n1 = 1623
n2 = 964

n = n1 + n2

pooled_mean = (c1_age_mean * n1 + c2_age_mean * n2) / (n)

# 19.12
print(f"Pooled mean: {pooled_mean:.2f}")

c1_age_var = c1_age_sd ** 2
c2_age_var = c2_age_sd ** 2

pooled_var = (c1_age_var * (n1 - 1) + c2_age_var * (n2 - 1)) / (n1 + n2 - 2)

pooled_sd = pooled_var ** 0.5

# 1.27
print(f"Pooled sd: {pooled_sd:.2f}")


# sex composition:
n_male = (1623 * 0.581) + (964 * 0.6079)
n_female = n - n_male

print(n_male) # 1529
print(n_female) # 1058
