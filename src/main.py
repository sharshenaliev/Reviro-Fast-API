from fastapi import FastAPI
from fastapi_pagination import add_pagination
from sqladmin import Admin
from src.database import engine
from src.admin import ProductAdmin, EstablishmentAdmin
from src.routers import product_router, establishment_router


app = FastAPI()
app.include_router(product_router)
app.include_router(establishment_router)

admin = Admin(app, engine)
admin.add_view(ProductAdmin)
admin.add_view(EstablishmentAdmin)

add_pagination(app)
