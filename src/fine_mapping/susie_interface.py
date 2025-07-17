import numpy as np
from rpy2.robjects import numpy2ri, pandas2ri
from rpy2.robjects.packages import importr
from rpy2.rinterface_lib.sexp import NULLType

numpy2ri.activate()
pandas2ri.activate()

susieR = importr("susieR")

def run_susie(geno_dosage_df, phenotype, L=10):
    X = geno_dosage_df.to_numpy(dtype=np.float64)
    y = np.array(phenotype, dtype=np.float64)

    susie_result = susieR.susie(X, y, L=L, verbose=False)
    pips = np.array(susie_result.rx2("pip"))
    
    # Get 'sets' object
    cs = susie_result.rx2("sets")
    credible_sets = []

    #  Guard clause for NULL object
    if isinstance(cs, NULLType):
        print("WARN: SuSiE returned no credible sets.")
    else:
        cs_names = list(cs.names)
        if "cs" in cs_names:
            cs_list = cs.rx2("cs")
            if isinstance(cs_list, NULLType):
                print("WARN: 'sets$cs' exists but is NULL.")
            else:
                for cs_set in cs_list:
                    credible_sets.append(list(cs_set))

    return {
        "pips": pips,
        "credible_sets": credible_sets
    }


