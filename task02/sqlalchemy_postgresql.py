
# with open("../task01/serialnum",'r') as f:
#     print(f.read())
    # print(f.readline())

import pandas as pd
from sqlalchemy import Column, Table, String, Integer, MetaData, create_engine
from sqlalchemy.exc import DisconnectionError

class SaveToPostgres:

    def __init__(self):
        self.path = "../task01/serialnum"
        self.create_sql_table()



    def create_sql_table(self):
        engine = create_engine("postgresql+psycopg2://junfu:@localhost/task3",  pool_pre_ping=False)
        self.conn = engine.connect()
        meta = MetaData()
        self.serialnum = Table("serial_number", meta,
                          Column("id", Integer, primary_key=True),
                          Column("serial", String))

        meta.create_all(engine)

    def save_to_postgres(self):
        range_file = pd.read_csv(self.path)[['result']].values.ravel().tolist()
        for count, serial in enumerate(range_file):
            insert = self.serialnum.insert().values(id=count, serial=serial)
            self.conn.execute(insert)
        print(len(range_file))

        self.conn.close()


if __name__ == '__main__':
    example = SaveToPostgres()
    example.save_to_postgres()