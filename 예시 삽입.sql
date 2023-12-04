use projectdb;
#show tables;
#describe tb_student;

INSERT INTO tb_student (STU_NO, NAME, BIRTH, SEX, STU_GRADE, TEL_NO, STU_SCORE, MAJOR_CODE, LICENSE)
VALUES
("2019001001", "김철수", "20000101", "남", "3", "010-0001-0001", "3.5", "001", "0"),
("2019002001", "정영희", "20000202", "여", "1", "010-0002-0002", "3.7", "002", "1"),
("2019003001", "박순구", "20000303", "남", "2", "010-0003-0003", "4.0", "003", "0"),
("2019004001", "황정민", "20000404", "남", "3", "010-0004-0004", "2.3", "004", "3"),
("2019005001", "남희철", "20000505", "남", "4", "010-0005-0005", "4.2", "005", "2");

INSERT INTO tb_department (MAJOR_CODE, DEP_NAME)
VALUES
("001", "전자공학부"),
("002", "전기공학부"),
("003", "정보통신공학부"),
("004", "컴퓨터공학부"),
("005", "소프트웨어공학부"),
("006", "지능로봇공학부");

INSERT INTO tb_history (RECEIVED_NUM, SCH_NAME, STU_NO, SEMESTER)
VALUES
("1", "a", "2019001001", "1901"),
("2", "a", "2019002001", "1902"),
("3", "b", "2019001001", "2001"),
("4", "c", "2019003001", "2001"),
("5", "b", "2019001001", "2102");

INSERT INTO tb_semester (SEMESTER, YEAR, PART)
VALUES
("1901", "2019년", "1학기"),
("1902", "2019년", "2학기"),
("2001", "2020년", "1학기"),
("2002", "2020년", "2학기"),
("2101", "2021년", "1학기"),
("2102", "2021년", "2학기"),
("2201", "2022년", "1학기"),
("2202", "2022년", "2학기");

INSERT INTO tb_scholarship (SCH_NAME, MONEY, REGULATIONS)
VALUES
("a", "100만원", "성적장학금"),
("b", "50만원", "봉사장학금"),
("c", "70만원", "특별장학금");

