from binascii import Error
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db import engine,Base
from .app_auth.auth_router import app as auth_app
from .seller.seller_router import app as seller_app
from .client.client_router import app as client_app

from .admin_panel.admin_router import app as admin_app

from .prodcuts.products_models import Product, Category, SubCategory
from .seller.seller_models import SellerProfile, SellerProduct
from .client.client_models import ClientBacket


app = FastAPI()

# routers
app.include_router(auth_app)
app.include_router(seller_app)
app.include_router(client_app)


# ADMIN PANEL

app.include_router(admin_app)

# CORS

origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type",
                   "Set-Cookie",
                   "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)




# init project
@app.get("/init")
async def create_db():
    
    async with engine.begin() as conn:
        try:
            await conn.run_sync(Base.metadata.drop_all)
        except Error as e:
            print(e)
        await  conn.run_sync(Base.metadata.create_all)




