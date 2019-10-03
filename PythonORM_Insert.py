from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from PythonORM import Base, Teacher

engine = create_engine('sqlite:///teacher.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

new_teacher = Teacher(name='new teacher')
session.add(new_teacher)
session.commit()
