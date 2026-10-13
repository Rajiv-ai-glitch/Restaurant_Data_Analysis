import pandas as pd

# Read the dataset
df = pd.read_csv("../Dataset.csv")

# Count the most common cuisine combinations
cuisine_count = df["Cuisines"].value_counts()

print("Most common cuisine combinations:")
print(cuisine_count.head(10))

# Calculate average rating for each cuisine combination
cuisine_rating = df.groupby("Cuisines")["Aggregate rating"].mean()

# Sort by highest average rating
cuisine_rating = cuisine_rating.sort_values(ascending=False)

print("\nCuisine combinations with highest average ratings:")
print(cuisine_rating.head(10))