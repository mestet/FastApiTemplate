from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
import logging

# Setup logging (optional for debugging)
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unexpected error: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"message": "Internal server error. Please try again later."},
    )


async def value_error_handler(request: Request, exc: ValueError):
    logger.error(f"ValueError: {exc}")
    return JSONResponse(
        status_code=400,
        content={"message": str(exc)},
    )
