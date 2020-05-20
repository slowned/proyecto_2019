-- MySQL dump 10.13  Distrib 5.7.29, for Linux (x86_64)
--
-- Host: localhost    Database: grupo8
-- ------------------------------------------------------
-- Server version	5.7.29-0ubuntu0.18.04.1

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
-- Table structure for table `attend`
--

DROP TABLE IF EXISTS `attend`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `attend` (
  `has_attended` tinyint(1) DEFAULT NULL,
  `student_id` int(11) NOT NULL,
  `lesson_id` int(11) NOT NULL,
  PRIMARY KEY (`student_id`,`lesson_id`),
  KEY `lesson_id` (`lesson_id`),
  CONSTRAINT `attend_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `students` (`id`),
  CONSTRAINT `attend_ibfk_2` FOREIGN KEY (`lesson_id`) REFERENCES `lesson` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attend`
--

LOCK TABLES `attend` WRITE;
/*!40000 ALTER TABLE `attend` DISABLE KEYS */;
INSERT INTO `attend` VALUES (1,1,1),(0,1,2),(0,1,3),(0,1,4),(0,1,11),(0,1,12),(0,1,13),(0,1,14),(0,1,15),(0,1,16),(0,1,17),(0,1,18),(0,1,19),(0,1,20),(0,1,21),(0,1,22),(0,1,23),(0,1,24),(0,1,25),(0,1,26),(0,2,1),(1,2,2),(0,2,3),(1,2,4);
/*!40000 ALTER TABLE `attend` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `configurations`
--

DROP TABLE IF EXISTS `configurations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `configurations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `active` tinyint(1) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `title` varchar(60) DEFAULT NULL,
  `email` varchar(60) DEFAULT NULL,
  `offset_paginator` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_configurations_title` (`title`),
  KEY `ix_configurations_email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `configurations`
--

LOCK TABLES `configurations` WRITE;
/*!40000 ALTER TABLE `configurations` DISABLE KEYS */;
INSERT INTO `configurations` VALUES (3,1,'Escuela orquesta beriso','Escuela orquesta','escuela@orquesta.mail.com',5);
/*!40000 ALTER TABLE `configurations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `instruments`
--

DROP TABLE IF EXISTS `instruments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `instruments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(60) DEFAULT NULL,
  `type` varchar(60) DEFAULT NULL,
  `inventory_number` varchar(60) DEFAULT NULL,
  `img_path` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `instruments`
--

LOCK TABLES `instruments` WRITE;
/*!40000 ALTER TABLE `instruments` DISABLE KEYS */;
/*!40000 ALTER TABLE `instruments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lesson`
--

DROP TABLE IF EXISTS `lesson`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lesson` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` int(11) DEFAULT NULL,
  `workshop_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `workshop_id` (`workshop_id`),
  CONSTRAINT `lesson_ibfk_1` FOREIGN KEY (`workshop_id`) REFERENCES `workshop` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lesson`
--

LOCK TABLES `lesson` WRITE;
/*!40000 ALTER TABLE `lesson` DISABLE KEYS */;
INSERT INTO `lesson` VALUES (1,1,1),(2,2,1),(3,3,1),(4,4,1),(5,1,2),(6,2,2),(7,3,2),(8,4,2),(9,5,2),(10,6,2),(11,1,3),(12,2,3),(13,3,3),(14,4,3),(15,5,3),(16,6,3),(17,7,3),(18,8,3),(19,9,3),(20,10,3),(21,11,3),(22,12,3),(23,13,3),(24,14,3),(25,15,3),(26,16,3),(27,1,4),(28,2,4),(29,3,4),(30,4,4),(31,5,4),(32,6,4),(33,7,4),(34,8,4),(35,9,4),(36,10,4),(37,11,4),(38,12,4),(39,13,4);
/*!40000 ALTER TABLE `lesson` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `level`
--

DROP TABLE IF EXISTS `level`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `level` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `level`
--

LOCK TABLES `level` WRITE;
/*!40000 ALTER TABLE `level` DISABLE KEYS */;
INSERT INTO `level` VALUES (13,'1'),(22,'10'),(23,'11'),(14,'2'),(15,'3'),(16,'4'),(17,'5'),(18,'6'),(19,'7'),(20,'8'),(21,'9');
/*!40000 ALTER TABLE `level` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `neighborhood`
--

DROP TABLE IF EXISTS `neighborhood`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `neighborhood` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `neighborhood`
--

LOCK TABLES `neighborhood` WRITE;
/*!40000 ALTER TABLE `neighborhood` DISABLE KEYS */;
INSERT INTO `neighborhood` VALUES (5,'Barrio Bco. Pcia.'),(6,'Barrio J.B. Justo'),(1,'Barrio Náutico'),(2,'Barrio Obrero'),(4,'Barrio Solidaridad'),(3,'Berisso'),(7,'El Carmen'),(8,'El Labrador'),(9,'Ensenada'),(10,'La Hermosura'),(11,'La PLata'),(12,'Los Talas'),(13,'Ringuelet'),(14,'Tolosa'),(15,'Villa Alba'),(16,'Villa Arguello'),(17,'Villa B. C'),(18,'Villa Elvira'),(19,'Villa Nueva'),(20,'Villa Paula'),(21,'Villa Progreso'),(22,'Villa San Carlos'),(23,'Villa Zula');
/*!40000 ALTER TABLE `neighborhood` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nucleos`
--

DROP TABLE IF EXISTS `nucleos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `nucleos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(60) DEFAULT NULL,
  `longitud` float DEFAULT NULL,
  `latitude` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nucleos`
--

LOCK TABLES `nucleos` WRITE;
/*!40000 ALTER TABLE `nucleos` DISABLE KEYS */;
INSERT INTO `nucleos` VALUES (1,'Nucleo Berisso',-34.9228,-57.986),(2,'Nucleo Centro',-34.8976,-57.9653),(3,'Nucleo Numero 1',-34.911,-57.9548),(4,'Nucleo Numero 2',-34.9316,-57.9341);
/*!40000 ALTER TABLE `nucleos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(60) NOT NULL,
  `permisos` varchar(60000) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'docente','students_index,students_update,students_show,teachers_index,teachers_show,administration_index,administration_show'),(2,'administrador','students_index,students_new,students_destroy,students_update,students_show,user_index,user_new,user_destroy,user_update,user_show,teachers_index,teachers_new,teachers_destroy,teachers_update,teachers_show,configurations_index,configurations_new,configurations_destroy,configurations_update,configurations_show,administration_index,administration_new,administration_destroy,administration_update,administration_show'),(3,'preceptor','students_index,students_update,students_show');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `school`
--

DROP TABLE IF EXISTS `school`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `school` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(60) NOT NULL,
  `address` varchar(100) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `school`
--

LOCK TABLES `school` WRITE;
/*!40000 ALTER TABLE `school` DISABLE KEYS */;
INSERT INTO `school` VALUES (1,'Nacional','Calle 123','123123'),(2,'Albert Thomas','Calle 123','123123'),(3,'Normal','Calle 123','123123'),(4,'Escuela 7','Calle 123','123123'),(5,'Escuela 501','Calle 123','123123');
/*!40000 ALTER TABLE `school` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `school_year`
--

DROP TABLE IF EXISTS `school_year`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `school_year` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `semesters` varchar(255) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `start_date` (`start_date`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `school_year`
--

LOCK TABLES `school_year` WRITE;
/*!40000 ALTER TABLE `school_year` DISABLE KEYS */;
INSERT INTO `school_year` VALUES (1,'2020-06-11','2020-08-01','1',1),(2,'2020-03-11','2020-12-18','2',1),(3,'2019-10-01','2020-03-12','1',1);
/*!40000 ALTER TABLE `school_year` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `students` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `surname` varchar(60) DEFAULT NULL,
  `name` varchar(60) DEFAULT NULL,
  `birth_date` date DEFAULT NULL,
  `borned` varchar(60) DEFAULT NULL,
  `locality` varchar(60) DEFAULT NULL,
  `address` varchar(60) DEFAULT NULL,
  `gender` varchar(255) DEFAULT NULL,
  `document_type` varchar(60) DEFAULT NULL,
  `document_number` varchar(60) DEFAULT NULL,
  `tutor` varchar(60) DEFAULT NULL,
  `phone` varchar(60) DEFAULT NULL,
  `tutor_name` varchar(60) DEFAULT NULL,
  `level_id` int(11) NOT NULL,
  `school_id` int(11) NOT NULL,
  `neighborhood_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `level_id` (`level_id`),
  KEY `school_id` (`school_id`),
  KEY `neighborhood_id` (`neighborhood_id`),
  CONSTRAINT `students_ibfk_1` FOREIGN KEY (`level_id`) REFERENCES `level` (`id`),
  CONSTRAINT `students_ibfk_2` FOREIGN KEY (`school_id`) REFERENCES `school` (`id`),
  CONSTRAINT `students_ibfk_3` FOREIGN KEY (`neighborhood_id`) REFERENCES `neighborhood` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES (1,'Garcia','Carlos','2020-02-10','la Balandra','General San Martín','Calle falsa 123','male','DNI','12345678','Madre','23','Stella',13,1,10),(2,'shhsh','dgssg','2019-09-25','sgsgs ','Azul','gsfg sg451651','female','Pasaporte','2165165','Padre','65161565516','Victor',19,1,9);
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teachers`
--

DROP TABLE IF EXISTS `teachers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `teachers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `surname` varchar(60) DEFAULT NULL,
  `name` varchar(60) DEFAULT NULL,
  `birth_date` date DEFAULT NULL,
  `locality` varchar(60) DEFAULT NULL,
  `address` varchar(60) DEFAULT NULL,
  `document_type` varchar(60) DEFAULT NULL,
  `document_number` varchar(60) DEFAULT NULL,
  `phone` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teachers`
--

LOCK TABLES `teachers` WRITE;
/*!40000 ALTER TABLE `teachers` DISABLE KEYS */;
INSERT INTO `teachers` VALUES (1,'Sanchez','Marta','2020-02-03','General Rodríguez','ssadsd 351365','DNI','12345678','6856165151'),(2,'Suarez','Adolfo','1970-02-11','Lobos','aosfaf 651651','Pasaporte','654165','516516815');
/*!40000 ALTER TABLE `teachers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_roles`
--

DROP TABLE IF EXISTS `user_roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `user_roles_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  CONSTRAINT `user_roles_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_roles`
--

LOCK TABLES `user_roles` WRITE;
/*!40000 ALTER TABLE `user_roles` DISABLE KEYS */;
INSERT INTO `user_roles` VALUES (1,1,2),(2,2,2);
/*!40000 ALTER TABLE `user_roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `created_at` date DEFAULT NULL,
  `updated_at` date DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `is_admin` tinyint(1) DEFAULT NULL,
  `username` varchar(60) NOT NULL,
  `email` varchar(60) NOT NULL,
  `name` varchar(60) DEFAULT NULL,
  `surname` varchar(60) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `password_hash` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('2020-02-14',NULL,1,0,'superadmin','admin@admin.com',NULL,NULL,1,'pbkdf2:sha256:150000$H53M4BjI$c5db00a04f43c9ca8582e929f46c393e26f53a6e750da66f8cf667491595d098'),('2020-02-14','2020-02-14',2,0,'mmo','usu4edit@mail.com','OtroUser','ApOtroUser',0,'pbkdf2:sha256:150000$s7o2eFap$f3ffef75c652e1993c28d7d23af3f0ac4d79cb73d72be448580eb74aee367330');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `workshop`
--

DROP TABLE IF EXISTS `workshop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `workshop` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(120) DEFAULT NULL,
  `short_name` varchar(60) DEFAULT NULL,
  `semester_id` int(11) NOT NULL,
  `teacher_id` int(11) DEFAULT NULL,
  `cant_lessons` int(11) DEFAULT NULL,
  `nucleo` varchar(120) DEFAULT NULL,
  `address` varchar(214) DEFAULT NULL,
  `days` varchar(520) DEFAULT NULL,
  `horario` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `semester_id` (`semester_id`),
  KEY `teacher_id` (`teacher_id`),
  CONSTRAINT `workshop_ibfk_1` FOREIGN KEY (`semester_id`) REFERENCES `school_year` (`id`),
  CONSTRAINT `workshop_ibfk_2` FOREIGN KEY (`teacher_id`) REFERENCES `teachers` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `workshop`
--

LOCK TABLES `workshop` WRITE;
/*!40000 ALTER TABLE `workshop` DISABLE KEYS */;
INSERT INTO `workshop` VALUES (1,'piano','Pi',1,2,3,'Barrio Náutico','Calle falsa 123','Calle falsa 123','10:00'),(2,'piano','pi2',1,2,5,'Barrio Náutico','Calle falsa 123','Calle falsa 123','18:00'),(3,'bateria','bt',2,1,15,'Villa Progreso','cal 9859','cal 9859','11:00'),(4,'trompeta','t1',2,2,12,'Barrio J.B. Justo','sadfaffa','sadfaffa','16:00');
/*!40000 ALTER TABLE `workshop` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `workshop_students`
--

DROP TABLE IF EXISTS `workshop_students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `workshop_students` (
  `workshop_id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  PRIMARY KEY (`workshop_id`,`student_id`),
  KEY `student_id` (`student_id`),
  CONSTRAINT `workshop_students_ibfk_1` FOREIGN KEY (`workshop_id`) REFERENCES `workshop` (`id`),
  CONSTRAINT `workshop_students_ibfk_2` FOREIGN KEY (`student_id`) REFERENCES `students` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `workshop_students`
--

LOCK TABLES `workshop_students` WRITE;
/*!40000 ALTER TABLE `workshop_students` DISABLE KEYS */;
INSERT INTO `workshop_students` VALUES (1,1),(3,1),(1,2);
/*!40000 ALTER TABLE `workshop_students` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-02-14  3:25:10
