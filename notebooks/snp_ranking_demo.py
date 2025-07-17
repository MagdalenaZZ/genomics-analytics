import sys, os
sys.path.append(os.path.abspath("src"))


from ml.snp_ranker import rank_snps

# gwas_df: from your GWAS pipeline
# susie_pips: from SuSiE output
ranked_df = rank_snps(gwas_df, susie_pips)

print(ranked_df.head())


