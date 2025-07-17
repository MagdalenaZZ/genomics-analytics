import numpy as np
import pandas as pd

def simulate_multiple_phenotypes(geno_dosage_df, snp_name='snp_10', n_phenos=100, seed=42):
    np.random.seed(seed)
    n_individuals = geno_dosage_df.shape[0]
    snp_dosage = geno_dosage_df[snp_name].values

    phenos = {}
    causal_idxs = np.random.choice(n_phenos, size=5, replace=False)  # 5 causal phenos

    for i in range(n_phenos):
        noise = np.random.normal(0, 1, size=n_individuals)
        if i in causal_idxs:
            # causal phenotypes: SNP has real effect
            beta = np.random.uniform(0.5, 1.5)
            y = snp_dosage * beta + noise
        else:
            # null phenotypes: just noise
            y = noise
        phenos[f'pheno_{i}'] = y

    pheno_df = pd.DataFrame(phenos)
    return pheno_df, causal_idxs

def simulate_binary_phenotypes(geno_dosage_df, snp_name='snp_10', n_phenos=50, seed=123):
    np.random.seed(seed)
    n_individuals = geno_dosage_df.shape[0]
    snp_dosage = geno_dosage_df[snp_name].values
    phenos = {}
    causal_idxs = np.random.choice(n_phenos, size=5, replace=False)

    for i in range(n_phenos):
        if i in causal_idxs:
            log_odds = snp_dosage * np.random.uniform(0.8, 1.5)
        else:
            log_odds = np.random.normal(0, 1, size=n_individuals)
        prob = 1 / (1 + np.exp(-log_odds))
        y = np.random.binomial(1, prob)
        phenos[f'pheno_{i}'] = y

    return pd.DataFrame(phenos), causal_idxs


