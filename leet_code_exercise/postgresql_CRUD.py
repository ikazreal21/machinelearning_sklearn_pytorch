import psycopg2


def ConnectDB(database, user, password):
    con = psycopg2.connect(
        database=database,
        user=user,
        password=password,
        host="127.0.0.1",
    )
    print("Database opened successfully")
    return con


def CreateTable(query):
    con = ConnectDB("postgres", "postgres", "zakizakizaki")
    cur = con.cursor()
    cur.execute(query)
    print("Table created successfully")

    con.commit()
    con.close()


def InsertData(data):
    con = ConnectDB("postgres", "postgres", "zakizakizaki")
    cur = con.cursor()
    for i in data:
        cur.execute(i)

    con.commit()
    print("Record inserted successfully")
    con.close()


def RetrieveData(query):
    con = ConnectDB("postgres", "postgres", "zakizakizaki")
    cur = con.cursor()
    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print("ADMISSION =", row[0])
        print("NAME =", row[1])
        print("AGE =", row[2])
        print("COURSE =", row[3])
        print("DEPARTMENT =", row[4], "\n")

    print("Operation done successfully")
    con.close()


def UpdateData(data, query):
    con = ConnectDB("postgres", "postgres", "zakizakizaki")
    cur = con.cursor()
    for i in data:
        cur.execute(i)
    con.commit()
    print("Total updated rows:", cur.rowcount)
    RetrieveData(query)
    print("Operation done successfully")
    con.close()


def DeleteData(data, query):
    con = ConnectDB("postgres", "postgres", "zakizakizaki")
    cur = con.cursor()
    for i in data:
        cur.execute(i)
    con.commit()
    con.commit()
    print("Total deleted rows:", cur.rowcount)
    RetrieveData(query)
    print("Deletion successful")
    con.close()


table_creation = """CREATE TABLE STUDENT
	      (
	      ADMISSION INT PRIMARY KEY     NOT NULL,
	      NAME           TEXT    NOT NULL,
	      AGE            INT     NOT NULL,
	      COURSE        CHAR(50),
	      DEPARTMENT        CHAR(50)
	      );"""

data_inserted = [
    "INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3420, 'John', 18, 'Computer Science', 'ICT');",
    "INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3421, 'Joaquin', 20, 'Information Technology', 'ICT');",
    "INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3422, 'Janine', 19, 'Mechanical Engineering', 'Engineering')",
    "INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3423, 'Colston', 18, 'Information Technology', 'ICT')",
]

retieve_query = "SELECT admission, name, age, course, department from STUDENT"

data_update = ["UPDATE STUDENT set AGE = 20 where ADMISSION = 3420;"]

data_delete = ["DELETE from STUDENT where ADMISSION=3420;"]


# CreateTable(table_creation) ## Run First
# InsertData(data_inserted) ## Run Second
# RetrieveData(retieve_query) ## Run Third
# UpdateData(data_update, retieve_query) ## Run Fourth
# DeleteData(data_delete, retieve_query) ## Run Fifth
