import pandas as pd
from data_analysis.statistics import correlation, t_test

def test_correlation():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [1, 2, 3]})
    assert correlation(df, 'A', 'B') == 1.0

def test_t_test():
    sample1 = [1, 2, 3]
    sample2 = [4, 5, 6]
    t_stat, p_value = t_test(sample1, sample2)
    assert p_value > 0.05  # Arbitrary test, adjust for your data
