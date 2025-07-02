from sqlalchemy import Column, String, DECIMAL, func, DateTime
from sqlalchemy.orm import relationship
from src.database.postgres import Base


class OrderHeaderModel(Base):
    __tablename__: str = 'order_header'

    order_id = Column(String(10), primary_key=True, autoincrement=True)
    order_date = Column(DateTime, default=func.current_timestamp())
    total_amount = Column(DECIMAL(10, 2))

    items = relationship('OrderItemModel', back_populates='header', passive_deletes=True)
