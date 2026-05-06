bin_1_age = 12.6
bin_2_age = 14.6
bin_3_age = 16.6

bin_1_sd = 0.02
bin_2_sd = 0.01
bin_3_sd = 0.01

bin_1_n = 1132
bin_2_n = 5562
bin_3_n = 5294

overall_age = ((bin_1_age * bin_1_n) + (bin_2_age * bin_2_n) + (bin_3_age * bin_3_n)) / (bin_1_n + bin_2_n + bin_3_n)

overall_age #15.29

overall_var = (bin_1_sd ** 2 * (bin_1_n - 1) + bin_2_sd ** 2 * (bin_2_n - 1) + bin_3_sd ** 2 * (bin_3_n - 1)) / (bin_1_n + bin_2_n + bin_3_n - 3)

overall_sd = overall_var ** 0.5

overall_sd # 0.01
