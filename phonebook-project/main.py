from typing import List
from fastapi import FastAPI, status, HTTPException, Depends
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
import models
import schemas

# Create the database
Base.metadata.create_all(engine)

# Initialize app
app = FastAPI()


# Helper function to get database session
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@app.get("/")
def root():
    return {"msg": "Welcome to Narvan Phone Book App :)"}


@app.post("/create", response_model=schemas.Contact, status_code=status.HTTP_201_CREATED)
def create_todo(contact: schemas.ContactCreate, session: Session = Depends(get_session)):

    contactDB = models.Contact(first_name=contact.first_name,
                               last_name=contact.last_name,
                               phone_number=contact.phone_number)

    # add it to the session and commit it
    session.add(contactDB)
    session.commit()
    session.refresh(contactDB)

    # return the todo object
    return contactDB


@app.get("/find/{txt}", response_model=List[schemas.Contact])
def read_todo(txt: str, session: Session = Depends(get_session)):

    contactsList = session.query(models.Contact).all()
    matchingContacts = list()

    for item in contactsList:
        if txt in item.first_name or txt in item.last_name or txt in item.phone_number:
            matchingContacts.append(item)


    if len(matchingContacts) == 0:
        raise HTTPException(status_code=404, detail="No such a contact found")

    return matchingContacts


@app.put("/edit/{id}", response_model=schemas.Contact)
def update_todo(id: int, cont: schemas.ContactCreate, session: Session = Depends(get_session)):

    # get the contact with the given id
    contact = session.query(models.Contact).get(id)

    if contact:
        contact.first_name = cont.first_name
        contact.last_name = cont.last_name
        contact.phone_number = cont.phone_number
        session.commit()

    # check if the contact with given id exists. If not, raise exception and return 404 not found response
    if not contact:
        raise HTTPException(status_code=404, detail=f"Contact with id {id} not found")

    return contact


@app.delete("/remove/{id}", status_code=status.HTTP_200_OK, response_model=str)
def delete_todo(id: int, session: Session = Depends(get_session)):

    # get the contact with the given id
    contact = session.query(models.Contact).get(id)

    if contact:
        session.delete(contact)
        session.commit()
    
    else:
        raise HTTPException(status_code=404, detail=f"Contact with id {id} not found")


    return f"{contact.first_name} {contact.last_name} has been removed."
    


@app.get("/all-contacts", response_model = List[schemas.Contact])
def read_todo_list(session: Session = Depends(get_session)):

    # get all contacts
    allContacts = session.query(models.Contact).all()

    return allContacts