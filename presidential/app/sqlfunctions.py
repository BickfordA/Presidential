from sqlalchemy.orm import create_session
from sqlalchemy.orm import Session

from app import db

import models

Candidate = models.Candidate

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
