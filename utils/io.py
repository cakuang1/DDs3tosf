import boto3
import os
import pandas as pd
import pickle
import s3fs
import typing


## Helpeer file for everything IO related (S3 data retrieval,snowflake import)

BUCKET = ""


def imp_file(month,day,year):
    """        
    Arguments : 
        month (str): month of t  

    Returns : 
        pd.Dataframe: Dataframe from the 
    """

    





    return pd.read_csv(file)


