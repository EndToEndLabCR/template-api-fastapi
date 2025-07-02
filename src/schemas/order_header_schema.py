from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, Field, model_validator
from datetime import datetime
from src.models.order_header import OrderHeaderModel



class OrderHeaderResponse(BaseModel):
    order_id: str = Field(..., alias="orderId")
    order_date: datetime = Field(..., alias="orderDate")
    total_amount: Decimal = Field(..., alias="totalAmount")

    @model_validator(mode="before")
    def validate_dates(cls, obj):
        if isinstance(obj, OrderHeaderModel):
            return {
                "order_id": obj.order_id,
                "order_date": obj.order_date.isoformat() if obj.order_date else None,
                "total_amount": obj.total_amount
            }

        return obj

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True


class OrderHeaderCreate(BaseModel):
    order_id: str = Field(..., alias="orderId")
    total_amount: Decimal = Field(..., alias="totalAmount")

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True


class OrderHeaderUpdate(BaseModel):
    total_amount: Optional[Decimal] = Field(None, alias="totalAmount")

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True
