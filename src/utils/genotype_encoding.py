import pandas as pd

def acgt_to_dosage(geno_df, snp_df):
    encoded_df = pd.DataFrame(index=geno_df.index)
    
    for snp in geno_df.columns:
        major = snp_df.loc[snp_df['SNP'] == snp, 'Major'].values[0]
        minor = snp_df.loc[snp_df['SNP'] == snp, 'Minor'].values[0]
        
        def count_minor(gt):
            return sum(1 for base in gt if base == minor)
        
        encoded_df[snp] = geno_df[snp].apply(count_minor)

    return encoded_df

