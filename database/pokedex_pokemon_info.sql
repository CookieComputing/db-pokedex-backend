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
  `name` varchar(45) NOT NULL,
  `photo_url` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `devolved_state_pkid` int DEFAULT NULL,
  `evolved_state_pkid` int DEFAULT NULL,
  PRIMARY KEY (`national_num`),
  KEY `pokemon_info_devolved_state_pkid_87bdfbdb_fk_pokemon_i` (`devolved_state_pkid`),
  KEY `pokemon_info_evolved_state_pkid_fd87168f_fk_pokemon_i` (`evolved_state_pkid`),
  CONSTRAINT `pokemon_info_devolved_state_pkid_87bdfbdb_fk_pokemon_i` FOREIGN KEY (`devolved_state_pkid`) REFERENCES `pokemon_info` (`national_num`),
  CONSTRAINT `pokemon_info_evolved_state_pkid_fd87168f_fk_pokemon_i` FOREIGN KEY (`evolved_state_pkid`) REFERENCES `pokemon_info` (`national_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pokemon_info`
--

LOCK TABLES `pokemon_info` WRITE;
/*!40000 ALTER TABLE `pokemon_info` DISABLE KEYS */;
INSERT INTO `pokemon_info` VALUES (25,'Pikachu','https://assets.pokemon.com/assets/cms2/img/pokedex/full/025.png','Pikachu that can generate powerful electricity have cheek sacs that are extra soft and super stretchy.',172,26),(26,'Raichu','https://assets.pokemon.com/assets/cms2/img/pokedex/full/026.png','Its long tail serves as a ground to protect itself from its own high-voltage power.',25,NULL),(74,'geodude','https://assets.pokemon.com/assets/cms2/img/pokedex/full/074.png','Commonly found near mountain trails and the like. If you step on one by accident, it gets angry.',NULL,NULL),(172,'Pichu','https://assets.pokemon.com/assets/cms2/img/pokedex/full/172.png','Despite its small size, it can zap even adult humans. However, if it does so, it also surprises itself.',NULL,25);
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

-- Dump completed on 2021-12-13 21:30:12
