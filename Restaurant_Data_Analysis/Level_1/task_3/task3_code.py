import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# reading the dataset
current_dir = Path(__file__).parent
project_folder = current_dir.parent.parent
df = pd.read_csv(project_folder / "Dataset.csv")

# number of restaurants in each price range
price_count = df["Price range"].value_counts().sort_index()

print("Number of restaurants in each price range:")
print(price_count)

# percentage
percent= (price_count / len(df)) * 100

print("\nPercentage of restaurants in each price range:")
print(percent.round(2))

# Creating a bar chart
plt.bar(price_count.index, price_count.values)

plt.xlabel("Price Range")
plt.ylabel("Number of Restaurants")
plt.title("Distribution of Price Range")

plt.show()