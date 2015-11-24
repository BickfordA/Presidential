from sqlalchemy.orm import create_session
from sqlalchemy.orm import Session
from sqlalchemy import desc

from app import db

import models

#add the model names here to make access a little easier
Candidate = models.Candidate
Google_trend = models.Google_trend
Location = models.Location

def newSession():
    return create_session(bind = db.engine);

def candidateNames(session):
    candidates = session.query(Candidate.Candidate_id, Candidate.Fname, Candidate.Lname).all()

    parsed = []
    for can in candidates:
        pc =[]
        pc.append(can[0])
        pc.append(str(can[1].encode('ascii', 'ignore') + " " + can[2].encode('ascii', 'ignore')))
        parsed.append(pc)

    return parsed


def canidateGoogleTrend(canId, session):
    q = session.query(Google_trend.Count,  Google_trend.Week).filter(Google_trend.Candidate_id == canId)
    q = q.order_by((Google_trend.Week))

    parsed = []
    for count in q.all():
        if count[0] is not None:
            parsed.append(count[0])

    return parsed


def candidateName(canId, session):
    q = session.query(Candidate.Fname, Candidate.Lname).filter(Candidate.Candidate_id == canId)
    #get the first entry
    names = q.first()
    #join the first
    return " ".join(names);

def candidateInfo(canId, session):
    q = session.query(Candidate.Fname, \
                    Candidate.Lname,\
                     Candidate.Party,\
                      Candidate.Bdate,\
                       Location.City,\
                        Location.State,\
                         Location.Population).join(Location)



    q = q.filter(Candidate.Candidate_id == canId)
    values = q.first();

    names = ['Fname', 'Lname', 'Party', "Birthday", "City", "State", "Population"]

    joinedInfo =  []
    for v in range( 0 , len(values)) :
        att = []
        att.append(names[v])
        att.append(values[v])
        joinedInfo.append(att)

    return joinedInfo
