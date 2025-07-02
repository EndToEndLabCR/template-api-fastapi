from typing import List
from fastapi import APIRouter, HTTPException, Depends, status

from src.database.postgres import get_db
from src.models import OrderItemModel
from src.schemas.order_item_schema import OrderItemResponse, OrderItemUpdate, OrderItemCreate
from sqlalchemy.orm import Session
from src.services.order_item_service import get_order_item_by_id, create_order_item, \
    patch_order_item, delete_order_item

router = APIRouter()


@router.get("/{order_id}", response_model=List[OrderItemResponse])
async def fetch_order_items_by_order_id(order_id: str, db_session: Session = Depends(get_db)):
    order_items = get_order_item_by_id(order_id, db_session)

    if not order_items:
        raise HTTPException(status_code=404, detail=f"No order items with order id {order_id} found.")

    return order_items


@router.post("/", response_model=OrderItemResponse, status_code=status.HTTP_201_CREATED)
async def add_order_item(order_item_create: OrderItemCreate, db_session: Session = Depends(get_db)):
    try:
        order_item_created = create_order_item(order_item_create, db_session)
        return order_item_created

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating order item: {str(e)}.")


@router.patch("/{order_id}/{order_item}", response_model=OrderItemResponse)
async def update_order_item(order_id: str, order_item: str, order_item_update: OrderItemUpdate,
                            db_session: Session = Depends(get_db)):
    order_item_updated = patch_order_item(order_id, order_item, order_item_update, db_session)

    if not order_item_updated:
        raise HTTPException(status_code=404, detail=f"No order item: {order_item} for order id: {order_id} found.")

    return order_item_updated


@router.delete("/{order_id}/{order_item}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_order_item(order_id: str, order_item: str, db_session: Session = Depends(get_db)):
    order_item_deleted = delete_order_item(order_id, order_item, db_session)

    if not order_item_deleted:
        raise HTTPException(status_code=404, detail=f"No order item {order_item} for order id: {order_id} found.")
