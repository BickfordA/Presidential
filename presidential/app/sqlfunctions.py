from sqlalchemy.orm import create_session
from sqlalchemy.orm import Session
from sqlalchemy import desc

from app import db

import models

#add the model names here to make access a little easier
Candidate = models.Candidate
Google_trend = models.Google_trend
Location = models.Location
Opinion_poll = models.Opinion_poll
Net_worth = models.Net_worth

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


def canidateGoogleTrendYTD(canId, session):
    q = session.query(Google_trend.Count,  Google_trend.Week).filter(Google_trend.Candidate_id == canId)
    q = q.order_by((Google_trend.Week.desc()))
    q = q.limit(45)

    parsed = []
    i = 0
    sum = 0
    for count in q.all():
        i += 1
        if count[0] is not None:
            sum += count[0]
        if i == 4:
            parsed.append(sum)
            sum = 0
            i = 0

    return parsed[::-1]


def canidateOpinionPollYTD(canId, session):
    q = session.query(Opinion_poll.Month,  Opinion_poll.Standing, Opinion_poll.Poll_date).filter(Opinion_poll.Can_id == canId)
    q = q.order_by(Opinion_poll.Poll_date)

    parsed = []
    i = 0
    sum = 0

    for count in q.all():
        if count[1] is not None:
            parsed.append(count[1])
        else:
            parsed.append("None")

    return parsed


def candidateName(canId, session):
    q = session.query(Candidate.Fname, Candidate.Lname).filter(Candidate.Candidate_id == canId)
    #get the first entry
    names = q.first()
    #join the first
    return " ".join(names);

def candidateInfo(canId, session):
    q = session.query(Candidate.Fname,
                        Candidate.Lname,
                        Candidate.Party,
                        Candidate.Bdate,
                        Location.City,
                        Location.State,
                        Location.Population,
                        Net_worth.Amount).join(Location).join(Net_worth)


    q = q.filter(Candidate.Candidate_id == canId)
    values = q.first();

    names = ['Fname', 'Lname', 'Party', "Birthday", "City", "State", "Population", "Net Worth"]

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


    retVal = {}
    if(result.rowcount > 0):
        row = result.fetchone();
        retVal = {"Home State" : row["Home State"],
                "Home State Count" : row["Home State Count"],
                "Home State Amount": row["Home State Amount"],
                "Top State" : row["Top State"],
                "Top State Count" : row["Top State Count"],
                "Top State Amount" : row["Top State Amount"]
                }

    return retVal

def TopContribOccupations(canId, session):
    result = session.execute("""
                        SELECT o.*
                        FROM (
                            SELECT a.Candidate_id, Fname, Lname, Donor_occupation, SUM(Amount) as SUM, count(*) as NUM
                            FROM
                            (select * from CAMPAIGN_CONTRIBUTION where Candidate_id = :canId) a
                            JOIN
                            (select * from CANDIDATE where Candidate_id = :canId) b
                            ON a.Candidate_id=b.Candidate_id
                            GROUP BY Candidate_id, Donor_occupation
                        ) AS o
                        LEFT JOIN (
                            SELECT b.Candidate_id, Fname, Lname, Donor_occupation, SUM(Amount) as SUM, count(*) as NUM
                            FROM
                            (select * from CAMPAIGN_CONTRIBUTION where Candidate_id = :canId) a
                            JOIN
                            (select * from CANDIDATE where Candidate_id = :canId) b
                            ON a.Candidate_id=b.Candidate_id
                            GROUP BY Candidate_id, Donor_occupation
                        ) AS b
                        ON (o.Candidate_id=b.candidate_id) AND (o.SUM < b.SUM)
                        WHERE b.SUM is NULL""", {'canId': canId})

    retVal = {}
    if(result.rowcount > 0):
        row = result.fetchone();

        retVal = {
                "Occupation": row["Donor_occupation"],
                "Total Contributers" : row["NUM"],
                "Total Amount" : row["SUM"]
                }

    return retVal
