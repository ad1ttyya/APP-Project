from sqlalchemy import text,create_engine

connection_string ="mysql+mysqlconnector://38qgj2jzjlqiptyqih4i:pscale_pw_UdvHoFuJsbsVnjQMSoRPVBjYUdHPY1fDNdszfnuxMZT@aws.connect.psdb.cloud/shopez"

engine = create_engine(connection_string)
items=[]
def get_listing():
    for i in var:
        items.append(list(i))
    print(items)
with engine.connect() as connection:
    var=connection.execute(text("select * from ITEM_DATA"))