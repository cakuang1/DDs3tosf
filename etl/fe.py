import sys
import os
sys.path.append(os.path.abspath('../utils'))
from utils import io


"""
    This script imports a chosen file from the 'clean' directory in our s3 bucket, adds relevent new fields for our production uses,then uploads the file as a csv to '/feateng' directory.
    Refer to the EDA portion of this project to see what exactly im doing to each file. 
"""








def main():    
    impdirectory = 'clean'
    outdirectory  = 'feateng'

    ##Import csv file from the raw directory 
    df = io.imp_file(impdirectory,filename)





    # Write "feature engineered" df to s3
    io.save_file(outdirectory, filename)


    print("Your data has been cleansed and uploaded with the filename : " )
    return    



if __name__ == "__main__":
    main()





