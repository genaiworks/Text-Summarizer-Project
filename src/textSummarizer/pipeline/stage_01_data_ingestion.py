
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_ingestion import DataIngestion
from textSummarizer.logging import logger

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config_manager = ConfigurationManager()
        data_ingestion = DataIngestion(config_manager.get_dataingestion_config())
        data_ingestion.download_data()
        data_ingestion.unzip_data()