import sys
import os
sys.path.append(os.path.abspath('../utils'))
from utils import io,helpers


"""
    This script imports a chosen file from the 'clean' directory in our s3 bucket, adds relevent new fields for our production uses,then uploads the file as a csv to '/feateng' directory.
    Refer to the EDA portion of this project to see what exactly im doing to each file. 
"""








def main():    
    impdirectory = 'clean'
    outdirectory  = 'feateng'

    ##Import csv file from the raw directory 
    df = io.imp_file(impdirectory,filename)


    ##Feature Engineering
    v1 = helpers.addminutefield(df)
    v2 = helpers.get_total_minutes(v1)
    v3= helpers.addresponse(v2)

    # Write "feature engineered" df to s3
    io.save_file(outdirectory, filename,v3)
    
    print("Your data has now has new fields! : " )
    return  



if __name__ == "__main__":
    main()





