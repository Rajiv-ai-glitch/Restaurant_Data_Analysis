import pandas as pd

# Read the dataset
df = pd.read_csv("../Dataset.csv")

# Count restaurants
restaurant_count = df["Restaurant Name"].value_counts()

# Find restaurant chains
chains = restaurant_count[restaurant_count > 1]

print("Restaurant chains:")
print(chains)

# Analyze ratings and popularity
# using votes as a measure of popularity
chain_analysis = df.groupby("Restaurant Name").agg({
    "Aggregate rating": "mean",
    "Votes": "sum"
})

# Keep only restaurant chains
chain_analysis = chain_analysis.loc[chains.index]

print("\nRatings and popularity of restaurant chains:")
print(chain_analysis.sort_values("Votes", ascending=False).head(10))