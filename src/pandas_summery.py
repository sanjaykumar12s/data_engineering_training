import pandas as pd
import os
import yaml
import logging

# find project root
current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, ".."))

# load configuration
config_path = os.path.join(project_root, "config", "config.yaml")

with open(config_path, "r") as file:
    config = yaml.safe_load(file)
    print(config)

data_path = os.path.join(project_root, config["input_file"])
output_path = os.path.join(project_root, config["output_file"])
log_path = os.path.join(project_root, config["log_file"])

# setup logging
logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Pipeline started")

try:
    df = pd.read_csv(data_path)
    logging.info("Data loaded")

    category_summary = df.groupby("category").agg(
        total_products=("product_id", "count"),
        average_price=("price", "mean"),
        max_price=("price", "max"),
        min_price=("price", "min")
    )

    category_summary.to_csv(output_path)

    logging.info("Data transformation completed")

except Exception as e:
    logging.error(f"Pipeline error: {e}")

logging.info("Pipeline finished")