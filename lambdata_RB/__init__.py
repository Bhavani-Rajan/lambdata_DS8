"""
lambdata - a collection of data science helper function
"""
import pandas as pd
import numpy as np

# sample datasets
ONES = pd.DataFrame(np.ones(50))
ZEROS = pd.DataFrame(np.zeros(50))

# sample function

def increment(x):
    return (x+1)

def decrement(x):
    return (x-1)
