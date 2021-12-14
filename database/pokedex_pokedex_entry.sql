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
-- Table structure for table `pokedex_entry`
--

DROP TABLE IF EXISTS `pokedex_entry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pokedex_entry` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `pokedex_id` bigint NOT NULL,
  `pokemon_info_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `pokedex_entry_pokedex_id_pokemon_info_id_8f3a494c_uniq` (`pokedex_id`,`pokemon_info_id`),
  KEY `pokedex_entry_pokemon_info_id_564cabb6_fk_pokemon_i` (`pokemon_info_id`),
  CONSTRAINT `pokedex_entry_pokedex_id_2ff68a5d_fk_pokedex_id` FOREIGN KEY (`pokedex_id`) REFERENCES `pokedex` (`id`),
  CONSTRAINT `pokedex_entry_pokemon_info_id_564cabb6_fk_pokemon_i` FOREIGN KEY (`pokemon_info_id`) REFERENCES `pokemon_info` (`national_num`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pokedex_entry`
--

LOCK TABLES `pokedex_entry` WRITE;
/*!40000 ALTER TABLE `pokedex_entry` DISABLE KEYS */;
INSERT INTO `pokedex_entry` VALUES (3,1,25),(4,1,74),(5,2,74),(2,3,26),(1,3,172);
/*!40000 ALTER TABLE `pokedex_entry` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-13 21:30:14
