import pandas as pd
from data_analysis import fill_missing, plot_histogram, t_test

# Sample DataFrame for testing
df = pd.DataFrame({
    'age': [25, 30, None, 40, 50],
    'income': [50000, 60000, 55000, None, 65000]
})

# Data cleaning
df_clean = fill_missing(df)
print("Data after filling missing values:")
print(df_clean)

# Data visualization
plot_histogram(df_clean, 'age')

# Statistical analysis
t_stat, p_value = t_test(df_clean['age'].dropna(), df_clean['income'].dropna())
print(f"T-statistic: {t_stat}, P-value: {p_value}")
