import pandas as pd
import os
current_dir = os.path.dirname(__file__) 
file_path = os.path.join(current_dir, "..", "data", "products.csv")

df = pd.read_csv(file_path)

total_rows = len(df)
unique_categories = df["category"].unique()
average_price = df["price"].mean()

print("Total rows:", total_rows)
print("Unique categories:", unique_categories)
print("Average price:", average_price)
