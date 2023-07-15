import phonebook_pb2_grpc, phonebook_pb2
import grpc
from concurrent import futures
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
import models

# Create the database
Base.metadata.create_all(engine)

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class PhoneBookServicer(phonebook_pb2_grpc.PhoneBookServicer):

    def Get(self, request:phonebook_pb2.ID, context):
        db = get_db()
        contact = db.query(models.Contact).get(request.id)
        
        if not contact:
            return None
        else:
            return contact
    

    def GetAll(self, request, context):
        db = get_db()
        allContacts = db.query(models.Contact).all()

        return allContacts
    

    def Remove(self, request:phonebook_pb2.ID, context):
        db = get_db()
        contact = db.query(models.Contact).get(request.id)

        if contact:
            db.delete(contact)
            db.commit()


    def Create(self, request:phonebook_pb2.Contact, context):
        db = get_db()
        newContact = models.Contact(first_name=request.first_name,
                               last_name=request.last_name,
                               phone_number=request.phone_number)


        # add it to the session and commit it
        db.add(newContact)
        db.commit()
        db.refresh(newContact)

        # return the todo object
        return newContact


    def Update(self, request:phonebook_pb2.Contact, context):
        db = get_db()
        contact = db.query(models.Contact).get(id)

        if contact:
            contact.first_name = request.first_name
            contact.last_name = request.last_name
            contact.phone_number = request.phone_number
            db.commit()

        return contact


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    phonebook_pb2_grpc.add_PhoneBookServicer_to_server(PhoneBookServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()