# src/gwas/simulate.py
import numpy as np
import pandas as pd
from random import choice

def simulate_acgt_genotypes(n_individuals=100, n_snps=1000, seed=42):
    np.random.seed(seed)
    bases = ['A', 'C', 'G', 'T']
    geno_matrix = []
    snp_info = []

    for snp_id in range(n_snps):
        major = choice(bases)
        minor = choice([b for b in bases if b != major])
        maf = np.random.uniform(0.05, 0.5)  # realistic minor allele frequency

        # Hardy-Weinberg genotype frequencies
        p = 1 - maf
        q = maf
        freq = {
            f"{major}{major}": p**2,
            f"{major}{minor}": 2*p*q,
            f"{minor}{minor}": q**2
        }

        genotypes = np.random.choice(
            list(freq.keys()), 
            size=n_individuals, 
            p=list(freq.values())
        )

        geno_matrix.append(genotypes)
        snp_info.append((f"snp_{snp_id}", major, minor, maf))

    geno_df = pd.DataFrame(np.array(geno_matrix).T, columns=[snp[0] for snp in snp_info])
    snp_df = pd.DataFrame(snp_info, columns=["SNP", "Major", "Minor", "MAF"])
    return geno_df, snp_df

def simulate_phenotype(geno_df, causal_snps=None, noise=1.0):
    if causal_snps is None:
        causal_snps = geno_df.columns[:2]  # pick first 2 as causal

    def encode(g):  # Convert genotype to 0, 1, 2 based on minor allele count
        a1, a2 = g[0], g[1]
        return sum([1 if a == 'G' else 0 for a in (a1, a2)])  # Example: use 'G' as minor

    #encoded = geno_df[causal_snps].applymap(encode)
    encoded = geno_df[causal_snps].apply(lambda col: col.map(encode))
    genetic_score = encoded.sum(axis=1)
    phenotype = genetic_score + np.random.normal(0, noise, size=len(genetic_score))
    return phenotype


