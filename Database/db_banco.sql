-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 06-08-2021 a las 00:46:24
-- Versión del servidor: 10.4.18-MariaDB
-- Versión de PHP: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `db_banco`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_cuenta_ahorro`
--

CREATE TABLE `tbl_cuenta_ahorro` (
  `ID_CUENTA_AHORRO` int(11) NOT NULL,
  `N_CUENTA` int(11) NOT NULL,
  `MONTO_INGRESAR` int(10) NOT NULL,
  `MONTO_RETIRAR` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tbl_cuenta_ahorro`
--

INSERT INTO `tbl_cuenta_ahorro` (`ID_CUENTA_AHORRO`, `N_CUENTA`, `MONTO_INGRESAR`, `MONTO_RETIRAR`) VALUES
(1, 1, 8700, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_depositos`
--

CREATE TABLE `tbl_depositos` (
  `ID_DEPOSITO` int(11) NOT NULL,
  `N_CUENTA` int(11) NOT NULL,
  `MONTO` int(10) NOT NULL,
  `N_CUENTA_DEPOSITAR` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tbl_depositos`
--

INSERT INTO `tbl_depositos` (`ID_DEPOSITO`, `N_CUENTA`, `MONTO`, `N_CUENTA_DEPOSITAR`) VALUES
(1, 1, 9000, 8700);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_prestamo`
--

CREATE TABLE `tbl_prestamo` (
  `ID_PRESTAMO` int(11) NOT NULL,
  `N_CUENTA` int(11) NOT NULL,
  `MONTO_PRESTAR` int(10) NOT NULL,
  `MONTO_PAGAR` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tbl_prestamo`
--

INSERT INTO `tbl_prestamo` (`ID_PRESTAMO`, `N_CUENTA`, `MONTO_PRESTAR`, `MONTO_PAGAR`) VALUES
(1, 1, 8700, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_usuarios`
--

CREATE TABLE `tbl_usuarios` (
  `N_CUENTA` int(11) NOT NULL,
  `ID_USUARIO` int(11) NOT NULL,
  `EDAD` int(5) NOT NULL,
  `NOMBRE_APELLIDO` varchar(50) NOT NULL,
  `CONTRASENA` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tbl_usuarios`
--

INSERT INTO `tbl_usuarios` (`N_CUENTA`, `ID_USUARIO`, `EDAD`, `NOMBRE_APELLIDO`, `CONTRASENA`) VALUES
(1, 0, 26, 'Lissy Bonilla', '12345');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `tbl_cuenta_ahorro`
--
ALTER TABLE `tbl_cuenta_ahorro`
  ADD PRIMARY KEY (`ID_CUENTA_AHORRO`),
  ADD KEY `FK_USUARIOS_CUENTA` (`N_CUENTA`);

--
-- Indices de la tabla `tbl_depositos`
--
ALTER TABLE `tbl_depositos`
  ADD PRIMARY KEY (`ID_DEPOSITO`),
  ADD KEY `FK_USUARIOS_DEPOSITO` (`N_CUENTA`);

--
-- Indices de la tabla `tbl_prestamo`
--
ALTER TABLE `tbl_prestamo`
  ADD PRIMARY KEY (`ID_PRESTAMO`),
  ADD KEY `FK_USUARIOS_PRESTAMO` (`N_CUENTA`);

--
-- Indices de la tabla `tbl_usuarios`
--
ALTER TABLE `tbl_usuarios`
  ADD PRIMARY KEY (`N_CUENTA`),
  ADD KEY `FK_TBL_USUARIO_CUENTA_AHORRO` (`ID_USUARIO`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `tbl_cuenta_ahorro`
--
ALTER TABLE `tbl_cuenta_ahorro`
  MODIFY `ID_CUENTA_AHORRO` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `tbl_depositos`
--
ALTER TABLE `tbl_depositos`
  MODIFY `ID_DEPOSITO` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `tbl_prestamo`
--
ALTER TABLE `tbl_prestamo`
  MODIFY `ID_PRESTAMO` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `tbl_usuarios`
--
ALTER TABLE `tbl_usuarios`
  MODIFY `N_CUENTA` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `tbl_cuenta_ahorro`
--
ALTER TABLE `tbl_cuenta_ahorro`
  ADD CONSTRAINT `tbl_cuenta_ahorro_ibfk_1` FOREIGN KEY (`N_CUENTA`) REFERENCES `tbl_usuarios` (`N_CUENTA`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `tbl_depositos`
--
ALTER TABLE `tbl_depositos`
  ADD CONSTRAINT `tbl_depositos_ibfk_1` FOREIGN KEY (`N_CUENTA`) REFERENCES `tbl_usuarios` (`N_CUENTA`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `tbl_prestamo`
--
ALTER TABLE `tbl_prestamo`
  ADD CONSTRAINT `tbl_prestamo_ibfk_1` FOREIGN KEY (`N_CUENTA`) REFERENCES `tbl_usuarios` (`N_CUENTA`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
