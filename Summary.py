import pandas as pd

def summary_statistics(data):
    summary_stats = data.describe()
    return summary_stats

# Example usage:
data = pd.read_csv("data.csv")
summary_stats = summary_statistics(data)
print(summary_stats)
