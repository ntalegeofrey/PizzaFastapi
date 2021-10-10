from pydantic import BaseModel
from typing import Optional


class OrderModel(BaseModel):
    id: Optional[int]
    quantity: int
    order_status: Optional[str] = "PENDING"
    pizza_size: Optional[str] = "SMALL"
    user_id: Optional[int]

    class Config:
        orm_mode = True
        schema_extra = {"example": {"quantity": 2, "pizza_size": "LARGE"}}


class OrderStatusModel(BaseModel):
    order_status: Optional[str] = "PENDING"
