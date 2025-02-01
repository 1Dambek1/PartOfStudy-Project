from binascii import Error
import os
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from .db import engine,Base
from .app_auth.auth_router import app as auth_app
from .seller.seller_router import app as seller_app
from .client.client_router import app as client_app
from .orders.orders_router import app as orders_app

from .admin_panel.admin_router import app as admin_app
from .chat.chat_router import app as chat_app

# from src.models.products_models.ProductModel import Product
# from src.models.products_models.CategoryModel import Category
# from src.models.products_models.SubCategoryModel import SubCategory
# from src.models.seller_models.SellerProfileModel import SellerProfile
# from src.models.seller_models.SellerProductModel import SellerProduct
# from src.models.ClientBacketModel import ClientBacket
# from src.models.OrdersModel import Orders, OrdersSellerProduct
# from src.models.ChatModel import Chat, Message
from fastapi.responses import FileResponse





# 010100101010101001010101010
# 010100101010101001010101010
#  .jpeg .png .jpg .gif .svg




app = FastAPI()

# routers
app.include_router(auth_app)
app.include_router(seller_app)
app.include_router(client_app)
app.include_router(orders_app)
app.include_router(chat_app)

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




import shutil


UPLOAD_FOLDER = 'uploads'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# @app.post("/upload")
# async def upload_file(file_name: str, file: UploadFile = File(...)):
#     # file_location = f"{UPLOAD_DIR}/{file.filename}"
#     # with open(file_location, "wb") as buffer:
#     #     shutil.copyfileobj(file.file, buffer)
    
    
#     file_location = f"{UPLOAD_FOLDER}/{file_name}.png"
    
    
#     with open(file_location, "wb") as f:
#         f.write(await file.read())
#     return {"filename": file_name}



# @app.get("/files")
# async def get_files(file_name: str):
#     file_location = f"{UPLOAD_FOLDER}/{file_name}.png"
#     if not os.path.exists(file_location):
#         return {"error": "File not found"}
#     return FileResponse(file_location)



