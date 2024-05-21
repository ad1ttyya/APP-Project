from sqlalchemy import text,create_engine

connection_string ="REPLACE WITH YOUR CONNECTION STRING"

engine = create_engine(connection_string)
items=[]
def get_listing():
    for i in var:
        items.append(list(i))
    print(items)
with engine.connect() as connection:
    var=connection.execute(text("select * from ITEM_DATA"))
