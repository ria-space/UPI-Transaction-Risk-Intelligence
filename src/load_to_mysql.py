import pandas as pd
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

# 1. Load the processed CSV
csv_path = "data/processed/upi_transactions_risk_scored.csv"
df = pd.read_csv(csv_path)

print("CSV loaded successfully.")
print("Rows:", len(df))
print("Columns:", len(df.columns))

# 2. Connect to MySQL
connection = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
)

cursor = connection.cursor()
print("Connected to MySQL successfully.")

# --------------------------------------------------
# 3. Insert data
# --------------------------------------------------

insert_query = """
INSERT INTO upi_transactions (
    transaction_id,
    transaction_timestamp,
    transaction_type,
    merchant_category,
    amount_inr,
    transaction_status,
    sender_age_group,
    receiver_age_group,
    sender_state,
    sender_bank,
    receiver_bank,
    device_type,
    network_type,
    fraud_flag,
    hour_of_day,
    day_of_week,
    is_weekend,
    amount_band,
    amount_log,
    time_period,
    weekend_evening,
    high_value_flag,
    risk_score,
    risk_tier
)
VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s
)
"""


# --------------------------------------------------
# 4. Convert dataframe rows to MySQL-friendly values
# --------------------------------------------------

data = []

for _, row in df.iterrows():

    data.append((
        row["transaction id"],
        pd.to_datetime(row["timestamp"]).to_pydatetime(),
        row["transaction type"],
        row["merchant_category"],
        float(row["amount (INR)"]),
        row["transaction_status"],
        row["sender_age_group"],
        row["receiver_age_group"],
        row["sender_state"],
        row["sender_bank"],
        row["receiver_bank"],
        row["device_type"],
        row["network_type"],
        int(row["fraud_flag"]),
        int(row["hour_of_day"]),
        row["day_of_week"],
        int(row["is_weekend"]),
        row["amount_band"],
        float(row["amount_log"]),
        row["time_period"],
        int(row["weekend_evening"]),
        int(row["high_value_flag"]),
        int(row["risk_score"]),
        row["risk_tier"]
    ))


# --------------------------------------------------
# 5. Insert in batches
# --------------------------------------------------

batch_size = 5000

for start in range(0, len(data), batch_size):

    batch = data[start:start + batch_size]

    cursor.executemany(insert_query, batch)
    connection.commit()

    print(
        f"Inserted {min(start + batch_size, len(data)):,} "
        f"of {len(data):,} rows"
    )


# --------------------------------------------------
# 6. Close connection
# --------------------------------------------------

cursor.close()
connection.close()

print()
print("========================================")
print("IMPORT COMPLETED SUCCESSFULLY")
print("========================================")
