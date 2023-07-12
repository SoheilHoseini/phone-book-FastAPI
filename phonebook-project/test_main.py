from fastapi.testclient import TestClient
from main import app, get_session
import pytest
from database import Base
from sqlalchemy.pool import StaticPool
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import status


SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db_session():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


client = TestClient(app)

# override database for testing 
app.dependency_overrides[get_session] = override_get_db_session


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Welcome to Narvan Phone Book App :)"}


def test_inexistent_contact():
    response = client.get("/find/99")
    assert response.status_code == 404
    assert response.json() == {"detail": "No such a contact found"}


def test_existng_contact():
    response = client.post(
        "/create",
        json={"first_name": "jon",
              "last_name": "snow",
              "phone_number": "09111111111"}
        )
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    user_id = data["id"]
    
    response = client.get(f"/get-contact/{user_id}")
    assert response.status_code == 200
    assert response.json() == data


def test_deleting_contact():
    response = client.post(
        "/create",
        json={"first_name": "aryaa",
              "last_name": "stark",
              "phone_number": "09111111000"}
        )
    data = response.json()

    assert response.status_code == status.HTTP_201_CREATED

    user_id = data["id"]
    fName = data["first_name"]
    lName = data["last_name"]

    # needs work !!!!!!
    try:
        response = client.delete(f"/remove/{user_id}")
    except:
        print("errrrrrrrrrrr")
    print(response.json())
    # assert response.json() == {"msg": f"{fName} {lName} has been removed."}


def test_edit_contact():
    response = client.post(
        "/create",
        json={"first_name": "robert",
              "last_name": "bolton",
              "phone_number": "09111111000"}
        )
    user_id = response.json()["id"]

    response = client.patch(
        f"/edit/{user_id}",
        json={"first_name": "robert",
              "last_name": "barathion",
              "phone_number": "09111111000"}
        )
    
    # needs work !!!!
    # assert response.json() == 12

