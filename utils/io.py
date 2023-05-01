import boto3
import pandas as pd
import s3fs
import typing



## Helpeer file for everything IO related (S3 data retrieval,snowflake import)

BUCKET = "dd-tran-data"


def imp_file(bucketname,directory,filename):
    """    
    Imports CSV file from S3 into a pandas dataframe


    Arguments : 
        bucketname (str) : The bucket name
        filename (str): The filename
        directory(str): There directory where the file is located   

    Returns : 
        pd.Dataframe: Dataframe from the 
    """
    path = 's3://' + bucketname +  '/' + directory + '/' + filename + '.csv'

    df = pd.read_csv(path)

    return df




def save_file(bucketname,directory,filename,df):
    """        
    Saves pandas data frame into


    Arguments : 
        bucketname (str) : The bucket name
        directory(str): There directory where the file is located   
        filename (str): The filename

    Returns : 
        None
    """

    path = 's3://' + bucketname +  '/' + directory + '/' + filename + '.csv'
    df.to_csv(path)
    return None





