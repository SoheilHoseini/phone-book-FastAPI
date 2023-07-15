import grpc
import phonebook_pb2, phonebook_pb2_grpc



def get_contact(stub):
    pass


def get_all_contacts(stub):
    pass


def remove_contact(stub):
    pass


def update_contact(stub):
    pass


def create_contact(stub):
    pass


def run():

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = phonebook_pb2_grpc.PhoneBookStub(channel)
        print("-------------- Get --------------")
        get_contact(stub)
        print("-------------- Get All --------------")
        get_all_contacts(stub)
        print("-------------- Remove --------------")
        remove_contact(stub)
        print("-------------- Update --------------")
        update_contact(stub)
        print("-------------- Create --------------")
        create_contact(stub)



if __name__ == '__main__':
    run()
