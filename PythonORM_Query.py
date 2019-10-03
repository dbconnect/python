from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from PythonORM import Base, Teacher

engine = create_engine('sqlite:///teacher.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

teacher = session.query(Teacher).first()
print('Id: {0}, Name: {1}'.format(teacher.id, teacher.name))
