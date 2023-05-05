
import boto3
import pandas as pd
import snowflake.connector
import os
from dotenv import load_dotenv

snowflake_user = 'cakuang1'
snowflake_password = 'Powerbest123'
snowflake_account = 'vezyeir-og88155'
aws_access_key_id ='AKIAVDWFA4HQJT3W647C'
aws_secret_access_key ='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'


snowflake_database = 'ddtosfpipeline' # Dont need to change
snowflake_schema = 'ddtosfpipelineschema' # Dont need to change
AWS_REGION = "us-west-1" # Dont need to change
BUCKET_NAME = 'ddsfpipeline' # Dont need to change





# set up AWS and Snowflake credentials

snowflake_user = os.environ.get('snowflake_user')
snowflake_password = os.environ.get('snowflake_password')
snowflake_account = os.environ.get('snowflake_account')
snowflake_database = os.environ.get('ddtosfpipeline')
snowflake_schema = os.environ.get('snowflake_schema')

snowflake_table = os.environ.get('MY_VARIABLE')

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






