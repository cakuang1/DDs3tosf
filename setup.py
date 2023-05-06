## This is a setup file is meant to parse the original data into seperate dates and store them into the chosen bucket. This is so we can simulate batch work.

import pandas as pd
import boto3
import os
from dotenv import load_dotenv
from utils.io import save_file
import snowflake.connector


AWS_REGION = os.environ.get('AWS_REGION')
BUCKET_NAME = os.environ.get('BUCKET_NAMEr')
snowflake_user = os.environ.get('snowflake_user')
snowflake_password = os.environ.get('snowflake_password')
snowflake_account = os.environ.get('snowflake_account')
snowflake_database = os.environ.get('ddtosfpipeline')
snowflake_schema = os.environ.get('snowflake_schema')
snowflake_table = os.environ.get('snowflake_table')

columns = [ 
        'Order_total FLOAT',
        'Amount_of_discount FLOAT', 
        'Refunded_amount FLOAT', 
        'Day INT',
        'Total Minutes FLOAT', 
        'Is_New_False BOOLEAN', 
        'Is_New_True BOOLEAN',
        'Delivery_Region_Mountain View BOOLEAN', 
        'Delivery_Region_None BOOLEAN',
        'Delivery_Region_Palo Alto BOOLEAN',
        'Delivery_Region_San Jose BOOLEAN',
        'Is_ASAP_False BOOLEAN',
        'Is_ASAP_True BOOLEAN', 
        'Tip BOOLEAN?']





def bucketexists(client):
    # Initialize S3 client
    s3 = client

    # Define the name of the bucket you want to check
    bucket_name = 'my-bucket'

    # Check if the bucket exists
    bucket_exists = True
    try:
        s3.head_bucket(Bucket= BUCKET_NAME)
    except:
        bucket_exists = False

    # If the bucket exists, empty and delete it
    if bucket_exists:
        print(f"{BUCKET_NAME} already exists")
        # List all objects in the bucket
        objects = s3.list_objects(Bucket= BUCKET_NAME)['Contents']

        # Create a list of object keys
        keys = [{'Key': obj['Key']} for obj in objects]

        # Delete all objects in the bucket
        s3.delete_objects(Bucket=bucket_name, Delete={'Objects': keys})

        # Delete the bucket
        s3.delete_bucket(Bucket=bucket_name)

        print(f"{bucket_name} deleted successfully!")
    else:
        print(f"{bucket_name} does not exist.")




def main():
    """
    Script that creates and populates raw S3 bucket. This assigns each row arbitrarily a day from 1-31, representing a day in 

    """
    # S3 Setup
    client = boto3.client("s3", region_name=AWS_REGION)

    ## Checks if bucket already exists. If it does, delete it. Then create a new Bucket.
    bucketexists(client=client)
    response = client.create_bucket(Bucket=BUCKET_NAME, CreateBucketConfiguration=location)
    ## Populates the newly created s3 bucket
    url = 'https://raw.githubusercontent.com/ralfsantacruz/Doordash-Analytics/master/resources/analytics.csv'
    df = pd.read_csv(url)
    df["Day"] = df['Customer_placed_order_datetime'].str[:2].astype(int)
    location = {'LocationConstraint': AWS_REGION}

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
                schema= snowflake_schema
                )

    snowflake_cursor = snowflake_conn.cursor()

    #Deletes if exists
    cur.execute(f"DROP DATABASE IF EXISTS {snowflake_database}")
    #Creates the database
    snowflake_cursor.execute(f"CREATE DATABASE {snowflake_database}")

    print('Your database ' + snowflake_database + ' has been created')


    #Creates the schema
    snowflake_cursor.execute("CREATE SCHEMA " + schemaname)

    print ('Your schema ' + schemaname + ' has been created')




    snowflake_conn.close()

    print('Your setup is complete. T')


    return

if __name__ == "__main__":
    main()


