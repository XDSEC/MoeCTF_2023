-- MySQL dump 10.13  Distrib 8.0.24, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: messageboard
-- ------------------------------------------------------
-- Server version	8.0.24

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `flag`
--
CREATE Database messageboard;
USE messageboard;
DROP TABLE IF EXISTS `flag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flag` (
  `flag` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flag`
--

LOCK TABLES `flag` WRITE;
/*!40000 ALTER TABLE `flag` DISABLE KEYS */;
INSERT INTO `flag` VALUES ('-Are-YOu-myS0L-MasT3r?-');
/*!40000 ALTER TABLE `flag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `message` (
  `username` char(16) COLLATE utf8mb4_general_ci NOT NULL,
  `data` text COLLATE utf8mb4_general_ci NOT NULL,
  `time` char(30) COLLATE utf8mb4_general_ci NOT NULL,
  `private` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES ('admin','You can\'t see it!','2023-7-20 15:58:59.655194',1),('admin','记录一下搭建留言板的过程\r\n首先确定好web框架，笔者选择使用简单的flask框架。\r\n然后使用强且随机的字符串作为session的密钥。\r\napp.secret_key = \"This-random-secretKey-you-can\'t-get\" + os.urandom(2).hex()\r\n最后再写一下路由和数据库处理的函数就完成啦！！\r\n身为web手的我为了保护好服务器，写代码的时候十分谨慎，一定不会让有心人有可乘之机！','2023-08-01 19:22:07.274353',0),('admin','今天测试留言板的时候发现我的调试模式给出的pin码一直是128-243-397不变，真是奇怪呢\r\n不过这个泄露了貌似很危险，别人就可以进我的console执行任意python代码了！\r\n一定不能泄露出去！！！！','2023-08-02 09:43:45.168971',1),('admin','欢迎来到xlccccc的留言板！\r\n你可以在这里畅所欲言，但请不要攻击我，好吗QAQ','2023-08-02 14:21:50.358262',0),('admin','（题外话）\r\n1.本比赛对于校外选手无任何性质的奖励，竞争是不存在的，所以请不要主动破坏环境\r\n2.本题的web页面设置为留言板形式是希望让各位选手做题的时候能有互动感，我完全可以以单纯的文字形式，但我并没有这样做\r\n3.题目环境改为每隔一个小时重置，若时间太短可找我要docker容器本地尝试\r\n4.如果还是屡屡出现完全恶意的破坏题目环境的现象，会考虑下线此题目，只面向校内选手\r\n5.本题不需要扫描web目录，也不需要爆破密码','2023-08-02 17:22:50.358262',0);
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL,
  `username` char(16) COLLATE utf8mb4_general_ci NOT NULL,
  `password` char(16) COLLATE utf8mb4_general_ci NOT NULL,
  `power` char(10) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (0,'admin','SecurityP@sSw0Rd','root');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-02 15:27:58
