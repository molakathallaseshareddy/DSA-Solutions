from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine

Base = declarative_base()
db_url = "mysql+pymysql://root:root@localhost:3306/student_db"
engine = create_engine(db_url)
sessionlocal = sessionmaker(autoflush = False, autocommit = False, bind = engine)

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()