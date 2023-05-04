
import boto3
import pandas as pd
import snowflake.connector

# set up AWS and Snowflake credentials

snowflake_user = 'YOUR_SNOWFLAKE_USER'
snowflake_password = 'YOUR_SNOWFLAKE_PASSWORD'
snowflake_account = 'YOUR_SNOWFLAKE_ACCOUNT'
snowflake_database = 'YOUR_SNOWFLAKE_DATABASE'
snowflake_schema = 'YOUR_SNOWFLAKE_SCHEMA'
snowflake_table = 'YOUR_SNOWFLAKE_TABLE'

# connect to S3 and read CSV file into Pandas DataFrame
s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)
s3_object = s3.get_object(Bucket=s3_bucket, Key='path/to/your/csv/file.csv')
df = pd.read_csv(s3_object['Body'])

# connect to Snowflake and create new table
snowflake_conn = snowflake.connector.connect(
    user=snowflake_user,
    password=snowflake_password,
    account=snowflake_account,
    database=snowflake_database,
    schema=snowflake_schema
)
snowflake_cursor = snowflake_conn.cursor()
snowflake_cursor.execute(f"CREATE TABLE {snowflake_table} (COLUMN1 VARCHAR, COLUMN2 VARCHAR, COLUMN3 VARCHAR, COLUMN4 VARCHAR)")

# load data into Snowflake table using pandas DataFrame
df.to_sql(name=snowflake_table, con=snowflake_conn, schema=snowflake_schema, if_exists='append', index=False)

# close Snowflake connection
snowflake_conn.close()

"""
    This script imports a chosen file from the 'clean' directory in our s3 bucket, adds relevent new fields for our production uses,then uploads the file as a csv to '/feateng' directory.
    Refer to the EDA portion of this project to see what exactly im doing to each file. 
"""



filename = str(sys.argv[1])


def main():
    








    return 

if __name__ == "__main__":
    main()






