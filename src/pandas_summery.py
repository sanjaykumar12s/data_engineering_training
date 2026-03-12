import pandas as pd
import os
import logging

# locate folders
current_dir = os.path.dirname(__file__)
data_path = os.path.join(current_dir, "..", "data", "products.csv")
log_path = os.path.join(current_dir, "..", "logs", "pipeline.log")

# configure logging
logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Pipeline started")

try:
    df = pd.read_csv(data_path)
    logging.info("CSV file loaded successfully")

    # basic validation
    if df["price"].isnull().any():
        logging.warning("Null values detected in price column")

    # transformation
    category_summary = df.groupby("category").agg(
        total_products=("product_id", "count"),
        average_price=("price", "mean"),
        max_price=("price", "max"),
        min_price=("price", "min")
    )

    output_path = os.path.join(current_dir, "..", "data", "category_summary.csv")
    category_summary.to_csv(output_path)

    logging.info("Aggregation completed and file saved")

except Exception as e:
    logging.error(f"Pipeline failed: {e}")

logging.info("Pipeline finished")