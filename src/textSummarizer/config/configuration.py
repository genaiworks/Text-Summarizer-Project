from textSummarizer.constants import *
from textSummarizer.entity import (DataIngestionConfig, DataTransformationConfig, DataValidationConfig)
from textSummarizer.utils.common import read_yaml, create_directories


class ConfigurationManager:
    def __init__(
        self, config_file_path=CONFIG_FILE_PATH, param_file_path=PARAM_FILE_PATH
    ):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(param_file_path)
        create_directories([self.config.artifacts_root])

    def get_dataingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        return DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir,
        )

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES,
        )
        return data_validation_config
    
    def get_data_transformation_config(self)->DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([config.root_dir])
        
        data_transformation_config = DataTransformationConfig(
            root_dir = config.root_dir,
            data_path = config.data_path,
            tokenizer_name =config.tokenizer_name
        )
        return data_transformation_config
