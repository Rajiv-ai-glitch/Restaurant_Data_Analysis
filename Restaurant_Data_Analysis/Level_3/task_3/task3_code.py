import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv("../../Dataset.csv")

# Group by price range and online delivery
delivery = pd.crosstab(
    df["Price range"],
    df["Has Online delivery"],
    normalize="index"
) * 100

print("Online delivery availability by price range:")
print(delivery.round(2))

# Group by price range and table booking
table_booking = pd.crosstab(
    df["Price range"],
    df["Has Table booking"],
    normalize="index"
) * 100

print("\nTable booking availability by price range:")
print(table_booking.round(2))

# Create a graph for online delivery
delivery.plot(kind="bar")

plt.xlabel("Price Range")
plt.ylabel("Percentage of Restaurants")
plt.title("Price Range vs Online Delivery")
plt.legend(title="Online Delivery")
plt.xticks(rotation=0)
plt.show()

# Create a graph for table booking
table_booking.plot(kind="bar")

plt.xlabel("Price Range")
plt.ylabel("Percentage of Restaurants")
plt.title("Price Range vs Table Booking")
plt.legend(title="Table Booking")
plt.xticks(rotation=0)
plt.show()

# Check whether higher-priced restaurants are more likely
# to offer online delivery and table booking

print("\nOnline delivery percentage by price range:")
print(delivery["Yes"].round(2))

print("\nTable booking percentage by price range:")
print(table_booking["Yes"].round(2))

# Compare the lowest and highest price ranges
lowest_price_delivery = delivery.loc[1, "Yes"]
highest_price_delivery = delivery.loc[4, "Yes"]

lowest_price_booking = table_booking.loc[1, "Yes"]
highest_price_booking = table_booking.loc[4, "Yes"]

print("\nComparison:")

if highest_price_delivery > lowest_price_delivery:
    print("Higher-priced restaurants are more likely to offer online delivery.")
else:
    print("Higher-priced restaurants are not more likely to offer online delivery.")

if highest_price_booking > lowest_price_booking:
    print("Higher-priced restaurants are more likely to offer table booking.")
else:
    print("Higher-priced restaurants are not more likely to offer table booking.")