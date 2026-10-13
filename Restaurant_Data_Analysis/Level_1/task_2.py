import pandas as pd
from pathlib import Path

current_dir = Path(__file__).parent
project_folder = current_dir.parent
df = pd.read_csv(project_folder / "Dataset.csv")

# 1. city with the highest number of restaurants
city_count = df["City"].value_counts()

print("City with highest number of restaurants:")
print(city_count.head(1))


# 2. Average rating of restaurants in each city
average_rating = df.groupby("City")["Aggregate rating"].mean()

print("\nAverage rating of each city:")
print(average_rating)


# 3. city with the highest average rating
highest_rating_city = average_rating.idxmax()
highest_rating = average_rating.max()

print("\nCity with highest average rating:")
print(highest_rating_city)
print("Average rating:", highest_rating)