from sqladmin import ModelView
from src.models import Product, Establishment


class ProductAdmin(ModelView, model=Product):
    column_list = [Product.product_id, Product.name]
    column_searchable_list = [Product.name]


class EstablishmentAdmin(ModelView, model=Establishment):
    column_list = [Establishment.establishment_id, Establishment.name]
    column_searchable_list = [Establishment.name]
