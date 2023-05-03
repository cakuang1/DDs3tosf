import datetime
import pandas as pd
import numpy as np



def timetostring(): 
    """    
    Returns a string of the current data and time


    Arguments : 
        None

    Returns : 
        str: String of the current data and time
    """

    return datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")


def addminutefield(df):
   """
    
    Converts the 'Total_time_elapsed' field to the total number of minutes 

    Arguments : 
        df (pd.DataFrame): The dataframe

    Returns : 
        pd.DataFrame 
   """
    
   df['Total Minutes'] = df['Total_time_elapsed'].apply(get_total_minutes)
   newdf = df.drop(columns=['Total_time_elapsed'])
   return newdf


def onehotencode(df):
   """
    
    One-hot-encodes categorical columns

    Arguments : 
        df (pd.DataFrame): The dataframe you want to drop columns from 

    Returns : 
        pd.DataFrame 
   """
   newdf = pd.get_dummies(df, columns=['Is_New','Delivery_Region','Is_ASAP'])
   return newdf

def addresponse(df):
   """
   
    Adds the response variable we are trying to predict
  
   
   """
   

   df['Tip?'] = np.where(df['Amount_of_tip'] == 0, 0, 1)
   return df




def get_total_minutes(time_str):
    # Split the string to get the hours, minutes, and seconds components
    time_parts = time_str.split(' ')[-1].split(':')
    hours = int(time_parts[0])
    minutes = int(time_parts[1])
    seconds = int(time_parts[2].split('.')[0])
    microseconds = int(time_parts[2].split('.')[1])
    
    # Create a timedelta object representing the time difference
    time_diff = datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds, microseconds=microseconds)
    
    # Calculate the total number of minutes
    total_minutes = time_diff.total_seconds() // 60
    
    return total_minutes



