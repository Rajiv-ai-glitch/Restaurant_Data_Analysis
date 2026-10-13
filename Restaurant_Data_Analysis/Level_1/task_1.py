import pandas as pd
from pathlib import Path

current_dir = Path(__file__).parent
project_folder = current_dir.parent
df = pd.read_csv(project_folder / "Dataset.csv")

# the most common cuisines
cuisine_counts = df["Cuisines"].value_counts()

# the top 3 cuisines
top_3 = cuisine_counts.head(3)

# Calculating percentage of restaurants that serve that cuisine
percentage = (top_3 / len(df)) * 100

# Creating result table
result = pd.DataFrame({
    "Cuisine": top_3.index,
    "Count": top_3.values,
    "Percentage": percentage.values
})

print(result)