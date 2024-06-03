
import pandas as pd
import psycopg2
from zipfile import ZipFile

# Current issues:
# 1. Soon: do JSON instead of CSV. Staging table, or Pandas?
# 2. Data cleaning: Unix time, None as data, duplication (as noted from Web Robots)

db_host = "your_postgres_host"
db_name = "kickstarter"
db_user = ""
db_password = ""

# Connect to the Postgres database
conn = psycopg2.connect(
    host=db_host,
    database=db_name,
    user=db_user,
    password=db_password
)
cursor = conn.cursor()

try:
    # Open the input CSV file
    with ZipFile('kickstarter.zip') as zf:
        for file in zf.namelist():
            # File type filter
            if not file.endswith('.csv'):
                continue

            # Begin a transaction
            cursor.execute("BEGIN")

            df = pd.read_csv(file)
            print(df.head())

            with zf.open(file) as f:
                reader = csv.reader(f)
                
                # Skip the header row
                next(reader)
                
                # Iterate through each row and insert into the Postgres table
                for row in reader:
                    # Replace 'Null' with an empty string
                    cleaned_row = ['' if cell == 'Null' else cell for cell in row]
                    
                    # Insert the cleaned row into the Postgres table
                    cursor.execute("INSERT INTO your_table_name VALUES (%s, %s, %s)", cleaned_row)
    
            # Commit the changes
            cursor.execute("COMMIT")
            print(f"Sucessfully imported {file}")

except Exception as e:
    print("Error processing data. Rolling back transaction.")
    cursor.execute("ROLLBACK")
    print(e)

finally:
    # Close the cursor and connection
    cursor.close()
    conn.close()
