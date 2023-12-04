import mysql.connector

# 데이터베이스 연결
def connect_to_db():
    cnx = mysql.connector.connect(user='root', password='0000',
                                  host='localhost',
                                  database='projectdb')
    return cnx

# 데이터베이스 연결 종료
def close_db(cnx):
    if cnx:
        cnx.close()

# SQL 쿼리 실행 후 결과 반환
def execute_query(cnx, query):
    cursor = cnx.cursor()
    cursor.execute(query)
    field_names = [i[0] for i in cursor.description]
    result = cursor.fetchall()
    return field_names, result

# 메인 함수
def main():
    cnx = connect_to_db()
    while True:
        # 메뉴 출력
        print("[전체 정보 검색]")
        print("1. 모든 학생 통합 정보 확인")
        print("2. 장학금 받은 전체 학생 정보 확인")
        print("3. 모든 학과별 소속 학생 명단 확인")
        print("4. 전체 장학금별 수령 학생 명단 확인")
        print("5. 모든 학생 학점 평균 계산")
        print("6. 학과별 성적 정보 및 학생 수, 장학금 수령 횟수 확인")
        print("[특정 테이블 입력]")
        print("7. 특정 학생 장학 수령 내역 확인")
        print("8. 특정 학과 소속 학생 명단 확인")
        print("9. 특정 장학금 수령 학생 명단 확인")
        print("0. 종료")
        choice = input("원하는 기능의 번호를 입력하세요: ")

        # 사용자 입력에 따라 쿼리 생성 및 실행
        if choice == '1':
            query = """
            SELECT tb_student.STU_NO, tb_student.NAME, tb_student.STU_GRADE, tb_student.STU_SCORE, tb_department.DEP_NAME, COUNT(tb_history.SCH_CODE) as Scholarship_Count
            FROM tb_student
            INNER JOIN tb_department ON tb_student.MAJOR_CODE = tb_department.MAJOR_CODE
            LEFT JOIN tb_history ON tb_student.STU_NO = tb_history.STU_NO
            GROUP BY tb_student.STU_NO;
            """
        elif choice == '2':
            query = """
            SELECT tb_history.STU_NO, tb_student.NAME, tb_student.BIRTH, tb_student.SEX, tb_student.STU_GRADE, tb_student.TEL_NO, tb_student.LICENSE, tb_student.STU_SCORE
            FROM tb_history
            INNER JOIN tb_student ON tb_history.STU_NO = tb_student.STU_NO;
            """
        elif choice == '3':
            query = """
            SELECT tb_department.DEP_NAME, tb_student.STU_NO, tb_student.NAME
            FROM tb_student
            INNER JOIN tb_department ON tb_student.MAJOR_CODE = tb_department.MAJOR_CODE
            ORDER BY tb_department.DEP_NAME;
            """
        elif choice == '4':
            query = """
            SELECT tb_scholarship.SCH_CODE, tb_student.STU_NO, tb_student.NAME
            FROM tb_history
            INNER JOIN tb_student ON tb_history.STU_NO = tb_student.STU_NO
            INNER JOIN tb_scholarship ON tb_history.SCH_CODE = tb_scholarship.SCH_CODE
            ORDER BY tb_scholarship.SCH_CODE;
            """
        elif choice == '5':
            query = """
            SELECT ROUND(AVG(STU_SCORE), 2) as Average_Score
            FROM tb_student;
            """
        elif choice == '6':
            query = """
            SELECT tb_department.DEP_NAME, ROUND(AVG(tb_student.STU_SCORE), 2) as Average_Score, COUNT(DISTINCT tb_student.STU_NO) as Student_Count, COUNT(tb_history.SCH_CODE) as Scholarship_Count
            FROM tb_student
            INNER JOIN tb_department ON tb_student.MAJOR_CODE = tb_department.MAJOR_CODE
            LEFT JOIN tb_history ON tb_student.STU_NO = tb_history.STU_NO
            GROUP BY tb_department.DEP_NAME;
            """
        elif choice == '7':
            stu_no = input("학번을 입력하세요: ")
            query = f"""
            SELECT tb_student.STU_NO, tb_student.NAME, tb_scholarship.SCH_NAME, tb_scholarship.MONEY, tb_semester.YEAR, tb_semester.PART
            FROM tb_history
            INNER JOIN tb_student ON tb_history.STU_NO = tb_student.STU_NO
            INNER JOIN tb_scholarship ON tb_history.SCH_CODE = tb_scholarship.SCH_CODE
            INNER JOIN tb_semester ON tb_history.SEMESTER = tb_semester.SEMESTER
            WHERE tb_student.STU_NO = '{stu_no}'
            ORDER BY tb_semester.YEAR ASC, tb_semester.PART ASC;
            """
        elif choice == '8':
            dep_name = input("학과 이름을 입력하세요: ")
            query = f"""
            SELECT tb_student.STU_NO, tb_student.NAME, tb_student.STU_GRADE, tb_student.STU_SCORE, COUNT(tb_history.SCH_CODE) as Scholarship_Count
            FROM tb_student
            INNER JOIN tb_department ON tb_student.MAJOR_CODE = tb_department.MAJOR_CODE
            LEFT JOIN tb_history ON tb_student.STU_NO = tb_history.STU_NO
            WHERE tb_department.DEP_NAME = '{dep_name}'
            GROUP BY tb_student.STU_NO;
            """
        elif choice == '9':
            sch_code = input("장학금 코드를 입력하세요: ")
            query = f"""
            SELECT tb_student.STU_NO, tb_student.NAME, tb_scholarship.SCH_NAME, tb_scholarship.MONEY, tb_semester.YEAR, tb_semester.PART
            FROM tb_history
            INNER JOIN tb_student ON tb_history.STU_NO = tb_student.STU_NO
            INNER JOIN tb_scholarship ON tb_history.SCH_CODE = tb_scholarship.SCH_CODE
            INNER JOIN tb_semester ON tb_history.SEMESTER = tb_semester.SEMESTER
            WHERE tb_history.SCH_CODE = '{sch_code}';
            """
        elif choice == '0':
            break
        else:
            print("잘못된 입력입니다. 다시 시도해주세요.")
            continue

        # 쿼리 실행 후 결과 출력
        field_names, result = execute_query(cnx, query)
        print(field_names)
        for row in result:
            print(row)

    close_db(cnx)

if __name__ == "__main__":
    main()
