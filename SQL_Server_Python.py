from sqlalchemy import create_engine
import pandas as pd

# Replace with your SQL Server connection details
server = 'localhost'  # IP address and port of the Docker container
database = 'GAME'
username = 'sa'
password = 'reallyStrongPwd123'

# Create a connection string
conn_str = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"

# Create an engine
engine = create_engine(conn_str)

# Connect to the database
connection = engine.connect()
print(connection) # SQL SERVER IT HAS CONNECTED

# Read the CSV file
csv_file = '/Users/syedimad/Desktop/Data_Batch/data_sources/airbnb/listings.csv'
df_csv = pd.read_csv(csv_file) ##--> Extracting
#df_csv['price'] = df_csv['price'].fillna(0) ##--> Transform
# Update 'license' column: Replace null (NaN) values with 'Unknown'
df_csv.loc[df_csv['license'].isnull(), 'license'] = 'Unknown'

# Update 'license' column: Replace 'City registration pending' with 'License Pending'
df_csv.loc[df_csv['license'] == 'City registration pending', 'license'] = 'License Pending'

print("\n Data Read into Panda's Dataframe \n")
print("\n Ingesting into SQL Server \n")
# # Create a table in the database based on the CSV file
df_csv.to_sql('listings_detailed_cleansed', engine, if_exists='replace', index=False) ## --> Load

print("Table created successfully") 

query = 'select neighbourhood,avg(price) from dbo.listings group by neighbourhood'
df = pd.read_sql(query, engine)

print(df.head(10))