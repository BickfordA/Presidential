-- MySQL dump 10.13  Distrib 5.5.46, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: PRESIDENTIAL
-- ------------------------------------------------------
-- Server version	5.5.46-0ubuntu0.12.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `CAMPAIGN_CONTRIBUTION`
--

DROP TABLE IF EXISTS `CAMPAIGN_CONTRIBUTION`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CAMPAIGN_CONTRIBUTION` (
  `Transaction_id` int(11) NOT NULL,
  `Candidate_id` smallint(6) NOT NULL,
  `Donor` varchar(25) DEFAULT NULL,
  `State` char(2) CHARACTER SET latin1 DEFAULT NULL,
  `Recipient` varchar(25) DEFAULT NULL,
  `Amount` int(11) DEFAULT NULL,
  `Donor_occupation` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`Transaction_id`),
  UNIQUE KEY `Transaction_id_UNIQUE` (`Transaction_id`),
  KEY `Candidate_idx` (`Candidate_id`),
  CONSTRAINT `CandidateCamp` FOREIGN KEY (`Candidate_id`) REFERENCES `CANDIDATE` (`Candidate_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CAMPAIGN_CONTRIBUTION`
--

LOCK TABLES `CAMPAIGN_CONTRIBUTION` WRITE;
/*!40000 ALTER TABLE `CAMPAIGN_CONTRIBUTION` DISABLE KEYS */;
/*!40000 ALTER TABLE `CAMPAIGN_CONTRIBUTION` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CANDIDATE`
--

DROP TABLE IF EXISTS `CANDIDATE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CANDIDATE` (
  `Candidate_id` smallint(6) NOT NULL,
  `Fname` varchar(15) DEFAULT NULL,
  `Lname` varchar(20) DEFAULT NULL,
  `Bdate` date DEFAULT NULL,
  `Party` varchar(15) NOT NULL,
  `Twitter_id` varchar(15) NOT NULL,
  `Hometown` char(3) DEFAULT NULL,
  PRIMARY KEY (`Candidate_id`),
  UNIQUE KEY `candidate_id_UNIQUE` (`Candidate_id`),
  UNIQUE KEY `Twitter_id_UNIQUE` (`Twitter_id`),
  KEY `Hometown_idx` (`Hometown`),
  CONSTRAINT `Hometown` FOREIGN KEY (`Hometown`) REFERENCES `LOCATION` (`Location_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CANDIDATE`
--

LOCK TABLES `CANDIDATE` WRITE;
/*!40000 ALTER TABLE `CANDIDATE` DISABLE KEYS */;
/*!40000 ALTER TABLE `CANDIDATE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DEBATE`
--

DROP TABLE IF EXISTS `DEBATE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DEBATE` (
  `Debate_id` int(11) NOT NULL,
  `Type` varchar(15) DEFAULT NULL,
  `Party` varchar(20) DEFAULT NULL,
  `Debate_date` date DEFAULT NULL,
  PRIMARY KEY (`Debate_id`),
  UNIQUE KEY `Debate_id_UNIQUE` (`Debate_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DEBATE`
--

LOCK TABLES `DEBATE` WRITE;
/*!40000 ALTER TABLE `DEBATE` DISABLE KEYS */;
/*!40000 ALTER TABLE `DEBATE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DEBATE_PARTICIPANT`
--

DROP TABLE IF EXISTS `DEBATE_PARTICIPANT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DEBATE_PARTICIPANT` (
  `Debate_id` int(11) NOT NULL,
  `Candidate_id` smallint(6) NOT NULL,
  PRIMARY KEY (`Debate_id`,`Candidate_id`),
  KEY `Candidate_idx` (`Candidate_id`),
  CONSTRAINT `Debate` FOREIGN KEY (`Debate_id`) REFERENCES `DEBATE` (`Debate_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `CandidateDebate` FOREIGN KEY (`Candidate_id`) REFERENCES `CANDIDATE` (`Candidate_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DEBATE_PARTICIPANT`
--

LOCK TABLES `DEBATE_PARTICIPANT` WRITE;
/*!40000 ALTER TABLE `DEBATE_PARTICIPANT` DISABLE KEYS */;
/*!40000 ALTER TABLE `DEBATE_PARTICIPANT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ELECTION`
--

DROP TABLE IF EXISTS `ELECTION`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ELECTION` (
  `Election_id` int(11) NOT NULL,
  `Level` varchar(20) DEFAULT NULL,
  `Party` varchar(20) DEFAULT NULL,
  `State` char(2) CHARACTER SET latin1 DEFAULT NULL,
  `Date` date DEFAULT NULL,
  PRIMARY KEY (`Election_id`),
  UNIQUE KEY `Election_id_UNIQUE` (`Election_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ELECTION`
--

LOCK TABLES `ELECTION` WRITE;
/*!40000 ALTER TABLE `ELECTION` DISABLE KEYS */;
/*!40000 ALTER TABLE `ELECTION` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ELECTION_RESULTS`
--

DROP TABLE IF EXISTS `ELECTION_RESULTS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ELECTION_RESULTS` (
  `Election_id` int(11) NOT NULL,
  `Candidate_id` smallint(6) NOT NULL,
  `Percent_pop_vote` int(11) DEFAULT NULL,
  `Electoral_count` int(11) DEFAULT NULL,
  PRIMARY KEY (`Election_id`,`Candidate_id`),
  KEY `Candidate_idx` (`Candidate_id`),
  CONSTRAINT `Election` FOREIGN KEY (`Election_id`) REFERENCES `ELECTION` (`Election_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `CandidateElect` FOREIGN KEY (`Candidate_id`) REFERENCES `CANDIDATE` (`Candidate_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ELECTION_RESULTS`
--

LOCK TABLES `ELECTION_RESULTS` WRITE;
/*!40000 ALTER TABLE `ELECTION_RESULTS` DISABLE KEYS */;
/*!40000 ALTER TABLE `ELECTION_RESULTS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `GOOGLE_TREND`
--

DROP TABLE IF EXISTS `GOOGLE_TREND`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `GOOGLE_TREND` (
  `Candidate_id` smallint(6) NOT NULL,
  `Month` char(3) CHARACTER SET latin1 NOT NULL,
  `Count` int(11) DEFAULT NULL,
  PRIMARY KEY (`Candidate_id`,`Month`),
  CONSTRAINT `CandidateGoogle` FOREIGN KEY (`Candidate_id`) REFERENCES `CANDIDATE` (`Candidate_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `GOOGLE_TREND`
--

LOCK TABLES `GOOGLE_TREND` WRITE;
/*!40000 ALTER TABLE `GOOGLE_TREND` DISABLE KEYS */;
/*!40000 ALTER TABLE `GOOGLE_TREND` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LOCATION`
--

DROP TABLE IF EXISTS `LOCATION`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `LOCATION` (
  `Location_id` char(3) NOT NULL,
  `City` varchar(20) DEFAULT NULL,
  `State` char(2) CHARACTER SET latin1 DEFAULT NULL,
  `Zip` int(5) DEFAULT NULL,
  `Population` int(11) DEFAULT NULL,
  PRIMARY KEY (`Location_id`),
  UNIQUE KEY `Location_id_UNIQUE` (`Location_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LOCATION`
--

LOCK TABLES `LOCATION` WRITE;
/*!40000 ALTER TABLE `LOCATION` DISABLE KEYS */;
/*!40000 ALTER TABLE `LOCATION` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `NET_WORTH`
--

DROP TABLE IF EXISTS `NET_WORTH`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `NET_WORTH` (
  `Candidate_id` smallint(6) NOT NULL,
  `Year` int(11) NOT NULL,
  `Amount` int(11) DEFAULT NULL,
  PRIMARY KEY (`Candidate_id`,`Year`),
  CONSTRAINT `CandidateNet` FOREIGN KEY (`Candidate_id`) REFERENCES `CANDIDATE` (`Candidate_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `NET_WORTH`
--

LOCK TABLES `NET_WORTH` WRITE;
/*!40000 ALTER TABLE `NET_WORTH` DISABLE KEYS */;
/*!40000 ALTER TABLE `NET_WORTH` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `OPINION_POLL`
--

DROP TABLE IF EXISTS `OPINION_POLL`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `OPINION_POLL` (
  `Poll_date` date NOT NULL,
  `Source` varchar(20) NOT NULL,
  `Can_id` smallint(6) NOT NULL,
  `Standing` int(11) DEFAULT NULL,
  PRIMARY KEY (`Poll_date`,`Source`,`Can_id`),
  KEY `Can_idx` (`Can_id`),
  CONSTRAINT `CandidateOpinion` FOREIGN KEY (`Can_id`) REFERENCES `CANDIDATE` (`Candidate_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `OPINION_POLL`
--

LOCK TABLES `OPINION_POLL` WRITE;
/*!40000 ALTER TABLE `OPINION_POLL` DISABLE KEYS */;
/*!40000 ALTER TABLE `OPINION_POLL` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SEARCH_MENTION`
--

DROP TABLE IF EXISTS `SEARCH_MENTION`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SEARCH_MENTION` (
  `Search_id` int(11) NOT NULL,
  `User_mention` varchar(45) NOT NULL,
  PRIMARY KEY (`Search_id`,`User_mention`),
  CONSTRAINT `Search_IDMention` FOREIGN KEY (`Search_id`) REFERENCES `TWITTER_SEARCH` (`Search_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SEARCH_MENTION`
--

LOCK TABLES `SEARCH_MENTION` WRITE;
/*!40000 ALTER TABLE `SEARCH_MENTION` DISABLE KEYS */;
/*!40000 ALTER TABLE `SEARCH_MENTION` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SEARCH_TAG`
--

DROP TABLE IF EXISTS `SEARCH_TAG`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SEARCH_TAG` (
  `Search_id` int(11) NOT NULL,
  `Hashtag` varchar(45) NOT NULL,
  PRIMARY KEY (`Search_id`,`Hashtag`),
  CONSTRAINT `Search_IDTag` FOREIGN KEY (`Search_id`) REFERENCES `TWITTER_SEARCH` (`Search_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SEARCH_TAG`
--

LOCK TABLES `SEARCH_TAG` WRITE;
/*!40000 ALTER TABLE `SEARCH_TAG` DISABLE KEYS */;
/*!40000 ALTER TABLE `SEARCH_TAG` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TWITTER_SEARCH`
--

DROP TABLE IF EXISTS `TWITTER_SEARCH`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TWITTER_SEARCH` (
  `Search_id` int(11) NOT NULL,
  `Twitter_id` varchar(15) NOT NULL,
  `Time` timestamp NULL DEFAULT NULL,
  `Text` varchar(45) DEFAULT NULL,
  `Retweets` int(11) DEFAULT NULL,
  PRIMARY KEY (`Search_id`),
  UNIQUE KEY `Twitter_id_UNIQUE` (`Search_id`),
  KEY `Twitter_id_idx` (`Twitter_id`),
  CONSTRAINT `Twitter_id` FOREIGN KEY (`Twitter_id`) REFERENCES `CANDIDATE` (`Twitter_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TWITTER_SEARCH`
--

LOCK TABLES `TWITTER_SEARCH` WRITE;
/*!40000 ALTER TABLE `TWITTER_SEARCH` DISABLE KEYS */;
/*!40000 ALTER TABLE `TWITTER_SEARCH` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-11-16  0:06:05


