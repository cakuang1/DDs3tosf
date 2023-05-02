from utils.helpers import timetostring
from io import imp_file,save_file
import config



def main():
    rangeofdays = range(1,32)
    bucketname = config.BUCKET_NAME 
    impdirectory = 'raw'
    outdirectory  = 'cleaned'
    str = timetostring()
    for i in rangeofdays:
        filename = str(i)

        ##Import csv file from the raw directory 
        df = imp_file(bucketname,impdirectory,filename)
               
        ##Transform
        
        








        # Write "clean" df to s3
        save_file(bucketname,outdirectory, filename + ' ' +  str)

    

    print("Your data has been cleansed.")
    return    





if __name__ == "__main__":
    main()






