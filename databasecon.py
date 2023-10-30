from sqlalchemy import text,create_engine

connection_string ="mysql+mysqlconnector://uqherguranyqxm11k6ew:pscale_pw_z6PAlJnC4RAbVecv3SSVNYrspPO701qIJubmZPmhWrw@aws.connect.psdb.cloud/shopez"

engine = create_engine(connection_string)
items=[]
def get_listing():
    for i in var:
        items.append(list(i))
    print(items)
with engine.connect() as connection:
    var=connection.execute(text("select * from ITEM_DATA"))