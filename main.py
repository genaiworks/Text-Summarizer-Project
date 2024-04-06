from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline

STAGE_NAME = 'stage_01_data_ingestion'

try:
    logger.info(">>>> stage {STAGE_NAME} started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(">>>> stage {STAGE_NAME} completed")
except Exception as e:
    logger.error(f">>>> stage {STAGE_NAME} failed with error: {e}")
    raise e
    

STAGE_NAME = 'stage_02_data_validation'

try:
    logger.info(">>>> stage {STAGE_NAME} started")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(">>>> stage {STAGE_NAME} completed")
except Exception as e:
    logger.error(f">>>> stage {STAGE_NAME} failed with error: {e}")
    raise e

STAGE_NAME = 'stage_03_data_transformation'

try:
    logger.info(">>>> stage {STAGE_NAME} started")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(">>>> stage {STAGE_NAME} completed")
except Exception as e:
    logger.error(f">>>> stage {STAGE_NAME} failed with error: {e}")
    raise e
