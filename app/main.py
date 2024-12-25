from fastapi import FastAPI
from backend.user import router as user_router

app = FastAPI()

# Подключение маршрутов
app.include_router(user_router)

# Точка входа
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
