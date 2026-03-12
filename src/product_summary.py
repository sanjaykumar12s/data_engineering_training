import csv
import os

# get current script directory
current_dir = os.path.dirname(__file__)

# build path to data file
file_path = os.path.join(current_dir, "..", "data", "products.csv")

total_rows = 0
categories = set()
total_price = 0

with open(file_path, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total_rows += 1
        categories.add(row["category"])
        total_price += float(row["price"])

average_price = total_price / total_rows

print("Total rows:", total_rows)
print("Unique categories:", categories)
print("Average price:", average_price)