from itertools import product

import pandas as pd


def assign_matrix(*cols) -> pd.DataFrame:
    """
    Assigns a 0-1 matrix for each cols
    """
    list_0_1 = [*product([0, 1], repeat=len(cols))]
    return pd.DataFrame(list_0_1, columns=cols)
