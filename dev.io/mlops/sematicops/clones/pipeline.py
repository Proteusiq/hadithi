"""
This is the module in which you define your pipeline functions.

Feel free to break these definitions into as many files as you want for your
preferred code structure.
"""

# Sematic
import sematic
import pandas as pd
from .rio import load_data


@sematic.func
def pipeline() -> pd.DataFrame:
    """
    The root function of the pipeline.
    """

    df_X, df_y = load_data().set(name="Load Penguins", tags=["data loading"])
    return df_X
