import sys
import logging 

def error_message_details(error: Exception, error_detail: sys) -> str :
    """
    This function helps to extract the detailed error information including file name, line number and the error line message.

    :param error: The exception that has occurred.
    :param error_detail: The sys module to access that traceback details.
    :return: A formatted error message string.
    """

    # Extract the traceback details
    _, _, exc_tb = sys.exc_info()

    # Get the file name where the error occurred 
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Creating a customer error message string with file name, line number and error message.
    line_no = exc_tb.tb_lineno
    error_message = f"Error occurred in python script : [{file_name}] at line no [{line_no}] : str({error})"

    # Log the error for better tracking 
    logging.error(error_message)

    return error_message


class CustomException(Exception): 
    """
    Custom Exception for handling error in the loan application.
    """

    def __init__(self, error_message: str, error_detail: sys):
        """
        Initializes the CustomException with a detailed error message.

        : param error_message: A string describing the error.
        : param error_detail: The sys module to access the traceback details.
        """

        # Call the base class constructor with the error message.
        super().__init__(error_message)

        # Format the detailed error message using error_message_detail function.
        self.error_message = error_message_details(error_message, error_detail)

    
    def __str__(self):
        """
        Returns the str representation of the error message.
        """

        return self.error_message 