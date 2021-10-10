from fastapi import APIRouter, status, Depends
from sqlalchemy.orm.session import Session
from orders.schema import OrderModel, OrderStatusModel
from users.models import User
from config.token import get_currentUser
from .orderservice import OrderService
from config.database import get_db

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.get("/")
def getAll(
    current_user: User = Depends(get_currentUser), db: Session = Depends(get_db)
):
    return OrderService.get_all(current_user=current_user, db=db)


@router.post("/")
def createOrder(
    order: OrderModel,
    current_user: User = Depends(get_currentUser),
    db: Session = Depends(get_db),
):
    return OrderService.create_order(order=order, current_user=current_user, db=db)


@router.get("/{id}")
def showOrder(
    id: int,
    current_user: User = Depends(get_currentUser),
    db: Session = Depends(get_db),
):
    return OrderService.show_order(id=id, current_user=current_user, db=db)


@router.get("/user/orders")
def getUserOrders(
    current_user: User = Depends(get_currentUser), db: Session = Depends(get_db)
):
    return OrderService.getUserOrders(current_user=current_user, db=db)


@router.get("/user/order/{id}")
def getSpesificOrder(
    id: int,
    current_user: User = Depends(get_currentUser),
    db: Session = Depends(get_db),
):
    return OrderService.getSpesificOrder(id=id, current_user=current_user, db=db)


@router.put("/update/{id}")
def updateOrder(
    id: int,
    order: OrderModel,
    current_user: User = Depends(get_currentUser),
    db: Session = Depends(get_db),
):
    return OrderService.updateOrder(
        id=id, order=order, current_user=current_user, db=db
    )


@router.put("/update/status/{id}")
def updateOrderStatus(
    order: OrderStatusModel,
    current_user: User = Depends(get_currentUser),
    db: Session = Depends(get_db),
):
    return OrderService.updateOrderStatus(order=order, current_user=current_user, db=db)


@router.delete("/delete/{id}")
def deleteOrder(
    id: int,
    current_user: User = Depends(get_currentUser),
    db: Session = Depends(get_db),
):
    return OrderService.deleteOrder(id=id, current_user=current_user, db=db)
