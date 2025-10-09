-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 08-10-2025 a las 19:40:43
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bd_coches`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `camiones`
--

CREATE TABLE `camiones` (
  `Placa` int(11) NOT NULL,
  `ejes` int(3) NOT NULL,
  `capacidad_carga` int(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `camiones`
--

INSERT INTO `camiones` (`Placa`, `ejes`, `capacidad_carga`) VALUES
(3, 8, 2500),
(4, 6, 2000);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `camionetas`
--

CREATE TABLE `camionetas` (
  `Placa` int(11) NOT NULL,
  `Tracción` text NOT NULL,
  `Cerrada` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `camionetas`
--

INSERT INTO `camionetas` (`Placa`, `Tracción`, `Cerrada`) VALUES
(5, 'Delantera', 1),
(6, 'Trasera', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `coches`
--

CREATE TABLE `coches` (
  `placa` int(11) NOT NULL,
  `color` text NOT NULL,
  `marca` text NOT NULL,
  `modelo` text NOT NULL,
  `velocidad` int(4) NOT NULL,
  `caballaje` int(3) NOT NULL,
  `plazas` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `coches`
--

INSERT INTO `coches` (`placa`, `color`, `marca`, `modelo`, `velocidad`, `caballaje`, `plazas`) VALUES
(1, 'Blanco', 'VW', '2022', 220, 150, 5),
(2, 'Azul', 'Nissan', '2020', 180, 150, 6),
(3, 'Negro', 'Dina', '2020', 180, 300, 12),
(4, 'Azul', 'Star', '2019', 150, 200, 14),
(5, 'Amarillo', 'Renault', '2025', 240, 250, 8),
(6, 'Blanco', 'Nissan', '2020', 180, 150, 6);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `camiones`
--
ALTER TABLE `camiones`
  ADD KEY `FK_Placa` (`Placa`);

--
-- Indices de la tabla `camionetas`
--
ALTER TABLE `camionetas`
  ADD KEY `FK_Placa` (`Placa`);

--
-- Indices de la tabla `coches`
--
ALTER TABLE `coches`
  ADD PRIMARY KEY (`placa`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `coches`
--
ALTER TABLE `coches`
  MODIFY `placa` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `camiones`
--
ALTER TABLE `camiones`
  ADD CONSTRAINT `camiones_ibfk_1` FOREIGN KEY (`Placa`) REFERENCES `coches` (`placa`);

--
-- Filtros para la tabla `camionetas`
--
ALTER TABLE `camionetas`
  ADD CONSTRAINT `camionetas_ibfk_1` FOREIGN KEY (`Placa`) REFERENCES `coches` (`placa`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
