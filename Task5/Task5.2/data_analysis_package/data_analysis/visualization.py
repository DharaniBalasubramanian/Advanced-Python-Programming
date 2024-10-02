import matplotlib.pyplot as plt

def plot_histogram(data, column):
    """Generate a histogram for a specified column in the dataset."""
    plt.hist(data[column], bins=20, color='green', edgecolor='black')
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

def plot_scatter(data, col1, col2):
    """Generate a scatter plot between two columns."""
    plt.scatter(data[col1], data[col2], color='green')
    plt.title(f'Scatter plot between {col1} and {col2}')
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.show()
