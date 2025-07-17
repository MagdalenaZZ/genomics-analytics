import numpy as np
import pandas as pd
from rpy2.robjects import numpy2ri, r, pandas2ri
from rpy2.robjects.packages import importr

numpy2ri.activate()
pandas2ri.activate()

# Load susieR
susieR = importr("susieR")

def run_susie(geno_dosage_df, phenotype, L=10):
    """
    Run SuSiE fine-mapping using genotype dosages and phenotype values.
    
    Parameters:
        geno_dosage_df (DataFrame): SNP dosage matrix (n x p)
        phenotype (array-like): phenotype vector (length n)
        L (int): maximum number of causal variants to estimate
    
    Returns:
        dict: SuSiE output including credible sets and PIPs
    """
    X = geno_dosage_df.to_numpy(dtype=np.float64)
    #X = geno_dosage_df.to_numpy()
    #y = np.array(phenotype)
    y = np.array(phenotype, dtype=np.float64)
    susie_result = susieR.susie(X, y, L=L, verbose=False)
    
    # Extract Posterior Inclusion Probabilities (PIPs)
    pips = np.array(susie_result.rx2("pip"))
    cs = susie_result.rx2("sets")  # list of credible sets

    # Extract credible sets as a list of dicts
    credible_sets = []
    if "cs" in cs.names:
        for cs_set in cs.rx2("cs"):
            credible_sets.append(list(cs_set))

    return {
        "pips": pips,
        "credible_sets": credible_sets
    }



