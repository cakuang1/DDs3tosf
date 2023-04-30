## This is a setup file is meant to parse the original data into seperate dates and store them into the chosen bucket. This is so we can simulate batch work.



import pandas as pd

import random
import boto
def main():
    """
    Script that populates raw S3 bucket. This assigns each row arbitrarily a day from 1-31, representing a day in 

    """
    values_range = [1, 31]
    url = 'https://raw.githubusercontent.com/ralfsantacruz/Doordash-Analytics/master/resources/analytics.csv'

    df = pd.read_csv(url)
    
    random.sample(range(30), 4)

    



    return





if __name__ == "__main__":
    main()


