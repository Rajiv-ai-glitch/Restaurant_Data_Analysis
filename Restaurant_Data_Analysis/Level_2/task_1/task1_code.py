import pandas as pd

df = pd.read_csv("../../Dataset.csv")

# Display basic information
print("Dataset Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

# --------------------------------------------------
# 1. Distribution of Aggregate Ratings
# --------------------------------------------------

print("\nAggregate Rating Distribution:")
print(df["Aggregate rating"].value_counts().sort_index())

# Create rating ranges
bins = [-0.01, 1, 2, 3, 4, 5]
labels = ["0-1", "1-2", "2-3", "3-4", "4-5"]

df["Rating Range"] = pd.cut(
    df["Aggregate rating"],
    bins=bins,
    labels=labels,
    include_lowest=True
)

# Count restaurants in each rating range
rating_distribution = df["Rating Range"].value_counts().sort_index()

print("\nRating Range Distribution:")
print(rating_distribution)

# Find most common rating range
most_common_range = rating_distribution.idxmax()
most_common_count = rating_distribution.max()

print("\nMost Common Rating Range:", most_common_range)
print("Number of Restaurants:", most_common_count)

# --------------------------------------------------
# 2. Average Number of Votes
# --------------------------------------------------

average_votes = df["Votes"].mean()

print("\nAverage Number of Votes:", round(average_votes, 2))

