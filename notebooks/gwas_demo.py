
import sys, os
import pandas as pd
from pathlib import Path

sys.path.append(os.path.abspath("src"))

from simulate.simulate import simulate_acgt_genotypes, simulate_phenotype
from utils.genotype_encoding import acgt_to_dosage
from gwas.gwas_runner import run_gwas_dosage
from gwas.plots import manhattan_plot, qq_plot

geno_df, snp_df = simulate_acgt_genotypes(n_individuals=100, n_snps=1000)
phenotype = simulate_phenotype(geno_df, causal_snps=geno_df.columns[:2])
geno_dosage_df = acgt_to_dosage(geno_df, snp_df)

# Create results directory
Path("results").mkdir(exist_ok=True)

gwas_results = run_gwas_dosage(geno_dosage_df, phenotype)
manhattan_plot(gwas_results)
qq_plot(gwas_results["P"])

# Save GWAS results
gwas_results.to_csv("results/gwas_output.csv", index=False)
print("GWAS results saved to results/gwas_output.csv")


