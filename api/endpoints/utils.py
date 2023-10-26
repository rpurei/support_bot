from config import DEBUG_MODE
from app_logger import logger_output
from fastapi import HTTPException


def http_exception(error_message: str, error_level: int, error_code: int):
    lf = '\n'
    logger_output(error_message, DEBUG_MODE, error_level)
    error_message = error_message.replace(lf, ' ')
    raise HTTPException(status_code=error_code,
                        detail=error_message)
