# src/utils/genotype_encoding.py

import pandas as pd

def acgt_to_dosage(geno_df, snp_df):
    dosage_columns = []

    for snp in geno_df.columns:
        major = snp_df.loc[snp_df['SNP'] == snp, 'Major'].values[0]
        minor = snp_df.loc[snp_df['SNP'] == snp, 'Minor'].values[0]

        def count_minor(gt):
            return sum(1 for base in gt if base == minor)

        col = geno_df[snp].apply(count_minor)
        col.name = snp
        dosage_columns.append(col)

    encoded_df = pd.concat(dosage_columns, axis=1)
    return encoded_df

