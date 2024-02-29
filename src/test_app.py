from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from fastapi.testclient import TestClient
from src.main import app
from src.models import Base
from src.database import get_db
import factory
import unittest
from src.models import Product, Establishment


client = TestClient(app)


DATABASE_URL = "sqlite:///test.db"
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
Session = scoped_session(TestingSessionLocal)


class ProductFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Product
        sqlalchemy_session = Session
        sqlalchemy_session_persistence = "commit"

    name = factory.Faker('name')
    description = factory.Faker('text')
    price = factory.Faker('pyint')
    quantity_in_stock = factory.Faker('pyint')


class EstablishmentFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Establishment
        sqlalchemy_session = Session
        sqlalchemy_session_persistence = "commit"

    name = factory.Faker('name')
    description = factory.Faker('text')
    location = factory.Faker('address')
    opening_hours = factory.Faker('time')


class ProductTest(unittest.TestCase):

    def test_list_product(self):
        product = ProductFactory()
        response = client.get("/product/")
        assert response.status_code == 200
        expected_data = {
            'items': [
                {
                    'product_id': product.product_id,
                    'name': product.name,
                    'description': product.description,
                    'price': product.price,
                    'quantity_in_stock': product.quantity_in_stock
                }
            ], 'total': 1, 'page': 1, 'size': 50, 'pages': 1}
        assert response.json() == expected_data

    def test_post_product(self):
        product = ProductFactory.build()
        expected_data = {
            'product_id': 1,
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'quantity_in_stock': product.quantity_in_stock
        }
        response = client.post("/product/", json=expected_data)
        assert response.status_code == 201
        assert response.json() == expected_data

    def test_get_product(self):
        product = ProductFactory()
        response = client.get(f"/product/{product.product_id}/")
        assert response.status_code == 200
        expected_data = {
            'product_id': product.product_id,
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'quantity_in_stock': product.quantity_in_stock
        }
        assert response.json() == expected_data

    def test_put_product(self):
        product = ProductFactory()
        expected_data = {
            'product_id': product.product_id,
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'quantity_in_stock': product.quantity_in_stock
        }
        response = client.put(f"/product/{product.product_id}/", json=expected_data)
        assert response.status_code == 200
        assert response.json() == expected_data

    def test_delete_product(self):
        product = ProductFactory()
        response = client.delete(f"/product/{product.product_id}/")
        assert response.status_code == 204

    def tearDown(self):
        Session.query(Product).delete()
        Session.commit()
        Session.rollback()
        Session.remove()


class EstablishmentTest(unittest.TestCase):

    def test_list_establishment(self):
        establishment = EstablishmentFactory()
        response = client.get("/establishment/")
        assert response.status_code == 200
        expected_data = {
            'items': [
                {
                    'establishment_id': establishment.establishment_id,
                    'name': establishment.name,
                    'description': establishment.description,
                    'location': establishment.location,
                    'opening_hours': establishment.opening_hours
                }
            ], 'total': 1, 'page': 1, 'size': 50, 'pages': 1}
        assert response.json() == expected_data

    def test_post_establishment(self):
        establishment = EstablishmentFactory.build()
        expected_data = {
            'establishment_id': 1,
            'name': establishment.name,
            'description': establishment.description,
            'location': establishment.location,
            'opening_hours': establishment.opening_hours
        }
        response = client.post("/establishment/", json=expected_data)
        assert response.status_code == 201
        assert response.json() == expected_data

    def test_get_establishment(self):
        establishment = EstablishmentFactory()
        response = client.get(f"/establishment/{establishment.establishment_id}/")
        assert response.status_code == 200
        expected_data = {
            'establishment_id': establishment.establishment_id,
            'name': establishment.name,
            'description': establishment.description,
            'location': establishment.location,
            'opening_hours': establishment.opening_hours
        }
        assert response.json() == expected_data

    def test_put_establishment(self):
        establishment = EstablishmentFactory()
        expected_data = {
            'establishment_id': establishment.establishment_id,
            'name': establishment.name,
            'description': establishment.description,
            'location': establishment.location,
            'opening_hours': establishment.opening_hours
        }
        response = client.put(f"/establishment/{establishment.establishment_id}/", json=expected_data)
        assert response.status_code == 200
        assert response.json() == expected_data

    def test_delete_establishment(self):
        establishment = EstablishmentFactory()
        response = client.delete(f"/establishment/{establishment.establishment_id}/")
        assert response.status_code == 204

    def tearDown(self):
        Session.query(Establishment).delete()
        Session.commit()
        Session.rollback()
        Session.remove()
