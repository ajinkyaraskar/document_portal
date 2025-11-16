import sys
import traceback
from logger.custom_logger import CustomLogger
logger = CustomLogger().get_logger(__file__)


class DocumentPortalException(Exception):
    """Custom Exception for Document Portal"""
    def __init__(self,error_message:Exception,error_details:sys):
        print(error_details.exc_info())
        _,_,exc_tb=error_details.exc_info()
        self.line_number=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename
        self.error_message= str(error_message)
        self.traceback_str = ''.join(traceback.format_exception(*error_details.exc_info()))

    def __str__(self):
        return f"""
        Error occurred in script: [{self.file_name}] at line number: [{self.line_number}]
        Message: {self.error_message}
        Traceback: 
        {self.traceback_str}
        """

if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        app_exc = DocumentPortalException(e,sys)
        logger.error(app_exc)
        raise app_exc from e