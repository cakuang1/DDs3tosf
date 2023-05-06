
import boto3
import pandas as pd
import snowflake.connector
import os
from dotenv import load_dotenv




snowflake_user = os.environ.get('snowflake_user')
snowflake_password = os.environ.get('snowflake_password')
snowflake_account = os.environ.get('snowflake_account')
snowflake_database = os.environ.get('ddtosfpipeline')
snowflake_schema = os.environ.get('snowflake_schema')
snowflake_table = os.environ.get('MY_VARIABLE')



# connect to Snowflake and create new table








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
    
    snowflake_conn = snowflake.connector.connect(
        user=snowflake_user,
        password=snowflake_password,
        account=snowflake_account,
        database=snowflake_database,
        schema=snowflake_schema
    )












    return 

if __name__ == "__main__":
    main()






