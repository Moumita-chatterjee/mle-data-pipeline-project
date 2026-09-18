import pandas as pd

file_path = "data/staging/green_tripdata_2025-01.parquet"

df = pd.read_parquet(file_path)

print("first 5 rows:", df.head(5))
print("\nColumns:")
print(df.columns)

print("\nShape:")
print(df.shape)

print("\nData types:")
print(df.dtypes)

revenue_columns = [
    "fare_amount","extra","mta_tax","tip_amount","tolls_amount","ehail_fee",
    "improvement_surcharge","total_amount","congestion_surcharge","cbd_congestion_fee",
]

print("\n revenue_columns: ", df[revenue_columns].head(10))