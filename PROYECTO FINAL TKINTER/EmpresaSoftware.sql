-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 14-12-2024 a las 14:51:39
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `EmpresaSoftware`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Clientes`
--

CREATE TABLE `Clientes` (
  `ClienteID` int(11) NOT NULL,
  `Nombre` varchar(100) NOT NULL,
  `FechaRegistro` date NOT NULL DEFAULT curdate(),
  `Estado` varchar(50) DEFAULT 'Activo'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `Clientes`
--

INSERT INTO `Clientes` (`ClienteID`, `Nombre`, `FechaRegistro`, `Estado`) VALUES
(1, 'Juan Pérez', '2024-12-13', 'Activo'),
(2, 'María López', '2024-12-13', 'Activo'),
(3, 'Carlos Gómez', '2024-12-13', 'Inactivo'),
(8, 'Ramón Valdéz', '2024-12-14', 'Activo');

--
-- Disparadores `Clientes`
--
DELIMITER $$
CREATE TRIGGER `CheckClientesInactivos` AFTER UPDATE ON `Clientes` FOR EACH ROW BEGIN
    IF OLD.Estado = 'Activo' AND NEW.Estado = 'Inactivo' THEN
        INSERT INTO Notificaciones (ClienteID, Mensaje, FechaNotificacion)
        VALUES (NEW.ClienteID, CONCAT('El cliente ', NEW.Nombre, ' está inactivo desde ', NOW()), NOW());
    END IF;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Compras`
--

CREATE TABLE `Compras` (
  `CompraID` int(11) NOT NULL,
  `ClienteID` int(11) NOT NULL,
  `FechaCompra` date NOT NULL,
  `Monto` decimal(10,2) NOT NULL,
  `Descripcion` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `Compras`
--

INSERT INTO `Compras` (`CompraID`, `ClienteID`, `FechaCompra`, `Monto`, `Descripcion`) VALUES
(1, 1, '2024-12-01', 199.99, 'Software de contabilidad'),
(2, 2, '2024-12-02', 299.99, 'Sistema CRM'),
(3, 1, '2024-12-03', 99.99, 'Licencia adicional');

--
-- Disparadores `Compras`
--
DELIMITER $$
CREATE TRIGGER `AlertarPatronesCompra` AFTER INSERT ON `Compras` FOR EACH ROW BEGIN
    DECLARE MontoPromedio DECIMAL(10, 2);
    SELECT AVG(Monto) INTO MontoPromedio FROM Compras WHERE ClienteID = NEW.ClienteID;
    IF NEW.Monto > MontoPromedio * 2 THEN
        INSERT INTO Alertas (ClienteID, Mensaje, FechaAlerta)
        VALUES (NEW.ClienteID, CONCAT('Patrón inusual detectado: compra de ', NEW.Monto, ' supera el promedio por un factor de 2'), NOW());
    END IF;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Contactos`
--

CREATE TABLE `Contactos` (
  `ContactoID` int(11) NOT NULL,
  `ClienteID` int(11) NOT NULL,
  `Email` varchar(150) NOT NULL,
  `Telefono` varchar(20) DEFAULT NULL,
  `Direccion` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `Contactos`
--

INSERT INTO `Contactos` (`ContactoID`, `ClienteID`, `Email`, `Telefono`, `Direccion`) VALUES
(1, 1, 'juan.perez@email.com', '555-1234', 'Av. Principal 123'),
(2, 2, 'maria.lopez@email.com', '555-5678', 'Calle Secundaria 456'),
(3, 3, 'carlos.gomez@email.com', '555-9012', 'Plaza Central 789'),
(8, 8, 'soydonramon@gmail.com', '111111111', 'Ciudad de México');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Preferencias`
--

CREATE TABLE `Preferencias` (
  `PreferenciaID` int(11) NOT NULL,
  `ClienteID` int(11) NOT NULL,
  `Categoria` varchar(100) DEFAULT NULL,
  `Valor` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `Preferencias`
--

INSERT INTO `Preferencias` (`PreferenciaID`, `ClienteID`, `Categoria`, `Valor`) VALUES
(1, 1, 'Interés', 'Contabilidad'),
(2, 2, 'Interés', 'Gestión de clientes'),
(3, 3, 'Interés', 'Analítica de datos'),
(6, 8, 'Importante', 'Gestión Atención');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `Clientes`
--
ALTER TABLE `Clientes`
  ADD PRIMARY KEY (`ClienteID`);

--
-- Indices de la tabla `Compras`
--
ALTER TABLE `Compras`
  ADD PRIMARY KEY (`CompraID`),
  ADD KEY `ClienteID` (`ClienteID`);

--
-- Indices de la tabla `Contactos`
--
ALTER TABLE `Contactos`
  ADD PRIMARY KEY (`ContactoID`),
  ADD KEY `ClienteID` (`ClienteID`);

--
-- Indices de la tabla `Preferencias`
--
ALTER TABLE `Preferencias`
  ADD PRIMARY KEY (`PreferenciaID`),
  ADD UNIQUE KEY `ClienteID` (`ClienteID`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `Clientes`
--
ALTER TABLE `Clientes`
  MODIFY `ClienteID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `Compras`
--
ALTER TABLE `Compras`
  MODIFY `CompraID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `Contactos`
--
ALTER TABLE `Contactos`
  MODIFY `ContactoID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `Preferencias`
--
ALTER TABLE `Preferencias`
  MODIFY `PreferenciaID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `Compras`
--
ALTER TABLE `Compras`
  ADD CONSTRAINT `compras_ibfk_1` FOREIGN KEY (`ClienteID`) REFERENCES `Clientes` (`ClienteID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `Contactos`
--
ALTER TABLE `Contactos`
  ADD CONSTRAINT `contactos_ibfk_1` FOREIGN KEY (`ClienteID`) REFERENCES `Clientes` (`ClienteID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `Preferencias`
--
ALTER TABLE `Preferencias`
  ADD CONSTRAINT `preferencias_ibfk_1` FOREIGN KEY (`ClienteID`) REFERENCES `Clientes` (`ClienteID`) ON DELETE CASCADE ON UPDATE CASCADE;

DELIMITER $$
--
-- Eventos
--
CREATE DEFINER=`root`@`localhost` EVENT `VerificarClientesInactivos` ON SCHEDULE EVERY 1 WEEK STARTS '2024-12-13 19:14:48' ON COMPLETION NOT PRESERVE ENABLE DO BEGIN
    INSERT INTO Notificaciones (ClienteID, Mensaje, FechaNotificacion)
    SELECT ClienteID, CONCAT('Cliente inactivo desde ', FechaRegistro), NOW()
    FROM Clientes
    WHERE Estado = 'Inactivo' AND DATEDIFF(NOW(), FechaRegistro) > 30;
END$$

CREATE DEFINER=`root`@`localhost` EVENT `GenerarReportesMensuales` ON SCHEDULE EVERY 1 MONTH STARTS '2024-12-13 19:14:49' ON COMPLETION NOT PRESERVE ENABLE DO BEGIN
    DECLARE TotalVentas DECIMAL(10, 2);
    DECLARE NumCompras INT;
    DECLARE PromedioCompra DECIMAL(10, 2);

    CALL GenerarInformeVentas(TotalVentas, NumCompras, PromedioCompra);

    INSERT INTO Reportes (Tipo, Detalles, FechaGeneracion)
    VALUES ('Ventas Mensuales', CONCAT('Total: ', TotalVentas, ', Compras: ', NumCompras, ', Promedio: ', PromedioCompra), NOW());
END$$

CREATE DEFINER=`root`@`localhost` EVENT `LimpiezaRegistrosAnuales` ON SCHEDULE EVERY 1 YEAR STARTS '2024-12-13 19:14:49' ON COMPLETION NOT PRESERVE ENABLE DO BEGIN
    DELETE FROM Compras WHERE FechaCompra < DATE_SUB(NOW(), INTERVAL 5 YEAR);
    DELETE FROM LogsCambiosContactos WHERE FechaCambio < DATE_SUB(NOW(), INTERVAL 5 YEAR);
END$$

DELIMITER ;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
