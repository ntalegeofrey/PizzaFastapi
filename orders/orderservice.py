from fastapi import Depends, HTTPException, status
from .schema import OrderModel, OrderStatusModel
from config.token import get_currentUser
from users.models import User
from .models import Order
from sqlalchemy.orm import Session
from config.database import get_db


class OrderService:
    def get_all(
        current_user: User = Depends(get_currentUser), db: Session = Depends(get_db)
    ):
        users = db.query(User).filter(User.email == current_user.email).first()

        if users.is_staff:
            orders = db.query(Order).all()

            return orders
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not a superuser"
        )

    def create_order(
        order: OrderModel,
        current_user: User = Depends(get_currentUser),
        db: Session = Depends(get_db),
    ):
        users = db.query(User).filter(User.email == current_user.email).first()

        new_order = Order(pizza_size=order.pizza_size, quantity=order.quantity)

        new_order.user = users

        db.add(new_order)

        db.commit()

        return new_order

    def show_order(
        id: int,
        current_user: User = Depends(get_currentUser),
        db: Session = Depends(get_db),
    ):
        users = db.query(User).filter(User.email == current_user.email).first()

        if users.is_staff:
            order = db.query(Order).filter(Order.id == id).first()

            return order

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not alowed to carry out request",
        )

    def getUserOrders(
        current_user: User = Depends(get_currentUser), db: Session = Depends(get_db)
    ):
        users = db.query(User).filter(User.email == current_user.email).first()

        return users.orders

    def getSpesificOrder(
        id: int,
        current_user: User = Depends(get_currentUser),
        db: Session = Depends(get_db),
    ):
        users = db.query(User).filter(User.email == current_user.email).first()

        orders = users.orders

        for o in orders:
            if o.id == id:
                return o

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="No order with such id"
        )

    def updateOrder(
        id: int,
        order: OrderModel,
        current_user: User = Depends(get_currentUser),
        db: Session = Depends(get_db),
    ):
        order_toupdate = db.query(Order).filter(Order.id == id).first()

        order_toupdate.quantity = order.quantity
        order_toupdate.pizza_size = order.pizza_size

        db.commit()

        return order_toupdate

    def updateOrderStatus(
        order: OrderStatusModel,
        current_user: User = Depends(get_currentUser),
        db: Session = Depends(get_db),
    ):
        users = db.query(User).filter(User.email == current_user.email).first()

        if users.is_staff:
            order_to_update = db.query(Order).filter(Order.id == id).first()

            order_to_update.order_status = order.order_status

            db.commit()

            return order_to_update

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not alowed to carry out request",
        )

    def deleteOrder(
        id: int,
        current_user: User = Depends(get_currentUser),
        db: Session = Depends(get_db),
    ):
        order_delete = db.query(Order).filter(Order.id == id).first()

        db.delete(order_delete)

        db.commit()

        return order_delete
