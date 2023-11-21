-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 04, 2023 at 10:25 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.0.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `nail_scope`
--

-- --------------------------------------------------------

--
-- Table structure for table `blogs`
--

CREATE TABLE `blogs` (
  `Blog_ID` int(11) NOT NULL,
  `Author_name` varchar(45) NOT NULL,
  `Title` varchar(45) NOT NULL,
  `Description` varchar(500) NOT NULL,
  `Content` varchar(1500) NOT NULL,
  `Date` date NOT NULL,
  `Photo` varchar(45) NOT NULL,
  `Reference` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `blogs`
--

INSERT INTO `blogs` (`Blog_ID`, `Author_name`, `Title`, `Description`, `Content`, `Date`, `Photo`, `Reference`) VALUES
(2, 'Dalia Alzahrani', 'ACETONE NAIL POLISH REMOVERS BAD FOR YOUR NAI', 'You will come across different types of nail polish removers on the market today, namely, acetone as well as non-acetone nail polish removers. The majority of the well-known brands carry both these types of nail polish removers which will be mentioned on the label.', 'You will come across different types of nail polish removers on the market today, namely, acetone as well as non-acetone nail polish removers. The majority of the well-known brands carry both these types of nail polish removers which will be mentioned on the label.\r\n\r\nBoth these types consist of a solvent (similar to acetone) which helps to dissolve the hard film which is left on the nails by making use of the ingredients present in the nail polishes. These ingredients consist of plasticizers, resins, color pigments, as well as film formers. This aids in providing a uniform coating of nail polish which dries uniformly as well as quickly. However, it is quite difficult to remove these ingredients once you apply them on your nails.\r\n\r\nAcetone Nail Polish Removers \r\n\r\nBeing an extremely powerful solvent, acetone happens to be the best option when it comes to removing nail polish. However, it is likewise quite harsh given that a lot of natural oils will be removed from the skin and nails. And, in case an excessive amount of acetone is applied on the skin, your epidermis will appear to be white in color. This implies that your skin is dried out.', '2023-04-28', 'blog1.jpg', '');

-- --------------------------------------------------------

--
-- Table structure for table `diagnosis`
--

CREATE TABLE `diagnosis` (
  `Diagnosis_ID` int(11) NOT NULL,
  `Username` varchar(30) NOT NULL,
  `Photo` varchar(45) NOT NULL,
  `Diagnosis` varchar(45) NOT NULL,
  `Date` date NOT NULL,
  `Advice` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `diagnosis`
--

INSERT INTO `diagnosis` (`Diagnosis_ID`, `Username`, `Photo`, `Diagnosis`, `Date`, `Advice`) VALUES
(9, 'dalia11', 'mel.jpg', 'Melanoma', '2023-04-19', 'It is adviced to make an appointment to see a'),
(10, 'dalia11', 'ecz.jpg', 'Eczema', '2023-04-19', 'Avoiding irritating products, ecessive water '),
(11, 'dalia11', 'ecz.jpg', 'Eczema', '2023-04-19', 'Avoiding irritating products, ecessive water '),
(12, 'dalia11', 'mel.jpg', 'Melanoma', '2023-04-19', 'It is adviced to make an appointment to see a'),
(13, 'roro2000', 'ecz.jpg', 'Eczema', '2023-04-24', 'Avoiding irritating products, ecessive water '),
(14, 'roro2000', '17_1.PNG', 'Beaus Lines', '2023-04-25', 'Avoid artificial nails or harsh nail products, and Keep blood sugar under control if you have diabetes. Please visit your healthcare provider if the condition worsen'),
(17, 'roro2000', 'healthyN157.jpg', 'Healthy', '2023-04-25', ''),
(18, 'roro2000', '17_1.PNG', 'Beaus Lines', '2023-04-25', 'Avoid artificial nails or harsh nail products, and Keep blood sugar under control if you have diabetes. Please visit your healthcare provider if the condition worsen'),
(19, 'DaliaAdmin', 'ecz.jpg', 'Eczema', '2023-04-27', 'Avoiding irritating products, ecessive water contact, and moistrize regularly. Please visit your healthcare provider if the condition worsen'),
(20, 'dalia22', 'new-19.png', 'Eczema', '2023-04-30', 'Avoiding irritating products, ecessive water contact, and moistrize regularly. Please visit your healthcare provider if the condition worsen'),
(21, 'dalia44', '17_1.PNG', 'Beaus Lines', '2023-04-30', 'Avoid artificial nails or harsh nail products, and Keep blood sugar under control if you have diabetes. Please visit your healthcare provider if the condition worsen');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `User_ID` int(11) NOT NULL,
  `Username` varchar(45) NOT NULL,
  `Password` varchar(100) NOT NULL,
  `First_Name` varchar(45) NOT NULL,
  `Last_Name` varchar(45) NOT NULL,
  `Email` varchar(70) NOT NULL,
  `Gender` enum('Female','Male') NOT NULL,
  `DOB` date NOT NULL,
  `Nationality` varchar(45) NOT NULL,
  `Type` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`User_ID`, `Username`, `Password`, `First_Name`, `Last_Name`, `Email`, `Gender`, `DOB`, `Nationality`, `Type`) VALUES
(1234567894, 'dalia11', '$2b$12$zP5sZNhM6nhsV6zBlg1Z1udoO66gWYBa/3b7Mx01nccZuyWUBBdqC', 'Dalia', 'Ahmed', 'daliazh55@gmail.com', 'Female', '2023-04-05', 'Saudi', 'User'),
(1234567895, 'roro2000', '$2b$12$D8OpAgM6WlMeAduFu5A.d.3ND0TsA1YYnD7hKmEQtClFebNreJBN.', 'Rahaf', 'Alhajri', 'rahaf-2020-@hotmail.com', 'Female', '2023-03-31', 'Saudi', 'User'),
(1234567896, 'Admin1', '$2a$12$VRRKes7HF1aiIEUSY5NU4edsIky7qwnAxTOASknpRQc8J5CIhW41G', 'Dalia', 'Ahmed', 'daliazh00@gmail.com', 'Female', '2023-04-12', 'Saudi', 'Admin'),
(1234567897, 'Reema123', '$2b$12$/T0nIlh5CDbYxDWSxl33..bRrTuYeQlu1l8R9EpWftmkIp2WMUZi.', 'Reema', 'Ali', 'Reema@gmail.com', 'Female', '2023-03-29', 'antiguans', 'User'),
(1234567898, 'DaliaAdmin', '$2a$12$AdUjxFctMywkf7IiCcNvmuWUrl1YfeJlzsA61W30WcB3O4RKeDyQi', 'Dalia', 'Alzahrani', 'dalry_88@hotmail.com', 'Female', '2023-04-24', 'Saudi', 'Admin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `blogs`
--
ALTER TABLE `blogs`
  ADD PRIMARY KEY (`Blog_ID`);

--
-- Indexes for table `diagnosis`
--
ALTER TABLE `diagnosis`
  ADD PRIMARY KEY (`Diagnosis_ID`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`User_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `blogs`
--
ALTER TABLE `blogs`
  MODIFY `Blog_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `diagnosis`
--
ALTER TABLE `diagnosis`
  MODIFY `Diagnosis_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `User_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1234567902;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
