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

def candidateTopContributionState(canId, session):

    result = session.execute("""SELECT Fname, Lname, `Home State`, `Home State Count`, `Home State Amount`, `Top State`,
                                `Top State Count`, `Top State Amount`
                                FROM
                                (
                                	#Select the home state values
                                	SELECT H.Candidate_id,Fname, Lname, H.State as "Home State",
                                    Count as "Home State Count", Amount as "Home State Amount"
                                    from (
                                	#find the state and candidate amounts
                                	SELECT Candidate_id, State, COUNT(*) AS "Count", SUM(Amount) AS "Amount"
                                    from CAMPAIGN_CONTRIBUTION
                                    GROUP BY Candidate_id, State
                                	) H
                                JOIN
                                	(
                                	SELECT CANDIDATE.Candidate_id, State, Fname, Lname
                                	FROM
                                	CANDIDATE JOIN LOCATION ON CANDIDATE.Hometown = LOCATION.Location_id
                                	) J
                                		ON J.State = H.State
                                	WHERE J.`Candidate_id` = H.`Candidate_id`
                                ) K
                                JOIN
                                (
                                	# Top donor state for each candidate
                                	SELECT A.Candidate_id, A.State AS "Top State", A.Count AS "Top State Count",
                                    A.Amount as "Top State Amount"
                                    From
                                    (
                                        SELECT Candidate_id, State, COUNT(*) AS "Count", SUM(Amount) AS "Amount"
                                        from CAMPAIGN_CONTRIBUTION
                                        GROUP BY Candidate_id, State
                                    ) as A
                                	LEFT JOIN
                                    (
                                        SELECT Candidate_id, State, COUNT(*) AS "Count", SUM(Amount) AS "Amount"
                                        FROM CAMPAIGN_CONTRIBUTION GROUP BY Candidate_id, State
                                    ) as B
                                		on A.Candidate_id = B.Candidate_id
                                		AND A.Amount < B.Amount
                                	WHERE B.Amount is NULL
                                ) L
                                ON K.Candidate_id = L.Candidate_id\
                                WHERE K.Candidate_id = :canId""", {'canId': canId})

    row = result.fetchone();
    retVal = {"Home State" : row["Home State"],
            "Home State Count" : row["Home State Count"],
            "Home State Amount": row["Home State Amount"],
            "Top State" : row["Top State"],
            "Top State Count" : row["Top State Count"],
            "Top State Amount" : row["Top State Amount"]
            };

    return retVal;
