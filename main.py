from fastapi import FastAPI
from routers import authRouter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(authRouter.router)
'''app.include_router(sellersRouter.router)
app.include_router(ProductsRouter.router)'''

@app.get("/")
async def root():
    return {"message": "Welcome to the E-commerce API"}