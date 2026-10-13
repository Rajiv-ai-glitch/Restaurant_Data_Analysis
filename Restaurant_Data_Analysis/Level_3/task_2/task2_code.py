import pandas as pd
import matplotlib.pyplot as plt
# Read the dataset
df = pd.read_csv("../../Dataset.csv")

# Find restaurant with the highest number of votes
highest_votes = df.loc[df["Votes"].idxmax()]

print("Restaurant with highest votes:")
print(highest_votes["Restaurant Name"])
print("Votes:", highest_votes["Votes"])

# Find restaurant with the lowest number of votes
lowest_votes = df.loc[df["Votes"].idxmin()]

print("\nRestaurant with lowest votes:")
print(lowest_votes["Restaurant Name"])
print("Votes:", lowest_votes["Votes"])

# Calculate correlation between votes and rating
correlation = df["Votes"].corr(df["Aggregate rating"])

print("\nCorrelation between votes and rating:")
print(round(correlation, 2))

# create a scatter plot to visualize the relationship between votes and rating

plt.scatter(df["Votes"], df["Aggregate rating"], s = 10)
plt.xlabel("Number of Votes")
plt.ylabel("Aggregate Rating")
plt.title("Votes vs Restaurant Rating")

plt.show()