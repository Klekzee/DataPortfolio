import sys
import json
import time
import schedule
import pandas as pd
from os import environ, remove
from pathlib import Path
from ftplib import FTP_TLS

# Connects to an FTP server and returns FTP_TLS object
def get_ftp() -> FTP_TLS:
    # Get FTP details
    FTPHOST = environ["FTPHOST"]
    FTPUSER = environ["FTPUSER"]
    FTPPASS = environ["FTPPASS"]

    # Return authenticated FTP
    ftp = FTP_TLS(FTPHOST, FTPUSER, FTPPASS)
    ftp.prot_p()
    return ftp

# Function to upload csv files to the FTP server
def upload_to_ftp(ftp: FTP_TLS, file_source: Path):
    with open(file_source, "rb") as fp:
        ftp.storbinary(f"STOR {file_source.name}", fp)

# Function to delete files from local system
def delete_file(file_source: str | Path):
    remove(file_source)

# Function to read csv files from the URL
def read_csv(config: dict) -> pd.DataFrame:
    url = config["URL"]
    params = config["PARAMS"]
    return pd.read_csv(url, **params)

def pipeline():
    # Load source configuration from config.json file
    with open("config.json", "rb") as fp:
        config = json.load(fp)

    # Get FTP_TLS object
    ftp = get_ftp()

    # Itterating each source in the config.json file
    for source_name, source_config in config.items():
        file_name = Path(source_name + ".csv")
        df = read_csv(source_config)
        
        # Download to local
        df.to_csv(file_name, index=False)
        print(f'Downloaded {file_name} successfully!')

        # Upload to FTP server
        upload_to_ftp(ftp, file_name)
        print(f'Uploaded {file_name} successfully!')

        # Delete the local file
        delete_file(file_name)
        print(f'Deleted {file_name} successfully!')

if __name__=="__main__":
    
    schedule.every().day.at('00:00').do(pipeline)

    while True:
        schedule.run_pending()
        time.sleep(1)
