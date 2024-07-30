-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.32-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.4.0.6659
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para mov_dobot
CREATE DATABASE IF NOT EXISTS `mov_dobot` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
USE `mov_dobot`;

-- Volcando estructura para tabla mov_dobot.c_directa
CREATE TABLE IF NOT EXISTS `c_directa` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `joint_1` float NOT NULL,
  `joint_2` float NOT NULL,
  `joint_3` float NOT NULL,
  `joint_4` float NOT NULL,
  `timestamp` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla mov_dobot.c_directa: ~0 rows (aproximadamente)

-- Volcando estructura para tabla mov_dobot.c_inversa
CREATE TABLE IF NOT EXISTS `c_inversa` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `coord_x` float NOT NULL,
  `coord_y` float NOT NULL,
  `coord_z` float NOT NULL,
  `roll` float NOT NULL,
  `timestamp` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla mov_dobot.c_inversa: ~0 rows (aproximadamente)

-- Volcando estructura para tabla mov_dobot.movimientos_personalizados
CREATE TABLE IF NOT EXISTS `movimientos_personalizados` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `movimiento` varchar(10) NOT NULL,
  `timestamp` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla mov_dobot.movimientos_personalizados: ~0 rows (aproximadamente)

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
