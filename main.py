from database import create_tables, delete_tables
from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    print("База готова")
    yield
    await delete_tables()
    print("База очищена")

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)


@app.get("/")
async def home():
    return {"data": "Hello World"}
