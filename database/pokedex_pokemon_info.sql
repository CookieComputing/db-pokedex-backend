-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: pokedex
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `pokemon_info`
--

DROP TABLE IF EXISTS `pokemon_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pokemon_info` (
  `national_num` int NOT NULL,
  `evolved_state_pkid` int DEFAULT NULL,
  `devolved_state_pkid` int DEFAULT NULL,
  `pokemon_id` int DEFAULT NULL,
  `name` varchar(45) NOT NULL,
  `photo_url` varchar(255) NOT NULL,
  `description` varchar(45) NOT NULL,
  PRIMARY KEY (`national_num`),
  KEY `pokemon_idx` (`pokemon_id`),
  KEY `devolved_state_idx` (`devolved_state_pkid`),
  KEY `evolved_state_idx` (`evolved_state_pkid`),
  CONSTRAINT `devolved_state` FOREIGN KEY (`devolved_state_pkid`) REFERENCES `pokemon_info` (`national_num`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `evolved_state` FOREIGN KEY (`evolved_state_pkid`) REFERENCES `pokemon_info` (`national_num`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pokemon_info`
--

LOCK TABLES `pokemon_info` WRITE;
/*!40000 ALTER TABLE `pokemon_info` DISABLE KEYS */;
/*!40000 ALTER TABLE `pokemon_info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-15  8:45:11
