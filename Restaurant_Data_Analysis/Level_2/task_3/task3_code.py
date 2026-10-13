import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv("../../Dataset.csv")

# Remove rows where latitude or longitude is missing
df = df.dropna(subset=["Latitude", "Longitude"])

# Plot restaurant locations
plt.scatter(df["Longitude"], df["Latitude"], s=10)

plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Restaurant Locations")

plt.show()

# Find restaurant clusters
# Divide the map into small areas
df["lat_area"] = df["Latitude"].round(2)
df["long_area"] = df["Longitude"].round(2)

# Count restaurants in each area
clusters = df.groupby(["lat_area", "long_area"]).size()

# Sort areas by number of restaurants
clusters = clusters.sort_values(ascending=False)

print("Areas with the highest number of restaurants:")
print(clusters.head(10 ))