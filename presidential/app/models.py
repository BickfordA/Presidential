from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import reflection
from sqlalchemy.orm import relationship, backref

from app import db

db.Model.metadata.reflect(db.engine)

#engine = create_engine('mysql://root:root@localhost/PRESIDENTIAL')
#Base = declarative_base()
#Base.metadata.reflect(db)

#http://docs.sqlalchemy.org/en/latest/core/reflection.html

#Canidate = Table('CANDIDATE', db.Model.metadata, autoload = True, autoload_with = db.engine)

class Candidate(db.Model):
    #__table__ = db.Model.metadata.tables['CANDIDATE']
    __table__ = Table('CANDIDATE', db.Model.metadata, autoload = True, autoload_with = db.engine)



#class Foo(Base):
#    __table__ = Base.metadata.tables['foos']

#    bar = relationship(Bar, primaryjoin='Foo.bar_id == Bar.bar_id')


#http://stackoverflow.com/questions/33286518/flask-sqlalchemy-bind-causing-could-not-assemple-primary-key-error
#http://librelist.com/browser/flask/2012/5/23/flask-sqlalchemy-with-pre-existing-database/#9974419419ee1960c88c98689f6aee9d
