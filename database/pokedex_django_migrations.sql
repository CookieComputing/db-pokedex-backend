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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-12-13 01:37:50.413766'),(2,'auth','0001_initial','2021-12-13 01:37:51.317857'),(3,'admin','0001_initial','2021-12-13 01:37:51.686922'),(4,'admin','0002_logentry_remove_auto_add','2021-12-13 01:37:51.699252'),(5,'admin','0003_logentry_add_action_flag_choices','2021-12-13 01:37:51.712073'),(6,'contenttypes','0002_remove_content_type_name','2021-12-13 01:37:51.880737'),(7,'auth','0002_alter_permission_name_max_length','2021-12-13 01:37:51.978035'),(8,'auth','0003_alter_user_email_max_length','2021-12-13 01:37:52.020128'),(9,'auth','0004_alter_user_username_opts','2021-12-13 01:37:52.032536'),(10,'auth','0005_alter_user_last_login_null','2021-12-13 01:37:52.108693'),(11,'auth','0006_require_contenttypes_0002','2021-12-13 01:37:52.115033'),(12,'auth','0007_alter_validators_add_error_messages','2021-12-13 01:37:52.130564'),(13,'auth','0008_alter_user_username_max_length','2021-12-13 01:37:52.220166'),(14,'auth','0009_alter_user_last_name_max_length','2021-12-13 01:37:52.321686'),(15,'auth','0010_alter_group_name_max_length','2021-12-13 01:37:52.350767'),(16,'auth','0011_update_proxy_permissions','2021-12-13 01:37:52.365005'),(17,'auth','0012_alter_user_first_name_max_length','2021-12-13 01:37:52.456178'),(18,'pokemon','0001_initial','2021-12-13 01:37:52.808171'),(19,'pokemon','0002_auto_20211125_0003','2021-12-13 01:37:52.824313'),(20,'pokemon','0003_moves','2021-12-13 01:37:52.871293'),(21,'pokemon','0004_alter_moves_element_type','2021-12-13 01:37:52.879453'),(22,'pokemon','0005_gender_region','2021-12-13 01:37:52.942811'),(23,'pokemon','0006_auto_20211202_1627','2021-12-13 01:37:52.985344'),(24,'pokemon','0007_pokemontype_pokemonweakness','2021-12-13 01:37:53.321339'),(25,'pokemon','0008_auto_20211204_1644','2021-12-13 01:37:53.412900'),(26,'pokemon','0009_moveentry','2021-12-13 01:37:53.711879'),(27,'pokemon','0008_delete_pokemonweakness','2021-12-13 01:37:53.738213'),(28,'pokemon','0010_merge_0008_delete_pokemonweakness_0009_moveentry','2021-12-13 01:37:53.743677'),(29,'sessions','0001_initial','2021-12-13 01:37:53.796805'),(30,'trainers','0001_initial','2021-12-13 01:37:53.877778'),(31,'trainers','0002_teams','2021-12-13 01:37:53.984734'),(32,'trainers','0003_pokemon','2021-12-13 01:37:54.179756'),(33,'trainers','0004_rename_pokemoninfo_pokemon_pokemon_info','2021-12-13 01:37:54.298769'),(34,'trainers','0005_alter_trainers_date_of_birth','2021-12-13 01:37:54.307573'),(35,'trainers','0006_pokedex','2021-12-13 01:37:54.424675'),(36,'trainers','0007_auto_20211212_2039','2021-12-13 01:37:54.473839'),(37,'trainers','0008_alter_pokedex_trainer','2021-12-13 01:37:54.690621'),(38,'trainers','0009_pokedexentry','2021-12-13 01:40:09.610212');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
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
