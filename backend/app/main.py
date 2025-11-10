from fastapi import FastAPI
from app.expenses.views import router as expenses_router

app = FastAPI()

app.include_router(expenses_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Expense Manager API"}
