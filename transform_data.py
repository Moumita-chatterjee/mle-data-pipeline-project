import pandas as pd

jan_df = pd.read_parquet("data/staging/green_tripdata_2025-01.parquet")
feb_df = pd.read_parquet("data/staging/green_tripdata_2025-02.parquet")
mar_df = pd.read_parquet("data/staging/green_tripdata_2025-03.parquet")
df = pd.concat([jan_df,feb_df,mar_df], ignore_index=True)
df = df[
    (df["lpep_pickup_datetime"] >= "2025-01-01")
    & (df["lpep_pickup_datetime"] < "2025-04-01")
]

df["pickup_date"] = df["lpep_pickup_datetime"].dt.date
print("Total rows after combining:", len(df))

print("Minimum pickup date:", df["lpep_pickup_datetime"].min())
print("Maximum pickup date:", df["lpep_pickup_datetime"].max())

df["pickup_date"] = df["lpep_pickup_datetime"].dt.date

daily_revenue = (
    df.groupby("pickup_date")["total_amount"].sum().reset_index()
)

daily_revenue = daily_revenue.rename(
    columns={"total_amount": "daily_revenue"}
)

print(daily_revenue.head())
print(daily_revenue.loc[30:35])
print(daily_revenue.tail())
print("Number of days:", len(daily_revenue))

