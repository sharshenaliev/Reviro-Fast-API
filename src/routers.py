from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy import select
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import Product, Establishment
from src.schemas import ProductGet, ProductCreate, EstablishmentGet, EstablishmentCreate


product_router = APIRouter(
    prefix="/product",
    tags=["Operation"]
)


@product_router.get("/", response_model=Page[ProductGet], status_code=200)
async def list_product(db: Session = Depends(get_db)):
    return paginate(db, select(Product).order_by(Product.product_id))


@product_router.get("/{product_id}/", response_model=ProductGet, status_code=200)
async def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No product found")
    return product


@product_router.post("/", response_model=ProductGet, status_code=201)
async def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    new_product = Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


@product_router.put("/{product_id}/", response_model=ProductGet, status_code=200)
async def update_product(product_id: int, product: ProductCreate, db: Session = Depends(get_db)):
    updated_product = db.get(Product, product_id)
    if not updated_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No product found")
    else:
        update_data = product.dict(exclude_unset=True)
        db.query(Product).filter(Product.product_id == product_id).update(update_data, synchronize_session=False)
        db.commit()
        db.refresh(updated_product)
    return updated_product


@product_router.delete('/{product_id}/')
async def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No product found")
    else:
        db.query(Product).filter(Product.product_id == product_id).delete(synchronize_session=False)
        db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


establishment_router = APIRouter(
    prefix="/establishment",
    tags=["Operation"]
)


@establishment_router.get("/", response_model=Page[EstablishmentGet], status_code=200)
async def list_establishment(db: Session = Depends(get_db)):
    return paginate(db, select(Establishment).order_by(Establishment.establishment_id))


@establishment_router.get("/{establishment_id}/", response_model=EstablishmentGet, status_code=200)
async def get_establishment(establishment_id: int, db: Session = Depends(get_db)):
    establishment = db.get(Establishment, establishment_id)
    if not establishment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No establishment found")
    return establishment


@establishment_router.post("/", response_model=EstablishmentGet, status_code=201)
async def create_establishment(establishment: EstablishmentCreate, db: Session = Depends(get_db)):
    new_establishment = Establishment(**establishment.dict())
    db.add(new_establishment)
    db.commit()
    db.refresh(new_establishment)
    return new_establishment


@establishment_router.put("/{establishment_id}/", response_model=EstablishmentGet, status_code=200)
async def update_establishment(establishment_id: int, establishment: EstablishmentCreate, db: Session = Depends(get_db)):
    updated_establishment = db.get(Establishment, establishment_id)
    if not updated_establishment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No establishment found")
    else:
        update_data = establishment.dict(exclude_unset=True)
        db.query(Establishment).filter(Establishment.establishment_id == establishment_id).update(update_data, synchronize_session=False)
        db.commit()
        db.refresh(updated_establishment)
    return updated_establishment


@establishment_router.delete('/{establishment_id}/')
async def delete_establishment(establishment_id: int, db: Session = Depends(get_db)):
    product = db.get(Establishment, establishment_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No establishment found")
    else:
        db.query(Establishment).filter(Establishment.establishment_id == establishment_id).delete(synchronize_session=False)
        db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
