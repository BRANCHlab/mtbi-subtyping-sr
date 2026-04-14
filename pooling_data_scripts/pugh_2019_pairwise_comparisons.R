outcome_df <- data.frame(
    "moh1" = c(833, 598, 3082, 207),
    "moh_decline2" = c(769, 494, 2702, 242),
    "mental_health3" = c(1259, 1082, 4788, 434),
    "pt_improve4" = c(255, 162, 1584, 143),
    "pt5" = c(687, 437, 2694, 279)
)
rownames(outcome_df) <- c("srb", "overdose", "homelessness", "mortality")

sample_size_df <- data.frame(
    "moh1" = 29168,
    "moh_decline2" = 17706,
    "mental_health3" = 28268,
    "pt_improve4" = 16538,
    "pt5" = 11333
)

clusters <- names(outcome_df)
outcomes <- rownames(outcome_df)

cluster_pairs <- combn(5, 2)

outcome_df["overdose", ]

sample_size_df[, "moh1"]

pval_df <- data.frame()
for (col in seq_len(ncol(cluster_pairs))) {
    c1_id <- cluster_pairs[1, col]
    c2_id <- cluster_pairs[2, col]
    c1 <- clusters[c1_id]
    c2 <- clusters[c2_id]
    for (outcome in outcomes) {
        c1_cases <- outcome_df[outcome, c1]
        c1_n <- sample_size_df[, c1]
        c2_cases <- outcome_df[outcome, c2]
        c2_n <- sample_size_df[, c2]
        pval <- pairwise.prop.test(x = c(c1_cases, c2_cases), n = c(c1_n, c2_n), correct = FALSE)$"p.value"
        this_df <- data.frame(
            outcome = outcome,
            c1 = c1,
            c2 = c2,
            pval = as.numeric(pval)
        )
        pval_df <- rbind(pval_df, this_df)
    }
}
pval_df$"p_adj" <- p.adjust(pval_df$"pval", method = "fdr")
dplyr::filter(pval_df, p_adj < 0.05) |>
    dplyr::select(-pval)


