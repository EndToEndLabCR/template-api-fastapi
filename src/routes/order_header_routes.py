from typing import List

from fastapi import APIRouter, HTTPException, Depends, status

from src.database.postgres import get_db
from src.models import OrderHeaderModel
from src.schemas.order_header_schema import OrderHeaderResponse, OrderHeaderUpdate, OrderHeaderCreate
from sqlalchemy.orm import Session
from src.services.order_header_service import get_all_order_headers, get_order_header_by_id, create_order_header, \
    patch_order_header, delete_order_header

router = APIRouter()


@router.get("/all", response_model=List[OrderHeaderResponse])
async def fetch_all_order_headers(db_session: Session = Depends(get_db)):
    orders_headers = get_all_order_headers(db_session)

    if not orders_headers:
        raise HTTPException(status_code=404, detail="No orders headers found...")

    return orders_headers


@router.get("/{order_header_id}", response_model=OrderHeaderResponse)
async def fetch_order_by_id(order_header_id: str, db_session: Session = Depends(get_db)):
    order_header = get_order_header_by_id(order_header_id, db_session)

    if not order_header:
        raise HTTPException(status_code=404, detail=f"No order header with id {order_header_id} found.")

    return order_header


@router.post("/", response_model=OrderHeaderResponse, status_code=status.HTTP_201_CREATED)
async def add_order_header(order_header_create: OrderHeaderCreate, db_session: Session = Depends(get_db)):
    try:
        order_header_created = create_order_header(order_header_create, db_session)
        return order_header_created

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating order header: {str(e)}.")


@router.patch("/{order_header_id}", response_model=OrderHeaderResponse)
async def update_order_header(order_header_id: str, order_header_update: OrderHeaderUpdate,
                              db_session: Session = Depends(get_db)):
    order_header_updated = patch_order_header(order_header_id, order_header_update, db_session)

    if not order_header_updated:
        raise HTTPException(status_code=404, detail=f"No order header with id {order_header_id} found.")

    return order_header_updated


@router.delete("/{order_header_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_order_header(order_header_id: str, db_session: Session = Depends(get_db)):
    order_header_deleted = delete_order_header(order_header_id, db_session)

    if not order_header_deleted:
        raise HTTPException(status_code=404, detail=f"No order header with id {order_header_id} found.")
