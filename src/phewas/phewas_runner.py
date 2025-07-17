import statsmodels.api as sm
import pandas as pd

def run_phewas(geno_dosage_df, pheno_df, snp_name='snp_10', binary_phenos=None):
    """
    Run a PheWAS scan using linear or logistic regression depending on phenotype type.

    Args:
        geno_dosage_df (DataFrame): SNP dosages
        pheno_df (DataFrame): Phenotypes (each column is a trait)
        snp_name (str): SNP to scan
        binary_phenos (list): List of phenotype names to treat as binary

    Returns:
        DataFrame: Summary table with Beta, P-values, etc.
    """
    results = []
    snp_dosage = geno_dosage_df[snp_name]
    binary_phenos = binary_phenos or []

    for pheno in pheno_df.columns:
        X = sm.add_constant(snp_dosage)
        y = pheno_df[pheno]

        if pheno in binary_phenos:
            model = sm.Logit(y, X).fit(disp=False)
        else:
            model = sm.OLS(y, X).fit()

        results.append({
            'Phenotype': pheno,
            'Type': 'binary' if pheno in binary_phenos else 'continuous',
            'Beta': model.params[snp_name],
            'P': model.pvalues[snp_name]
        })

    return pd.DataFrame(results)



