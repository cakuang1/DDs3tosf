import datetime


def timetostring(): 
    """    
    Returns a string of the current data and time


    Arguments : 
        None

    Returns : 
        str: String of the current data and time
    """

    return datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")

def removecolumns(df,columns):
   """
    
   Removes irrelavent columns for our production table


    Arguments : 
        df (pd.DataFrame): The dataframe you want to drop columns from 
        columns (list[str]) :  The list of columns you want to drop 

    Returns : 
        pd.DataFrame 
   """
   newdf = df.drop(columns)
   return newdf


def 












