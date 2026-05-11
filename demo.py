# below is the code to check the logging config
# from src.logger import logging

# logging.debug("This is a debug message")
# logging.info("This is a info message")
# logging.critical("This is a critical message")
# logging.warning("This is a warning message")
# logging.error("This is a error message")

# -------------------------------------------------

# below is the code to check the exception config 
# from src.logger import logging
# from src.exception import CustomException
# import sys 

# try :
#     a = 1 + "Z"
# except Exception as e :
#     logging.info(e)
#     raise CustomException(e, sys)