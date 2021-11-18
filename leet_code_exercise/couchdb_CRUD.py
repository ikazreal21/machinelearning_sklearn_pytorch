from cloudant.client import CouchDB


def ConnectCouchdb(admin, password):
    client = CouchDB(admin, password, url="http://0.0.0.0:5984", connect=True)
    return client


def CreateOpenDatabase(name):
    client = ConnectCouchdb("admin", "password")
    database = client.create_database(name)
    if database.exists():
        print("All Ready Exist")
        database = client[name]
        return database
    else:
        database = client.create_database(name)
        if database.exists():
            print("Success")
        return database


def CreateDocument(data):
    database = CreateOpenDatabase("test_database")
    my_document = database.create_document(data)
    if my_document.exists():
        print("SUCCESS!!")


def RetrieveDocument(data):
    database = CreateOpenDatabase("test_database")
    my_document = database[data]
    print(my_document)


def RetieveAllDocuments():
    database = CreateOpenDatabase("test_database")
    for document in database:
        print(document)


def UpdateDocument(data, keys, value):
    database = CreateOpenDatabase("test_database")
    my_document = database[data]
    for key, val in zip(keys, value):
        my_document[key] = val
    my_document.save()


def DeleteDocument(data):
    database = CreateOpenDatabase("test_database")
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


# CreateDocument(data)
# RetrieveDocument("testdata")
# UpdateDocument("testdata", keys, value)
# DeleteDocument("testdata")
