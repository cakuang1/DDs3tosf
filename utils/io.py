import boto3
import os
import pandas as pd
import pickle
import s3fs
import typing



## Helpeer file for everything IO related (S3 data retrieval,snowflake import)

BUCKET = "dd-tran-data"

def initial_setup():
    """
    Parses the csv file by month and day and stores into the bucket 'dd-tran-data'

    Arguments : 
        None  

    Returns : 
        None 
    
    """

    url = 'https://raw.githubusercontent.com/ralfsantacruz/Doordash-Analytics/master/resources/analytics.csv'
    df = pd.read_csv(url)


    df["Day"] = df['Customer_placed_order_datetime'].str[:2]
    s3 = boto3.resource('s3')
    
    

    



    
    

    
















def imp_file(day,directory):
    """        
    Arguments : 
        month (str): month of t  

    Returns : 
        pd.Dataframe: Dataframe from the 
    """

    
    s3_client = boto3.client('s3')
    df.to_csv('s3://experimental/playground/temp_csv/dummy.csv', index=False)





    return pd.read_csv(file)




def save_output():



