import matplotlib.pyplot as plt
import numpy as np

def phewas_plot(results_df):
    results_df = results_df.sort_values("P")
    results_df["-log10P"] = -np.log10(results_df["P"])

    plt.figure(figsize=(10, 4))
    plt.scatter(range(len(results_df)), results_df["-log10P"], s=10)
    plt.axhline(-np.log10(0.05 / len(results_df)), color='red', linestyle='--')  # Bonferroni
    plt.xticks(ticks=range(len(results_df)), labels=results_df["Phenotype"], rotation=90)
    plt.ylabel("-log10(P)")
    plt.title("PheWAS Plot")
    plt.tight_layout()
    plt.show()

