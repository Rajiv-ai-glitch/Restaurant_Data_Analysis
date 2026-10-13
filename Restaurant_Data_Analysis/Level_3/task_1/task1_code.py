import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv("../../Dataset.csv")

# Remove missing reviews
df = df.dropna(subset=["Rating text"])

# Convert reviews to lowercase
reviews = df["Rating text"].str.lower()


# -------------------------------
# 1. Common positive keywords
# -------------------------------

positive_words = [
    "excellent",
    "very good",
    "good",
    "great",
    "amazing",
    "awesome",
    "wonderful"
]

positive_count = {}

for word in positive_words:
    positive_count[word] = reviews.str.contains(word).sum()

positive_count = pd.Series(positive_count).sort_values(ascending=False)

print("Most common positive keywords:")
print(positive_count)


# -------------------------------
# 2. Common negative keywords
# -------------------------------

negative_words = [
    "poor",
    "bad",
    "terrible",
    "average",
    "not good",
    "worst"
]

negative_count = {}

for word in negative_words:
    negative_count[word] = reviews.str.contains(word).sum()

negative_count = pd.Series(negative_count).sort_values(ascending=False)

print("\nMost common negative keywords:")
print(negative_count)


# -------------------------------
# 3. Average review length
# -------------------------------

df["Review Length"] = df["Rating text"].str.len()

average_length = df["Review Length"].mean()

print("\nAverage review length:")
print(round(average_length, 2))


# -------------------------------
# 4. Review length vs rating
# -------------------------------

average_review_length = df.groupby("Aggregate rating")["Review Length"].mean()

print("\nAverage review length for each rating:")
print(average_review_length.round(2))


# Create a graph
plt.scatter(df["Review Length"], df["Aggregate rating"], s=10)

plt.xlabel("Review Length")
plt.ylabel("Aggregate Rating")
plt.title("Review Length vs Rating")

plt.show()