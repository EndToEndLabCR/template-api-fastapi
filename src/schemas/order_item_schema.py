from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field, model_validator
from datetime import datetime
from src.models.order_item import OrderItemModel


class OrderItemResponse(BaseModel):
    order_id: str = Field(..., alias="orderId")
    order_item: str = Field(..., alias="orderItem")
    unit_price: Decimal = Field(..., alias="unitPrice")
    order_item_date: datetime = Field(..., alias="orderItemDate")

    @model_validator(mode="before")
    def validate_dates(cls, obj):
        if isinstance(obj, OrderItemModel):
            return {
                "order_id": obj.order_id,
                "order_item": obj.order_item,
                "unit_price": obj.unit_price,
                "order_item_date": obj.order_item_date.isoformat() if obj.order_item_date else None,
            }

        return obj

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True


class OrderItemCreate(BaseModel):
    order_id: str = Field(..., alias="orderId")
    order_item: str = Field(..., alias="orderItem")
    unit_price: Decimal = Field(..., alias="unitPrice")

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True


class OrderItemUpdate(BaseModel):
    order_item: Optional[str] = Field(..., alias="orderItem")
    unit_price: Optional[Decimal] = Field(None, alias="unitPrice")

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True
