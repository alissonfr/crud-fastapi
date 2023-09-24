import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routers import user

app = FastAPI()

app.include_router(user.router, tags=['Users'], prefix='/api/user')

@app.get('/api/')
def root():
    return {'message': 'Hello World'}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8080)