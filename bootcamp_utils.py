"""Useful functions constructed during the programming bootcamp"""

import numpy as np


# Construct an empirical cumulative distribution function (ECDF)
def ecdf(data):
    x = np.sort(data)
    y = np.arange(1, len(data) + 1, dtype=float)/len(data)
    return x, y
