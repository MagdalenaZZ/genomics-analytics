# 👬 Genomics Analytics Toolkit

A modular Python toolkit for demonstrating advanced population-level genomic analysis, supporting:

* ✅ Genome-Wide Association Studies (**GWAS**)
* ✅ Phenome-Wide Association Studies (**PheWAS**)
* ✅ Fine-mapping with **SuSiE**
* ✅ SNP ranking using P-values, PIPs, and effect sizes
* ⏳ Future: Selection scans, patient pairing, gene-based stats, full list in Docs/

This is not intended to be high-throughput, more as a showcase and learning tool around which problems we might come across in population studies, and how to statistically solve them, and quality check the data. There are probably much better resources for very high-throughput processing of 100,000s of thousands of genomes, and rich phenotypic data, which honestly, you'd want cloud-based, distributed, containerised, and with a powerful database storing your variants data.

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
conda env create -f environment.yml
conda activate py311
pip install -r requirements.txt
```

Install MAGMA for here: https://cncr.nl/research/magma/
It gives you a Generalized gene-set analysis of GWAS data. 

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
* [ ] SHAP/XGBoost variant prioritisation
* [ ] Web dashboard (Streamlit or Dash)

---

### ❓ **Example Problem: How do I analyze complex disorder genetics?**

**Context**: Complex disorders (e.g., diabetes, schizophrenia, asthma) are not caused by a single mutation. Instead, they:

* Do not follow Mendelian inheritance
* Are influenced by many variants with small effects
* Involve gene–environment interactions
* Show heritability, but have heterogeneous genetic causes and phenotype

**Approaches**:

* Perform **GWAS** to detect common variants with small effects
* Use **polygenic risk scores** to estimate cumulative risk
* Partition heritability to tissues/functions using methods like **LDSC**
* Explore gene–environment interactions and GxE models

**Statistical Tools**:

* `BOLT-LMM`, `SAIGE`, `REGENIE` for GWAS on large cohorts
* `PRSice-2`, `LDpred2`, `SBayesR` for polygenic scoring
* `LDSC`, `S-LDSC` for heritability partitioning
* `GEM`, `INTERSNP` for modeling GxE interactions

**Context**: You have raw variants or summary statistics and want to link them to genes, transcripts, functions, or predict deleteriousness.

**Approaches**:

* Annotate SNPs with gene and consequence information
* Filter by predicted impact or frequency (e.g., consider removing very common variants)
* Prioritize using conservation scores or deleteriousness predictors

**Statistical Tools**:

* `VEP` (Ensembl Variant Effect Predictor)
* `ANNOVAR` (multi-annotation framework)
* `SnpEff` (fast, locally runnable)
* `CADD`, `REVEL`, `PolyPhen-2`, `SIFT` (functional impact prediction)
* `dbNSFP` (integrated database of variant annotations)


---


## 📜 License

MIT License. Free to use, fork, and contribute.




