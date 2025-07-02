from sqlalchemy import Column, DECIMAL, DateTime, func, ForeignKey, String
from sqlalchemy.orm import relationship

from src.database.postgres import Base


class OrderItemModel(Base):
    __tablename__: str = 'order_item'

    order_id = Column(String(10), ForeignKey('order_header.order_id', ondelete='CASCADE'), primary_key=True)
    order_item = Column(String(4), primary_key=True)
    unit_price = Column(DECIMAL(10, 2))
    order_item_date = Column(DateTime, default=func.current_timestamp())

    header = relationship('OrderHeaderModel', back_populates='items')
