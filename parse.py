## This is a setup file is meant to parse the original data into seperate dates and store them into the chosen bucket. This is so we can simulate batch work.

import pandas as pd
import boto3
import config
from utils.io import save_file
import snowflake.connector


AWS_REGION = "us-west-1"
BUCKET_NAME = config.BUCKET_NAME
snowflake_user = config.snowflake_user
snowflake_password = config.snowflake_password
snowflake_account = config.snowflake_account
snowflake_database = config.snowflake_database



def main():
    """
    Script that populates raw S3 bucket. This assigns each row arbitrarily a day from 1-31, representing a day in 

    """


    
    ### S3 Setup
    client = boto3.client("s3", region_name=AWS_REGION)

    url = 'https://raw.githubusercontent.com/ralfsantacruz/Doordash-Analytics/master/resources/analytics.csv'
    df = pd.read_csv(url)
    df["Day"] = df['Customer_placed_order_datetime'].str[:2].astype(int)
    location = {'LocationConstraint': AWS_REGION}
    response = client.create_bucket(Bucket=BUCKET_NAME, CreateBucketConfiguration=location)

    print("Amazon S3 bucket has been created")
    for i in range(1,32):
        holder = df[df['Day'] == i]
        save_file('raw',str(i),holder)
    print( 'Your bucket ' + BUCKET_NAME + 'created with a raw directory containing files')

    ### SnowFlake SetUp


    snowflake_conn = snowflake.connector.connect(
                user=snowflake_user,
                password=snowflake_password,
                account=snowflake_account,
                database = snowflake_database,
                schema= 
                )
    schemaname = 'projectschema'
            
    snowflake_cursor = snowflake_conn.cursor()


        #Creates the database
    snowflake_cursor.execute(f"CREATE DATABASE {snowflake_database}")

    print('Your database ' + snowflake_database + ' has been created')


        #Creates the schema
    snowflake_cursor.execute("CREATE SCHEMA " + schemaname)

    print ('Your schema ' + schemaname + ' has been created')

    snowflake_cursor.execute("CREATE SCHEMA " + schemaname)


    snowflake_conn.close()

    print('Your setup is complete. T')


    return

if __name__ == "__main__":
    main()


