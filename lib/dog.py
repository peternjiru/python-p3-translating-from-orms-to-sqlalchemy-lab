from models import Dog
from sqlalchemy import (create_engine,Column,Integer, String) 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import Base, Dog
from testing.conftest import db_dir, SQLITE_URL

engine = create_engine(SQLITE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(engine)
session = Session()

Base = declarative_base()

class Dog(Base):
    __tablename__ = "dogs" 

    id = Column(Integer(),  primary_key=True)
    name = Column(String())
    breed = Column(String()) 

def create_table(Base, engine):   
    if __name__ == '__main__':
        # engine = create_engine('sqlite:///dogs.db')
        # engine = create_engine(SQLITE_URL)
        Base.metadata.create.all(engine)
    
def save(session, dog):
    print(dog.name)
    session.add(dog)
    session.commit()
    print(f"new dog {dog.name}")
    return session.query(Dog).first().name
    
def get_all(session):
    all_dogs = []
    all_dogs = session.query(Dog).all()
    return all_dogs

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name == name).first()
 
def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id == id).first()

def find_by_name_and_breed(session, name, breed):
  return session.query(Dog).filter(Dog.name == name , Dog.breed == breed).first()

def update_breed(session, dog, breed):
   print(dog.breed, breed)
   session.query(Dog).update({Dog.breed : breed})
   session.commit()




        
# dog = Dog(name="conan", breed="chihuahua")
# session.add(dog)
# session.commit()
        
# conan = find_by_name(session, 'conan')
# print("this should be conan", conan)