from fastapi import FastAPI
from config.settings import Settings
from config.database import Base, engine
from users import usersrouter
from auth import authrouter
from orders import orderrouter

Base.metadata.create_all(bind=engine)


app = FastAPI(title=Settings.PROJECT_NAME, version=Settings.PROJECT_VERSION)


@app.get("/")
def hello():
    return "Hello World"


app.include_router(usersrouter.router)
app.include_router(authrouter.router)
app.include_router(orderrouter.router)
