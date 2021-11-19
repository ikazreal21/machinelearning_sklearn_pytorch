import psycopg2


class PostgresDriver:
    def __init__(self, database, user, password):
        self.database = database
        self.user = user
        self.password = password

    def connect_database(self, database, user, password):
        con = psycopg2.connect(
            database=database,
            user=user,
            password=password,
            host="127.0.0.1",
        )
        print("Database opened successfully")
        return con

    def create_table(self, query):
        con = self.connect_database(self.database, self.user, self.password)
        cur = con.cursor()
        cur.execute(query)
        print("Table created successfully")

        con.commit()
        con.close()

    def insert_data(self, data):
        con = self.connect_database(self.database, self.user, self.password)
        cur = con.cursor()
        for i in data:
            cur.execute(i)

        con.commit()
        print("Record inserted successfully")
        con.close()

    def retrieve_data(self, query):
        con = self.connect_database(self.database, self.user, self.password)
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

    def update_data(self, data, query):
        con = self.connect_database(self.database, self.user, self.password)
        cur = con.cursor()
        for i in data:
            cur.execute(i)
        con.commit()
        print("Total updated rows:", cur.rowcount)
        RetrieveData(query)
        print("Operation done successfully")
        con.close()

    def delete_data(self, data, query):
        con = self.connect_database(self.database, self.user, self.password)
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


driver = PostgresDriver("postgres", "postgres", "zakizakizaki")
# driver.create_table(table_creation)
# driver.insert_data(data_inserted)
# driver.retrieve_data(retieve_query)
# driver.update_data(data_update, retieve_query)
# driver.delete_data(data_delete, retrieve_query)
