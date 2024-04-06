from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = 'stage_01_data_ingestion'

try:
    logger.info(">>>> stage {STAGE_NAME} started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(">>>> stage {STAGE_NAME} completed")
except Exception as e:
    logger.error(f">>>> stage {STAGE_NAME} failed with error: {e}")
    raise e
    
