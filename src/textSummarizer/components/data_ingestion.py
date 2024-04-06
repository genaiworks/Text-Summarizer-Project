import os
import urllib.request as request
import zipfile
from textSummarizer.entity import DataIngestionConfig
from textSummarizer.logging import logger


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config
    
    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file)
            logger.info(f" {filename} downloaded with following headers: {headers}")
        else:
            logger.info("Folder already exists Skipping download with size ")
    
    def unzip_data(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)
        logger.info("unzip done")