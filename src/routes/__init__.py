from fastapi import APIRouter

from .order_header_routes import router as order_header_router
from .order_item_routes import router as order_item_router

router = APIRouter()

router.include_router(order_header_routes.router, prefix="/order_header", tags=["order_header"])
router.include_router(order_item_routes.router, prefix="/order_item", tags=["order_item"])

