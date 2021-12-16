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
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add pokemon info',1,'add_pokemoninfo'),(2,'Can change pokemon info',1,'change_pokemoninfo'),(3,'Can delete pokemon info',1,'delete_pokemoninfo'),(4,'Can view pokemon info',1,'view_pokemoninfo'),(5,'Can add moves',2,'add_moves'),(6,'Can change moves',2,'change_moves'),(7,'Can delete moves',2,'delete_moves'),(8,'Can view moves',2,'view_moves'),(9,'Can add pokemon type',3,'add_pokemontype'),(10,'Can change pokemon type',3,'change_pokemontype'),(11,'Can delete pokemon type',3,'delete_pokemontype'),(12,'Can view pokemon type',3,'view_pokemontype'),(13,'Can add move entry',4,'add_moveentry'),(14,'Can change move entry',4,'change_moveentry'),(15,'Can delete move entry',4,'delete_moveentry'),(16,'Can view move entry',4,'view_moveentry'),(17,'Can add trainers',5,'add_trainers'),(18,'Can change trainers',5,'change_trainers'),(19,'Can delete trainers',5,'delete_trainers'),(20,'Can view trainers',5,'view_trainers'),(21,'Can add teams',6,'add_teams'),(22,'Can change teams',6,'change_teams'),(23,'Can delete teams',6,'delete_teams'),(24,'Can view teams',6,'view_teams'),(25,'Can add pokemon',7,'add_pokemon'),(26,'Can change pokemon',7,'change_pokemon'),(27,'Can delete pokemon',7,'delete_pokemon'),(28,'Can view pokemon',7,'view_pokemon'),(29,'Can add pokedex',8,'add_pokedex'),(30,'Can change pokedex',8,'change_pokedex'),(31,'Can delete pokedex',8,'delete_pokedex'),(32,'Can view pokedex',8,'view_pokedex'),(33,'Can add pokedex entry',9,'add_pokedexentry'),(34,'Can change pokedex entry',9,'change_pokedexentry'),(35,'Can delete pokedex entry',9,'delete_pokedexentry'),(36,'Can view pokedex entry',9,'view_pokedexentry'),(37,'Can add log entry',10,'add_logentry'),(38,'Can change log entry',10,'change_logentry'),(39,'Can delete log entry',10,'delete_logentry'),(40,'Can view log entry',10,'view_logentry'),(41,'Can add permission',11,'add_permission'),(42,'Can change permission',11,'change_permission'),(43,'Can delete permission',11,'delete_permission'),(44,'Can view permission',11,'view_permission'),(45,'Can add group',12,'add_group'),(46,'Can change group',12,'change_group'),(47,'Can delete group',12,'delete_group'),(48,'Can view group',12,'view_group'),(49,'Can add user',13,'add_user'),(50,'Can change user',13,'change_user'),(51,'Can delete user',13,'delete_user'),(52,'Can view user',13,'view_user'),(53,'Can add content type',14,'add_contenttype'),(54,'Can change content type',14,'change_contenttype'),(55,'Can delete content type',14,'delete_contenttype'),(56,'Can view content type',14,'view_contenttype'),(57,'Can add session',15,'add_session'),(58,'Can change session',15,'change_session'),(59,'Can delete session',15,'delete_session'),(60,'Can view session',15,'view_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-16 14:22:34
