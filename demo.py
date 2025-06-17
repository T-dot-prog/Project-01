# from src.logger import logger
# from src.exception import MyException
# import sys

# logger.info("this is an info message")
# logger.warning("this is an warning message")

# try:
#     result = 10 / 0 
# except Exception as e:
#     logger.error("there is a error encountering")
#     raise MyException(error_message= e, error_detail= sys) from e 


# all test passed successfully -----------------------------


from src.pipline.training_pipeline import TrainPipeline

pipeline = TrainPipeline()

pipeline.run_pipeline()