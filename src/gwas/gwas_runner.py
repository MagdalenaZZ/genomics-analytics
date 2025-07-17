import statsmodels.api as sm
import pandas as pd

def run_gwas_dosage(geno_dosage_df, phenotype):
    results = []
    for snp in geno_dosage_df.columns:
        X = sm.add_constant(geno_dosage_df[snp])
        model = sm.OLS(phenotype, X).fit()
        pval = model.pvalues[snp]
        beta = model.params[snp]
        results.append({"SNP": snp, "Beta": beta, "P": pval})
    return pd.DataFrame(results)


