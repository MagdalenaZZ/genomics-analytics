import sys, os
import numpy as np
from pathlib import Path
sys.path.append(os.path.abspath("src"))

Path("results").mkdir(exist_ok=True)

from simulate.simulate import simulate_acgt_genotypes, simulate_phenotype
from utils.genotype_encoding import acgt_to_dosage
from fine_mapping.susie_interface import run_susie
import matplotlib.pyplot as plt

# Simulate data
geno_df, snp_df = simulate_acgt_genotypes(n_individuals=100, n_snps=100)
phenotype = simulate_phenotype(geno_df, causal_snps=["snp_10", "snp_20"])
geno_dosage_df = acgt_to_dosage(geno_df, snp_df)
np.save("results/susie_snps.npy", geno_dosage_df.columns.values)
print("SNP list saved to results/susie_snps.npy")

# Run SuSiE
result = run_susie(geno_dosage_df, phenotype, L=5)

# Save PIPs and optional credible set info
np.save("results/susie_pips.npy", result["pips"])
print("SuSiE PIPs saved to results/susie_pips.npy")

# Save credible sets as JSON (optional)
import json
with open("results/credible_sets.json", "w") as f:
    json.dump(result["credible_sets"], f, indent=2)

# Visualize PIPs
import numpy as np
plt.figure(figsize=(10, 4))
plt.bar(range(len(result["pips"])), result["pips"])
plt.title("Posterior Inclusion Probabilities (PIPs)")
plt.xlabel("SNP Index")
plt.ylabel("PIP")
plt.show()

print("Credible Sets:")
for i, cs in enumerate(result["credible_sets"]):
    print(f"Set {i+1}: SNPs {cs}")

