from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


db_url = "mysql+pymysql://root:root@localhost:3306/product"
engine = create_engine(db_url)
session = sessionmaker(engine)