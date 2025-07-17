import sys, os
sys.path.append(os.path.abspath("src"))

from simulate.simulate import simulate_acgt_genotypes
from utils.genotype_encoding import acgt_to_dosage
from phewas.simulate_phenos import simulate_binary_phenotypes
from phewas.phewas_runner import run_phewas
from phewas.plots import phewas_plot

# Step 1: Simulate genotypes
geno_df, snp_df = simulate_acgt_genotypes(n_individuals=100, n_snps=20)
geno_dosage_df = acgt_to_dosage(geno_df, snp_df)

# Step 2: Simulate binary phenotypes
pheno_df, causal_binary_idxs = simulate_binary_phenotypes(geno_dosage_df, snp_name="snp_10", n_phenos=50)
binary_pheno_names = pheno_df.columns.tolist()

# Step 3: Run logistic regression PheWAS
results = run_phewas(geno_dosage_df, pheno_df, snp_name="snp_10", binary_phenos=binary_pheno_names)

# Step 4: Plot results
phewas_plot(results)

# Print causal phenotype names
print("Causal binary phenos:", [binary_pheno_names[i] for i in causal_binary_idxs])
print(results.sort_values("P").head())


