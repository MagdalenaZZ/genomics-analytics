import sys
import os
sys.path.append(os.path.abspath("src"))

from simulate.simulate import simulate_acgt_genotypes, simulate_phenotype

def main():
    # Generate data
    print("Generating genotypes...")
    geno_df, snp_df = simulate_acgt_genotypes(n_individuals=10, n_snps=5)

    print("\nGenotype DataFrame (first 5 rows):")
    print(geno_df.head())

    print("\nSNP Metadata:")
    print(snp_df)

    # Simulate phenotype using the first two SNPs as causal
    print("\nSimulating phenotype...")
    phenotype = simulate_phenotype(geno_df, causal_snps=geno_df.columns[:2])
    
    print("\nPhenotype values:")
    print(phenotype.head())

    print("\nEverything looks good!")

if __name__ == "__main__":
    main()



