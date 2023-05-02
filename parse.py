## This is a setup file is meant to parse the original data into seperate dates and store them into the chosen bucket. This is so we can simulate batch work.

import pandas as pd
import boto3
import config
from utils.io import save_file

AWS_REGION = "us-west-1"
BUCKET_NAME = config.BUCKET_NAME



def main():
    """
    Script that populates raw S3 bucket. This assigns each row arbitrarily a day from 1-31, representing a day in 

    """
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
    print("Your setup is complete. You should see a newly created bucket with parsed csv files in the raw directory")

    return

if __name__ == "__main__":
    main()


