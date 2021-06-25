from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, ARRAY, select
import json

# Global Variables
SQLITE                  = 'sqlite'

class MyDatabase:
    # http://docs.sqlalchemy.org/en/latest/core/engines.html
    DB_ENGINE = {
        SQLITE: 'sqlite:///{DB}'
    }

# Main DB Connection Ref Obj
    db_engine = None
    def __init__(self, dbtype, dbname=''):
        dbtype = dbtype.lower()
        if dbtype in self.DB_ENGINE.keys():
            engine_url = self.DB_ENGINE[dbtype].format(DB=dbname)
            self.db_engine = create_engine(engine_url)
            metadata = MetaData()
            self.data = Table('client_data', metadata,
                        Column('id', Integer, primary_key=True),
                        Column('raw_data1', Integer),
                        Column('raw_data2', Integer),
                        Column('raw_data3', Integer),
                        Column('result', Integer)
                        )
            try:
                metadata.create_all(self.db_engine)
                print("Tables created")
            except Exception as e:
                print("Error occurred during Table creation!")
                print(e)
        else:
            print("DBType is not found in DB_ENGINE")


    def create_db_tables(self):
        metadata = MetaData()
        self.data = Table('client_data', metadata,
                      Column('id', Integer, primary_key=True),
                      Column('raw_data1', Integer),
                      Column('raw_data2', Integer),
                      Column('raw_data3', Integer),
                      Column('result', Integer)
                    )
        try:
            metadata.create_all(self.db_engine)
            print("Tables created")
        except Exception as e:
            print("Error occurred during Table creation!")
            print(e)

# Insert, Update, Delete
    def getResult(self, id):
        # Sample Query
        query = select([self.data.columns.result]).where(self.data.c.id == id)
        with self.db_engine.connect() as connection:
            try:
                result = connection.execute(query)
            except Exception as e:
                print(e)
            else:
                for row in result:
                    return row[0]
                result.close()

    def insert(self, _id, data):
        # Insert Data
        query = self.data.insert().values(id = _id, raw_data1 = data[0], raw_data2 = data[1], raw_data3 = data[2])
        with self.db_engine.connect() as connection:
            try:
                connection.execute(query)
            except Exception as e:
                print(e)

    def updateResult(self, id, _result):
        # Update Data
        query = self.data.update().where(self.data.c.id==id).values(result=_result)
        with self.db_engine.connect() as connection:
            try:
                connection.execute(query)
            except Exception as e:
                print(e)