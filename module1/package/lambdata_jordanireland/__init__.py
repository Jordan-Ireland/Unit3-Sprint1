name = "jordanireland"

import pandas as pd

def null_check(dataframe):
    na_values = dataframe[dataframe.isna().any(axis=1)]
    na_sum = len(na_values)

    print(f'The total number of null or n/a values in your dataframe is {na_sum}. They are \n{na_values}')