#!/usr/bin/env python

import argparse
import os
import pandas as pd
import numpy as np
from pathlib import Path
import sys

# Add src to path
sys.path.append(os.path.abspath("src"))
from ml.snp_ranker import rank_snps

def main():
    parser = argparse.ArgumentParser(description="Rank SNPs using GWAS + SuSiE PIPs.")
    parser.add_argument("--gwas", required=True, help="Path to GWAS results CSV (with columns SNP, P, Beta)")
    parser.add_argument("--pips", required=False, help="Optional: Path to SuSiE PIPs as .npy or CSV file")
    parser.add_argument("--out", default="ranked_snps.csv", help="Filename for ranked output CSV")
    parser.add_argument("--results_dir", default="results", help="Folder to store results")

    args = parser.parse_args()

    # Ensure results directory exists
    Path(args.results_dir).mkdir(parents=True, exist_ok=True)

    # Load GWAS data
    gwas_df = pd.read_csv(args.gwas)
    if "SNP" not in gwas_df.columns or "P" not in gwas_df.columns or "Beta" not in gwas_df.columns:
        raise ValueError("GWAS file must contain 'SNP', 'P', and 'Beta' columns.")

    susie_pips = None

    # If SuSiE PIPs are provided, align SNPs
    if args.pips:
        susie_snps_path = Path(args.results_dir) / "susie_snps.npy"
        if not susie_snps_path.exists():
            raise FileNotFoundError(f"Expected SNP list at {susie_snps_path} to align with PIPs.")

        # Load SNP names and PIPs
        susie_snps = np.load(susie_snps_path, allow_pickle=True)
        if args.pips.endswith(".npy"):
            susie_pips = np.load(args.pips)
        else:
            susie_pips = pd.read_csv(args.pips, header=None).squeeze().values

        # Filter and align GWAS to SuSiE SNPs
        gwas_df = gwas_df[gwas_df["SNP"].isin(susie_snps)].reset_index(drop=True)
        gwas_df = gwas_df.set_index("SNP").loc[susie_snps].reset_index()

    # Rank SNPs
    ranked_df = rank_snps(gwas_df, susie_pips)

    # Save to file
    out_path = Path(args.results_dir) / args.out
    ranked_df.to_csv(out_path, index=False)
    print(f"DONE Ranked SNPs saved to: {out_path}")

if __name__ == "__main__":
    main()

