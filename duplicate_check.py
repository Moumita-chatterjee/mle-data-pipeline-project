import pandas as pd

jan_file = "data/staging/green_tripdata_2025-01.parquet"
feb_file = "data/staging/green_tripdata_2025-02.parquet"

jan_df = pd.read_parquet(jan_file)
feb_df = pd.read_parquet(feb_file)

trip_columns = [
    "VendorID",
    "lpep_pickup_datetime",
    "lpep_dropoff_datetime",
    "PULocationID",
    "DOLocationID",
    "trip_distance",
    "total_amount",
]

jan_boundary = jan_df[
    jan_df["lpep_pickup_datetime"] >= "2025-01-31"
]

feb_boundary = feb_df[
    feb_df["lpep_pickup_datetime"] <= "2025-02-01 23:59:59"
]

matches = jan_boundary.merge(
    feb_boundary,
    on=trip_columns,
    how="inner",
)

print("January boundary records:", len(jan_boundary))
print("February boundary records:", len(feb_boundary))
print("Matching records:", len(matches))