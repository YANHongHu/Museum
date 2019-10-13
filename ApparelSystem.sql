-- MySQL dump 10.13  Distrib 5.7.21, for Win64 (x86_64)
--
-- Host: localhost    Database: db_apparelsystem
-- ------------------------------------------------------
-- Server version	5.7.21-log

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
-- Current Database: `db_apparelsystem`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `db_apparelsystem` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `db_apparelsystem`;

--
-- Table structure for table `costume_sort`
--

DROP TABLE IF EXISTS `costume_sort`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `costume_sort` (
  `CSid` int(10) NOT NULL COMMENT '服饰类别id',
  `clothes` varchar(50) DEFAULT NULL COMMENT '服装',
  `makeup` varchar(50) DEFAULT NULL COMMENT '妆容',
  `baldric` varchar(50) DEFAULT NULL COMMENT '佩饰',
  PRIMARY KEY (`CSid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `costume_sort`
--

LOCK TABLES `costume_sort` WRITE;
/*!40000 ALTER TABLE `costume_sort` DISABLE KEYS */;
/*!40000 ALTER TABLE `costume_sort` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `costume_trait`
--

DROP TABLE IF EXISTS `costume_trait`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `costume_trait` (
  `CTid` int(10) NOT NULL COMMENT '服饰特征id',
  `dynasty` varchar(50) DEFAULT NULL COMMENT '朝代',
  `sex` varchar(50) DEFAULT NULL COMMENT '性别',
  `texture` varchar(50) DEFAULT NULL COMMENT '材质',
  `color` varchar(50) DEFAULT NULL COMMENT '色彩',
  `streak` varchar(50) DEFAULT NULL COMMENT '纹样',
  `descri` varchar(50) DEFAULT NULL COMMENT '描述',
  `CS_id` int(10) DEFAULT NULL COMMENT '外建 CSid',
  PRIMARY KEY (`CTid`),
  KEY `CS_id` (`CS_id`),
  CONSTRAINT `CS_id` FOREIGN KEY (`CS_id`) REFERENCES `costume_sort` (`CSid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `costume_trait`
--

LOCK TABLES `costume_trait` WRITE;
/*!40000 ALTER TABLE `costume_trait` DISABLE KEYS */;
/*!40000 ALTER TABLE `costume_trait` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `media`
--

DROP TABLE IF EXISTS `media`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `media` (
  `Mid` int(10) NOT NULL AUTO_INCREMENT COMMENT '多媒体id',
  `WordDescri` varchar(50) NOT NULL COMMENT '文字描述',
  `path` varchar(50) NOT NULL COMMENT '存放路径',
  `filename` varchar(50) NOT NULL COMMENT '文件名',
  PRIMARY KEY (`Mid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `media`
--

LOCK TABLES `media` WRITE;
/*!40000 ALTER TABLE `media` DISABLE KEYS */;
/*!40000 ALTER TABLE `media` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mediasort`
--

DROP TABLE IF EXISTS `mediasort`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mediasort` (
  `MSid` int(10) NOT NULL AUTO_INCREMENT COMMENT '多媒体类别id',
  `picture` varchar(100) DEFAULT NULL COMMENT '图片',
  `video` varchar(100) DEFAULT NULL COMMENT '视频',
  `voice` varchar(100) DEFAULT NULL COMMENT '音频',
  `AR` varchar(100) DEFAULT NULL,
  `VR` varchar(100) DEFAULT NULL,
  `Game` varchar(100) DEFAULT NULL,
  `M_id` int(10) DEFAULT NULL COMMENT '外键Mid',
  PRIMARY KEY (`MSid`),
  KEY `M_id` (`M_id`),
  CONSTRAINT `M_id` FOREIGN KEY (`M_id`) REFERENCES `media` (`Mid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mediasort`
--

LOCK TABLES `mediasort` WRITE;
/*!40000 ALTER TABLE `mediasort` DISABLE KEYS */;
/*!40000 ALTER TABLE `mediasort` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-15 17:24:56
