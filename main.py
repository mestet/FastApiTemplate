import logging

from fastapi import FastAPI
from fastapi.routing import APIRouter
from controllers import report_controller, user_controller
from exception_handlers import global_exception_handler, value_error_handler


app = FastAPI()

# Setup logging (optional but recommended for debugging)
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

# Create a versioned router for `/api/v1`
api_v1_router = APIRouter(prefix="/api/v1")

# Include all v1 routers in `/api/v1`
api_v1_router.include_router(report_controller.router)
api_v1_router.include_router(user_controller.router)

# Include routers in base app
app.include_router(api_v1_router)

# Register exception handlers
app.add_exception_handler(Exception, global_exception_handler)
app.add_exception_handler(ValueError, value_error_handler)
