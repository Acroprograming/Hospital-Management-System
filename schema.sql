
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+50:30";

--
-- Database: `hms`
--

-- --------------------------------------------------------

--
-- Table structure for table `diagnostics`
--

CREATE TABLE `diagnostics` (
  `diagnostic_id` int(10) NOT NULL,
  `name_of_test` varchar(255) NOT NULL,
  `amount` decimal(19,0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `diagnostics_conducted`
--

CREATE TABLE `diagnostics_conducted` (
  `patient_id` int(10) NOT NULL,
  `diagnostic_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `medicine`
--

CREATE TABLE `medicine` (
  `medicine_id` int(10) NOT NULL,
  `medicine_name` varchar(255) NOT NULL,
  `rate` decimal(19,0) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `medicine_issued`
--

CREATE TABLE `medicine_issued` (
  `patient_id` int(10) NOT NULL,
  `medicine_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

CREATE TABLE `patient` (
  `patient_id` int(10) NOT NULL,
  `patient_name` varchar(255) NOT NULL,
  `patient_age` int(10) NOT NULL,
  `date_of_admission` varchar(255) NOT NULL,
  `type_of_room` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `state` varchar(255) NOT NULL,
  `city` varchar(255) NOT NULL,
  `date_of_joining` varchar(255) NOT NULL,
  `date_of_discharge` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`username`, `password`) VALUES
('admin', 'password');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `diagnostics`
--
ALTER TABLE `diagnostics`
  ADD PRIMARY KEY (`diagnostic_id`);

--
-- Indexes for table `diagnostics_conducted`
--
ALTER TABLE `diagnostics_conducted`
  ADD PRIMARY KEY (`patient_id`,`diagnostic_id`),
  ADD KEY `FKDiagnostic427172` (`diagnostic_id`);

--
-- Indexes for table `medicine`
--
ALTER TABLE `medicine`
  ADD PRIMARY KEY (`medicine_id`);

--
-- Indexes for table `medicine_issued`
--
ALTER TABLE `medicine_issued`
  ADD PRIMARY KEY (`patient_id`,`medicine_id`),
  ADD KEY `FKMedicine_i667563` (`medicine_id`);

--
-- Indexes for table `patient`
--
ALTER TABLE `patient`
  ADD PRIMARY KEY (`patient_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `diagnostics`
--
ALTER TABLE `diagnostics`
  MODIFY `diagnostic_id` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `medicine`
--
ALTER TABLE `medicine`
  MODIFY `medicine_id` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `patient`
--
ALTER TABLE `patient`
  MODIFY `patient_id` int(10) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `diagnostics_conducted`
--
ALTER TABLE `diagnostics_conducted`
  ADD CONSTRAINT `FKDiagnostic427172` FOREIGN KEY (`diagnostic_id`) REFERENCES `diagnostics` (`diagnostic_id`),
  ADD CONSTRAINT `FKDiagnostic697444` FOREIGN KEY (`patient_id`) REFERENCES `patient` (`patient_id`);

--
-- Constraints for table `medicine_issued`
--
ALTER TABLE `medicine_issued`
  ADD CONSTRAINT `FKMedicine_i47009` FOREIGN KEY (`patient_id`) REFERENCES `patient` (`patient_id`),
  ADD CONSTRAINT `FKMedicine_i667563` FOREIGN KEY (`medicine_id`) REFERENCES `medicine` (`medicine_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
