from textSummarizer.constants import *
from textSummarizer.entity import (DataIngestionConfig)
from textSummarizer.utils.common import read_yaml,create_directories

class ConfigurationManager:
    def __init__(
        self,
        config_file_path= CONFIG_FILE_PATH,
        param_file_path = PARAM_FILE_PATH):
        
        self.config_file_path = read_yaml(config_file_path)
        self.param_file_path = read_yaml(param_file_path)
        create_directories([self.config_file_path.artifacts_root])

       
    def get_dataingestion_config(self) -> DataIngestionConfig:
        config =self.config_file_path.data_ingestion
        create_directories([config.root_dir])
        return DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )