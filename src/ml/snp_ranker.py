import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def rank_snps(
    gwas_df: pd.DataFrame,
    susie_pips: np.ndarray = None,
    additional_features: pd.DataFrame = None,
    scoring_weights: dict = None
) -> pd.DataFrame:
    """
    Rank SNPs based on GWAS, fine-mapping, and optional additional features.

    Args:
        gwas_df (pd.DataFrame): GWAS results with columns ['SNP', 'P', 'Beta']
        susie_pips (np.ndarray): Posterior inclusion probabilities (PIPs) from SuSiE
        additional_features (pd.DataFrame): Optional additional SNP-level features
        scoring_weights (dict): Weights for each feature, e.g. {"pval": 0.5, "pip": 0.3, "effect": 0.2}

    Returns:
        pd.DataFrame: Ranked SNPs with scoring breakdown
    """
    df = gwas_df.copy()
    scaler = MinMaxScaler()

    # 1. Add -log10(P)
    df["-log10P"] = -np.log10(df["P"])
    df["pval_score"] = scaler.fit_transform(df[["-log10P"]])

    # 2. Add effect size score (absolute value)
    df["effect_score"] = scaler.fit_transform(df[["Beta"]].abs())

    # 3. Add SuSiE PIPs (if available)
    if susie_pips is not None:
        df["pip"] = susie_pips
        df["pip_score"] = scaler.fit_transform(df[["pip"]])
    else:
        df["pip_score"] = 0.0

    # 4. Merge additional features (optional)
    if additional_features is not None:
        df = df.merge(additional_features, on="SNP", how="left")
        # Normalize all numeric features
        for col in additional_features.columns:
            if col != "SNP" and pd.api.types.is_numeric_dtype(df[col]):
                df[col + "_score"] = scaler.fit_transform(df[[col]])

    # 5. Weighted scoring
    weights = scoring_weights or {"pval": 0.5, "pip": 0.3, "effect": 0.2}
    df["combined_score"] = (
        weights.get("pval", 0) * df["pval_score"] +
        weights.get("pip", 0) * df["pip_score"] +
        weights.get("effect", 0) * df["effect_score"]
    )

    df = df.sort_values("combined_score", ascending=False).reset_index(drop=True)
    return df


