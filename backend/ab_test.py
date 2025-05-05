from statsmodels.stats.proportion import proportions_ztest

def perform_ab_test(df):
    conversions = df.groupby("group")["converted"].agg(["sum", "count"])
    count = conversions["sum"].values
    nobs = conversions["count"].values
    stat, pval = proportions_ztest(count, nobs)
    return {
        "z_stat": float(stat),
        "p_value": float(pval),
        "significant": pval < 0.05
    }
