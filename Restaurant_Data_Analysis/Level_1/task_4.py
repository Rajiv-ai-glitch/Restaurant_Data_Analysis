import pandas as pd
from pathlib import Path

current_dir = Path(__file__).parent
project_folder = current_dir.parent
df = pd.read_csv(project_folder / "Dataset.csv")

# Count restaurants with and without online delivery
delivery_count = df["Has Online delivery"].value_counts()

# Calculate percentage
percentage = (delivery_count / len(df)) * 100

print("Percentage of restaurants:")
print(percentage.round(2))

# Compare average ratings
average_rating = df.groupby("Has Online delivery")["Aggregate rating"].mean()

print("\nAverage rating comparison:")
print("With online delivery:",round(average_rating["Yes"], 2))
print("Without online delivery:",round(average_rating["No"], 2))