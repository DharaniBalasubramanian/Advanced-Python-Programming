import pandas as pd
from data_analysis.cleaning import fill_missing, drop_duplicates

def test_fill_missing():
    df = pd.DataFrame({'A': [1, 2, None, 4]})
    result = fill_missing(df)
    assert result.isnull().sum().sum() == 0

def test_drop_duplicates():
    df = pd.DataFrame({'A': [1, 2, 2, 4]})
    result = drop_duplicates(df)
    assert result.shape[0] == 3