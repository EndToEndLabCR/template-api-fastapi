import backoff
from sqlalchemy import and_

from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import Session
from fastapi import HTTPException

from src.models import OrderHeaderModel
from src.models.order_item import OrderItemModel
from src.schemas.order_item_schema import OrderItemResponse, OrderItemCreate, OrderItemUpdate
from src.utils.backoff_helper import backoff_handler
from src.utils.logUtil import log


def get_order_item_by_id(order_id: str, db_session: Session) -> list[OrderItemResponse]:
    log.info(f"Searching items for order id: {order_id} .")

    try:
        order_items = (
            db_session.query(OrderItemModel)
            .filter(OrderItemModel.order_id == order_id)
            .all()
        )

        if not order_items:
            log.info(f"Order items with order id: {order_id} not found.")
            return []

        return [OrderItemResponse.from_orm(order_item) for order_item in order_items]

    except Exception as e:
        db_session.rollback()
        log.error(f"Error getting order items with order id: {order_id}. Exception {e}.", exc_info=True)
        raise e


def create_order_item(order_item_create: OrderItemCreate, db_session: Session) -> OrderItemResponse:
    log.info(f"Creating a new order item.")

    try:
        new_order_item = OrderItemModel(
            order_id=order_item_create.order_id,
            order_item=order_item_create.order_item,
            unit_price=order_item_create.unit_price
        )
        db_session.add(new_order_item)
        db_session.commit()
        db_session.refresh(new_order_item)

        return OrderItemResponse.from_orm(new_order_item)

    except OperationalError as e:
        db_session.rollback()
        log.error(f"Error creating order item. Exception: {e}.", exc_info=True)
        raise HTTPException(status_code=500, detail="Database Error")

    except Exception as e:
        db_session.rollback()
        log.error(f"Error creating order item. Exception: {e}.", exc_info=True)
        raise e


def patch_order_item(order_id: str, order_item: str, order_item_update: OrderItemUpdate,
                     db_session: Session) -> OrderItemResponse:
    log.info(f"Updating order item: {order_item} for order id: {order_id}")

    try:
        order_item = (
            db_session.query(OrderItemModel)
            .filter(and_(OrderItemModel.order_id == order_id,
                         OrderItemModel.order_item == order_item))
            .first()
        )

        if not order_item:
            log.info(f"Order item: {order_item} for order id: {order_id} not found.")
            return None

        for key, value in order_item_update.dict(exclude_unset=True).items():
            setattr(order_item, key, value)

        db_session.commit()

        return OrderItemResponse.from_orm(order_item)

    except Exception as e:
        db_session.rollback()
        log.error(f"Error updating order item {order_item} for order id: {order_id}. Exception: {e}.", exc_info=True)
        raise e


def delete_order_item(order_id: str, order_item: str, db_session: Session) -> bool:
    log.info(f"Deleting order item {order_item} for order id: {order_id}.")

    try:
        order_item_deleted = (
            db_session.query(OrderItemModel)
            .filter(and_(OrderItemModel.order_id == order_id,
                         OrderItemModel.order_item == order_item))
            .first()
        )

        if not order_item_deleted:
            log.info(f"Order item: {order_item} for order id: {order_id} not found.")
            return False

        db_session.delete(order_item_deleted)
        db_session.commit()

        return True

    except Exception as e:
        db_session.rollback()
        log.error(f"Error deleting order item: {order_item} for order id: {order_id}. Exception: {e}.", exc_info=True)
