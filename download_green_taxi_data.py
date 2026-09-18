import requests

months =["01","02","03"]
for month in months:
    filename = f"green_tripdata_2025-{month}.parquet"
    url =f"https://d37ci6vzurychx.cloudfront.net/trip-data/{filename}"
    response = requests.get(url)
    print(response.status_code)

    with open(f"data/staging/{filename}", "wb") as file:
        file.write(response.content)