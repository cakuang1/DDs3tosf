"""
    
    This script imports a chosen file from the 'raw' directory in our s3 bucket, cleans it, then uploads the file as a csv to '/clean' directory.
    Refer to the EDA portion of this project to see what exactly im doing to each file. 
    

"""



import sys
import os
sys.path.append(os.path.abspath('../utils'))
from utils import io







filename = str(sys.argv[1])


def main():
    impdirectory = 'raw'
    outdirectory  = 'clean'
    str = timetostring()
    #Import csv file from the raw directory 
    df = io.imp_file(impdirectory,filename)
        
    #Cleaning

    df = df.drop(columns=['Customer_placed_order_datetime','Placed_order_with_restaurant_datetime','Unnamed: 0.1','Unnamed: 0','Driver_ID',
                     'Restaurant_ID','Consumer_ID','Driver_at_restaurant_datetime','Delivered_to_consumer_datetime'])

    # Write "clean" df to s3
    
    io.save_file(outdirectory, filename,df)

    print("Your data has been cleansed and uploaded in the /clean directory with the filename : " + filename )
    return    



if __name__ == "__main__":
    main()






