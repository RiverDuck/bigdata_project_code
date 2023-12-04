-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema projectdb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema projectdb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `projectdb` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin ;
USE `projectdb` ;

-- -----------------------------------------------------
-- Table `projectdb`.`tb_department`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `projectdb`.`tb_department` ;

CREATE TABLE IF NOT EXISTS `projectdb`.`tb_department` (
  `MAJOR_CODE` CHAR(6) NOT NULL,
  `DEP_NAME` VARCHAR(20) NULL DEFAULT NULL,
  PRIMARY KEY (`MAJOR_CODE`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_bin;


-- -----------------------------------------------------
-- Table `projectdb`.`tb_scholarship`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `projectdb`.`tb_scholarship` ;

CREATE TABLE IF NOT EXISTS `projectdb`.`tb_scholarship` (
  `SCH_CODE` VARCHAR(20) NOT NULL,
  `MONEY` VARCHAR(10) NULL DEFAULT NULL,
  `SCH_NAME` VARCHAR(200) NULL DEFAULT NULL,
  PRIMARY KEY (`SCH_CODE`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_bin;


-- -----------------------------------------------------
-- Table `projectdb`.`tb_semester`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `projectdb`.`tb_semester` ;

CREATE TABLE IF NOT EXISTS `projectdb`.`tb_semester` (
  `SEMESTER` VARCHAR(5) NOT NULL,
  `YEAR` CHAR(10) NULL DEFAULT NULL,
  `PART` CHAR(5) NULL DEFAULT NULL,
  PRIMARY KEY (`SEMESTER`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_bin;


-- -----------------------------------------------------
-- Table `projectdb`.`tb_student`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `projectdb`.`tb_student` ;

CREATE TABLE IF NOT EXISTS `projectdb`.`tb_student` (
  `STU_NO` CHAR(10) NOT NULL,
  `NAME` VARCHAR(10) NULL DEFAULT NULL,
  `BIRTH` CHAR(8) NULL DEFAULT NULL,
  `SEX` CHAR(3) NULL DEFAULT NULL,
  `STU_GRADE` CHAR(1) NULL DEFAULT NULL,
  `TEL_NO` VARCHAR(150) NULL DEFAULT NULL,
  `LICENSE` VARCHAR(200) NULL DEFAULT NULL,
  `MAJOR_CODE` CHAR(6) NULL DEFAULT NULL,
  `STU_SCORE` VARCHAR(10) NULL DEFAULT NULL,
  PRIMARY KEY (`STU_NO`),
  INDEX `MAJOR_CODE_idx` (`MAJOR_CODE` ASC) VISIBLE,
  CONSTRAINT `MAJOR`
    FOREIGN KEY (`MAJOR_CODE`)
    REFERENCES `projectdb`.`tb_department` (`MAJOR_CODE`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_bin;


-- -----------------------------------------------------
-- Table `projectdb`.`tb_history`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `projectdb`.`tb_history` ;

CREATE TABLE IF NOT EXISTS `projectdb`.`tb_history` (
  `RECEIVED_NUM` VARCHAR(10) NOT NULL,
  `SCH_CODE` VARCHAR(20) NULL DEFAULT NULL,
  `STU_NO` CHAR(10) NULL DEFAULT NULL,
  `SEMESTER` VARCHAR(5) NULL DEFAULT NULL,
  PRIMARY KEY (`RECEIVED_NUM`),
  INDEX `SCH_idx` (`SCH_CODE` ASC) VISIBLE,
  INDEX `STU_idx` (`STU_NO` ASC) VISIBLE,
  INDEX `SEMESTER_idx` (`SEMESTER` ASC) VISIBLE,
  CONSTRAINT `SCH`
    FOREIGN KEY (`SCH_CODE`)
    REFERENCES `projectdb`.`tb_scholarship` (`SCH_CODE`),
  CONSTRAINT `SEMESTER`
    FOREIGN KEY (`SEMESTER`)
    REFERENCES `projectdb`.`tb_semester` (`SEMESTER`),
  CONSTRAINT `STU`
    FOREIGN KEY (`STU_NO`)
    REFERENCES `projectdb`.`tb_student` (`STU_NO`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_bin;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
