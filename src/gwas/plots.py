# src/gwas/plots.py
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def manhattan_plot(gwas_df):
    plt.figure(figsize=(10, 4))
    gwas_df["-log10P"] = -np.log10(gwas_df["P"])
    plt.scatter(range(len(gwas_df)), gwas_df["-log10P"], s=2)
    plt.xlabel("SNP Index")
    plt.ylabel("-log10(P)")
    plt.title("Manhattan Plot")
    plt.show()

def qq_plot(pvalues):
    pvalues = np.sort(pvalues)
    expected = -np.log10(np.linspace(1/len(pvalues), 1, len(pvalues)))
    observed = -np.log10(pvalues)
    plt.figure()
    plt.plot(expected, observed, 'o', markersize=2)
    plt.plot(expected, expected, 'r--')
    plt.xlabel("Expected -log10(P)")
    plt.ylabel("Observed -log10(P)")
    plt.title("QQ Plot")
    plt.show()


