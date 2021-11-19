from cloudant.client import CouchDB


class CouchDBDriver:
    def __init__(self, admin, password):
        self.admin = admin
        self.password = password

    def connect_couchdb(self, admin, password):
        client = CouchDB(admin, password, url="http://0.0.0.0:5984", connect=True)
        return client

    def create_database(self, name):
        client = self.connect_couchdb(self.admin, self.password)
        database = client.create_database(name)
        if database.exists():
            database = client[name]
            return database
        else:
            database = client.create_database(name)
            if database.exists():
                print("Success")
            return database

    def create_document(self, data, database_name):
        database = self.create_database(database_name)
        my_document = database.create_document(data)
        if my_document.exists():
            print("SUCCESS!!")

    def retrieve_document(self, data, database_name):
        database = self.create_database(database_name)
        my_document = database[data]
        print(my_document)

    def retieve_all_documents(self, database_name):
        database = self.create_database(database_name)
        for document in database:
            print(document)

    def update_document(self, data, keys, value, database_name):
        database = self.create_database(database_name)
        my_document = database[data]
        for key, val in zip(keys, value):
            my_document[key] = val
        my_document.save()

    def delete_document(self, data, database_name):
        database = self.create_database(database_name)
        my_document = database[data]
        if my_document.exists():
            my_document.delete()
            print("Document Deleted")
        else:
            print("Document Doesnt Exist")


data = {
    "_id": "testdata",
    "name": "Joaquin",
    "age": 20,
    "pets": ["turtle", "snake", "cat"],
}

keys = ["name", "age"]
value = ["Zaki", 21]


driver = CouchDBDriver("admin", "password")
# driver.create_database("test_database")
# driver.create_document(data, "test_database")
# driver.retrieve_document("testdata", "test_database")
# driver.retieve_all_documents("test_database")
# driver.update_document("testdata", keys, value, "test_database")
# driver.delete_document("testdata", "test_database")
