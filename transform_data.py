import os
import pandas as pd

def extract():
    "Read the staged files from Jan-March"
    jan_df = pd.read_parquet("data/staging/green_tripdata_2025-01.parquet")
    feb_df = pd.read_parquet("data/staging/green_tripdata_2025-02.parquet")
    mar_df = pd.read_parquet("data/staging/green_tripdata_2025-03.parquet")

    df = pd.concat([jan_df,feb_df,mar_df], ignore_index=True)

    print(f"Extracted {len(df)} rows")

    return df


def transform(df):

    df = df[
        (df["lpep_pickup_datetime"] >= "2025-01-01")
        & (df["lpep_pickup_datetime"] < "2025-04-01")
    ]

    df["pickup_date"] = df["lpep_pickup_datetime"].dt.date

    daily_revenue = (
    df.groupby("pickup_date")["total_amount"].sum().reset_index()
)

    daily_revenue = daily_revenue.rename(
        columns={"total_amount": "daily_revenue"}
    )
    print(f"Transformed data into {len(daily_revenue)} daily records")

    return daily_revenue


def load(daily_revenue):
    #save the output to csv file
    os.makedirs("data/output", exist_ok=True)

    daily_revenue.to_csv(
        "data/output/daily_revenue.csv", index=False
    )

    print("Daily revenue saved to data/output/daily_revenue.csv")


def main():
    df = extract()
    daily_revenue = transform(df)
    load(daily_revenue)

    print("pipeline done")

if __name__ == "__main__":
    main()


