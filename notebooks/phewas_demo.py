import sys, os
sys.path.append(os.path.abspath("src"))

from simulate.simulate import simulate_acgt_genotypes
from utils.genotype_encoding import acgt_to_dosage
from phewas.simulate_phenos import simulate_multiple_phenotypes
from phewas.phewas_runner import run_phewas
from phewas.plots import phewas_plot

# simulate genotype
geno_df, snp_df = simulate_acgt_genotypes(n_individuals=100, n_snps=20)
geno_dosage_df = acgt_to_dosage(geno_df, snp_df)

# simulate phenotypes
pheno_df, causal_idxs = simulate_multiple_phenotypes(geno_dosage_df, snp_name="snp_10", n_phenos=50)

# run phewas
results = run_phewas(geno_dosage_df, pheno_df, snp_name="snp_10")

# plot
phewas_plot(results)
print("Causal phenotypes (indexes):", causal_idxs)
print(results.sort_values("P").head())

