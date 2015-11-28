from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import reflection
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.automap import automap_base

from app import db

db.Model.metadata.reflect(db.engine)

#prepare the database
Presidential = automap_base();
Presidential.prepare(db.engine, reflect = True)


#set up the tables
Campaign_contribution = Presidential.classes.CAMPAIGN_CONTRIBUTION

Candidate = Presidential.classes.CANDIDATE

Debate = Presidential.classes.DEBATE

Election = Presidential.classes.ELECTION

Election_results = Presidential.classes.ELECTION_RESULTS

Location = Presidential.classes.LOCATION

Net_worth = Presidential.classes.NET_WORTH

Opinion_poll = Presidential.classes.OPINION_POLL

Search_mention = Presidential.classes.SEARCH_MENTION

Search_tag = Presidential.classes.SEARCH_TAG

Twitter_search = Presidential.classes.TWITTER_SEARCH

Google_trend = Presidential.classes.GOOGLE_TREND

#Debate_participant = Presidential.classes.DEBATE_PARTICIPANT
# i cant get this to work , maybe add a pKey to fix it
#ALTER TABLE old_table ADD pk_column INT AUTO_INCREMENT PRIMARY KEY;
#http://docs.sqlalchemy.org/en/rel_0_9/orm/extensions/automap.html


#class Foo(Base):
#    __table__ = Base.metadata.tables['foos']

#    bar = relationship(Bar, primaryjoin='Foo.bar_id == Bar.bar_id')

#http://docs.sqlalchemy.org/en/latest/core/reflection.html

#http://stackoverflow.com/questions/33286518/flask-sqlalchemy-bind-causing-could-not-assemple-primary-key-error
#http://librelist.com/browser/flask/2012/5/23/flask-sqlalchemy-with-pre-existing-database/#9974419419ee1960c88c98689f6aee9d
