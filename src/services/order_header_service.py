from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import Session
from fastapi import HTTPException

from src.models.order_header import OrderHeaderModel
from src.schemas.order_header_schema import OrderHeaderResponse, OrderHeaderCreate, OrderHeaderUpdate
from src.utils.backoff_helper import backoff_handler
from src.utils.logUtil import log


def get_all_order_headers(db_session: Session) -> list[OrderHeaderResponse]:
    log.info("Getting all order headers.")

    try:
        order_headers = (
            db_session.query(OrderHeaderModel)
            .all()
        )
        if not order_headers:
            log.info(f"No order headers found.")
            return None

        return [OrderHeaderResponse.from_orm(order_header) for order_header in order_headers]

    except Exception as e:
        db_session.rollback()
        log.error(f"Error getting order headers. Exception: {e}.", exc_info=True)
        raise e


def get_order_header_by_id(order_header_id: str, db_session: Session) -> OrderHeaderResponse:
    log.info(f"Searching order header with id: {order_header_id}.")

    try:
        order_header = db_session.query(OrderHeaderModel).filter(OrderHeaderModel.order_id == order_header_id).first()

        if not order_header:
            log.info(f"Order header with id: {order_header_id} not found.")
            return None

        return OrderHeaderResponse.from_orm(order_header)

    except Exception as e:
        db_session.rollback()
        log.error(f"Error getting order header with id: {order_header_id}. Exception {e}.", exc_info=True)
        raise e


def create_order_header(order_header_create: OrderHeaderCreate, db_session: Session) -> OrderHeaderResponse:
    log.info(f"Creating a new order header.")

    try:
        new_order_header = OrderHeaderModel(
            order_id=order_header_create.order_id,
            total_amount=order_header_create.total_amount
        )
        db_session.add(new_order_header)
        db_session.commit()
        db_session.refresh(new_order_header)

        return OrderHeaderResponse.from_orm(new_order_header)

    except OperationalError as e:
        db_session.rollback()
        log.error(f"Error creating order header. Exception: {e}.", exc_info=True)
        raise HTTPException(status_code=500, detail="Database Error")

    except Exception as e:
        db_session.rollback()
        log.error(f"Error creating order header. Exception: {e}.", exc_info=True)
        raise e


def patch_order_header(order_header_id: str, order_header_update: OrderHeaderUpdate,
                       db_session: Session) -> OrderHeaderResponse:
    log.info(f"Updating order header id: {order_header_id}")

    try:
        order_header = db_session.query(OrderHeaderModel).filter(OrderHeaderModel.order_id == order_header_id).first()

        if not order_header:
            log.info(f"Order header with id: {order_header_id} not found.")
            return None

        for key, value in order_header_update.dict(exclude_unset=True).items():
            setattr(order_header, key, value)

        db_session.commit()
        return OrderHeaderResponse.from_orm(order_header)

    except Exception as e:
        db_session.rollback()
        log.error(f"Error updating order header {order_header_id}. Exception: {e}.", exc_info=True)
        raise e


def delete_order_header(order_header_id: str, db_session: Session) -> bool:
    log.info(f"Deleting order header with id: {order_header_id}.")

    try:
        order_header = db_session.query(OrderHeaderModel).filter(OrderHeaderModel.order_id == order_header_id).first()

        if not order_header:
            log.info(f"Order header with id: {order_header_id} not found.")

            return False

        db_session.delete(order_header)
        db_session.commit()

        return True

    except Exception as e:
        db_session.rollback()
        log.error(f"Error deleting order header with id: {order_header_id}. Exception: {e}.", exc_info=True)
