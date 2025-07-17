
# src/gwas/qc.py
import pandas as pd
import numpy as np

def maf_filter(geno_df, threshold=0.01):
    maf = geno_df.apply(lambda x: np.minimum(np.mean(x) / 2, 1 - np.mean(x) / 2))
    return geno_df.loc[:, maf > threshold]


