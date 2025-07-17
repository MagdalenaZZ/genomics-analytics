# 👬 Genomics Analytics Toolkit

A modular Python toolkit for advanced population-level genomic analysis, supporting:

* ✅ Genome-Wide Association Studies (**GWAS**)
* ✅ Phenome-Wide Association Studies (**PheWAS**)
* ✅ Fine-mapping with **SuSiE**
* ✅ SNP ranking using P-values, PIPs, and effect sizes
* ⏳ Future: Selection scans, patient pairing, gene-based stats

---

## 📀 Project Structure

```
genomics-analytics/
├── notebooks/           # Demonstration scripts for each method
├── scripts/             # Command-line tools
├── src/                 # Core modules (gwas, phewas, fine_mapping, ml, etc.)
├── tests/               # Unit tests
└── results/             # Output files (created automatically)
```

---

## 🔧 Setup Instructions

```bash
conda create -n genomics python=3.11
conda activate genomics
pip install -r requirements.txt
conda install -c conda-forge rpy2 r-susier
```

Install MAGMA for here: https://cncr.nl/research/magma/
It gives you Generalized gene-set analysis of GWAS data. 

---

## 🔬 Example Analyses

### 1. Simulate GWAS

```bash
python notebooks/gwas_demo.py
```

* Outputs: `results/gwas_output.csv`

### 2. Run Fine-Mapping (SuSiE)

```bash
python notebooks/fine_mapping_demo.py
```

* Outputs:

  * `results/susie_pips.npy`
  * `results/susie_snps.npy`
  * `results/credible_sets.json`

### 3. Rank SNPs

```bash
python scripts/rank_snps.py \
  --gwas results/gwas_output.csv \
  --pips results/susie_pips.npy \
  --out ranked_snps.csv
```

* Output: `results/ranked_snps.csv`

### 4. PheWAS

```bash
python notebooks/phewas_demo.py
python notebooks/phewas_binary_demo.py
```

* Phenome-wide scans across simulated traits

---

## 📊 What Each Module Does

| Module          | Description                                                   |
| --------------- | ------------------------------------------------------------- |
| `gwas/`         | Linear model GWAS analysis and plotting                       |
| `phewas/`       | PheWAS across multiple simulated traits (binary + continuous) |
| `fine_mapping/` | SuSiE fine-mapping via `rpy2` and `susieR`                    |
| `ml/`           | SNP ranking and prioritization                                |
| `simulate/`     | Synthetic genotype + phenotype generation                     |
| `utils/`        | Genotype encoding and helpers                                 |

---

## 🚀 Roadmap

* [ ] Gene-based testing (e.g., MAGMA, SKAT)
* [ ] Polygenic Risk Scoring
* [ ] Population structure / selection (e.g., Fst, iHS)
* [ ] SHAP/XGBoost variant prioritization
* [ ] Web dashboard (Streamlit or Dash)

---

## 👥 Contributors

Built with ❤️ for reproducible genomic analysis.

---

## 📜 License

MIT License. Free to use, fork, and contribute.




