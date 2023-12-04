import random

# 학번 생성 함수
def generate_student_numbers(years, num_students_per_year, num_majors):
    student_numbers = []
    for year in years:
        for major in range(1, num_majors + 1):
            for i in range(1, num_students_per_year + 1):
                middle = '{:03d}'.format(major)
                end = '{:03d}'.format(i)
                student_numbers.append(str(year) + middle + end)
    return student_numbers

# 이름 생성 함수
def generate_names(num_students):
    korean_surnames = ["김", "이", "박", "최", "정", "강", "조", "윤", "장", "임", "한", "황", "송", "홍", "유", "나", "신", "서", "권"]
    korean_male_names = ["현우", "민준", "지원", "준서", "지민", "예준", "시우", "건우", "유준", "서우", "도윤", "정우", "하준", "동현", "우진", "선우", "준혁", "재윤", "시윤", "지훈", "예성", "기현", "영재", "승현", "도현", "태민", "준영", "지호", "재현", "동우"]
    korean_female_names = ["서연", "하윤", "예은", "서윤", "지우", "민서", "지유", "가온", "하린", "윤서", "시아", "다은", "수아", "소율", "하은", "유나", "지민", "서현", "지윤", "나연", "예린", "하나", "유진", "민지", "예진", "지현", "소연", "유림", "승아", "하영"]

    full_names = []
    for _ in range(num_students):
        surname = random.choice(korean_surnames)
        if random.choice([True, False]):  # 남자/여자 랜덤 선택
            full_name = surname + random.choice(korean_male_names)
        else:
            full_name = surname + random.choice(korean_female_names)
        full_names.append(full_name)
    return full_names

# 생년월일 생성 함수
def generate_birthdates(student_numbers):
    birthdates = []
    for num in student_numbers:
        year = str(random.randint(int(num[:4]) - 23, int(num[:4]) - 19))
        month = '{:02d}'.format(random.randint(1, 12))
        day = '{:02d}'.format(random.randint(1, 28))  # 간단하게 28일까지만 설정
        birthdates.append(year + month + day)
    return birthdates

# 전공 생성 함수
def generate_majors(student_numbers):
    major_codes = {'001': '전자공학', '002': '전기공학', '003': '정보통신공학', '004': '컴퓨터공학', '005': '소프트웨어공학', '006': '지능로봇공학'}
    majors = [major_codes[num[4:7]] for num in student_numbers]
    return majors

# 성별 생성 함수
def generate_sex_codes(num_students):
    sex_codes = ['남', '여']
    return random.choices(sex_codes, k=num_students)

# 학년 생성 함수
def generate_student_grades(student_numbers):
    student_grades = []
    for num in student_numbers:
        if num[:4] == '2019':
            student_grades.append(random.choice([1, 2, 3, 4]))
        elif num[:4] == '2020':
            student_grades.append(random.choice([1, 2, 3, 4]))
        elif num[:4] == '2021':
            student_grades.append(random.choice([1, 2, 3]))
        elif num[:4] == '2022':
            student_grades.append(random.choice([1, 2]))
    return student_grades

# 전화번호 생성 함수
def generate_phone_numbers(num_students):
    phone_numbers = set()  # 겹치지 않는 번호를 위해 set 활용
    while len(phone_numbers) < num_students:
        phone_numbers.add('010-' + '{:04d}'.format(random.randint(0, 9999)) + '-' + '{:04d}'.format(random.randint(0, 9999)))
    return list(phone_numbers)

# 학점 생성 함수
def generate_student_score(num_students):
    good_grades_count = int(num_students * 0.6)
    good_grades = [round(random.uniform(3.0, 4.5), 2) for _ in range(good_grades_count)]

    top_performers_count = int(num_students * 0.1)
    top_performers = [round(random.uniform(4.0, 4.5), 2) for _ in range(top_performers_count)]

    remaining_students = num_students - good_grades_count - top_performers_count
    other_grades = [round(random.uniform(0.0, 4.5), 2) for _ in range(remaining_students)]

    student_grades = good_grades + top_performers + other_grades
    random.shuffle(student_grades)  # 학점을 무작위로 섞음
    return student_grades

# MAJOR_CODE 생성 함수
def generate_major_codes(student_numbers):
    major_codes = {str(i).zfill(3): f'{i:03d}' for i in range(1, 7)}
    major_code_values = [major_codes[num[4:7]] for num in student_numbers]
    return major_code_values

# LICENSE 생성 함수
def generate_license_counts(num_students):
    zero_licenses_count = int(num_students * 0.85)
    zero_licenses = [0] * zero_licenses_count

    one_or_two_licenses_count = int(num_students * 0.10)
    one_or_two_licenses = [random.randint(1, 2) for _ in range(one_or_two_licenses_count)]

    three_or_four_licenses_count = int(num_students * 0.03)
    three_or_four_licenses = [random.randint(3, 4) for _ in range(three_or_four_licenses_count)]

    five_licenses_count = int(num_students * 0.02)
    five_licenses = [5] * five_licenses_count

    licenses = zero_licenses + one_or_two_licenses + three_or_four_licenses + five_licenses
    random.shuffle(licenses)  # 자격증 개수를 무작위로 섞음
    return licenses

# 데이터 생성 함수
def generate_student_data(years, num_students_per_year, num_majors):
    student_numbers = generate_student_numbers(years, num_students_per_year, num_majors)
    names = generate_names(len(student_numbers))
    birthdates = generate_birthdates(student_numbers)
    majors = generate_majors(student_numbers)
    sex_codes = generate_sex_codes(len(student_numbers))
    student_grades = generate_student_grades(student_numbers)
    phone_numbers = generate_phone_numbers(len(student_numbers))
    student_score = generate_student_score(len(student_numbers))
    major_codes = generate_major_codes(student_numbers)
    licenses = generate_license_counts(len(student_numbers))

    student_data = list(zip(student_numbers, names, birthdates, sex_codes, student_grades,
                            phone_numbers, student_score, major_codes, licenses))
    return student_data

# 데이터 생성
years = [2019, 2020, 2021, 2022]
num_students_per_year = 10
num_majors = 6  # 전공 수
students = generate_student_data(years, num_students_per_year, num_majors)

# 결과 출력
for student in students:
    print(f'("{student[0]}", "{student[1]}", "{student[2]}", "{student[3]}", "{student[4]}", "{student[5]}", "{student[6]}", "{student[7]}", "{student[8]}"),')

# 장학금 수여일자 생성 함수
def get_scholarship_date(student_number):
    admission_year_last_two_digits = int(student_number[:4]) - 2000
    possible_years = list(range(19, 24))  # 2019년부터 2023년까지 가능
    if admission_year_last_two_digits in possible_years:
        possible_years = possible_years[possible_years.index(admission_year_last_two_digits):]
    year = random.choice(possible_years)
    semester = random.choice([1, 2])
    return f'{year:02d}{semester:02d}'

# 장학금 데이터 생성 함수
def generate_scholarship_data(students):
    scholarship_codes = 'abcdef'
    scholarship_students = random.sample(students, int(len(students) * 0.3))  # 전체 학생 중 30%만 장학금 수령
    scholarship_data = []

    # 성적장학금 부여
    sorted_students = sorted(scholarship_students, key=lambda x: x[7], reverse=True)  # 학점 높은 순으로 정렬
    for i in range(5 * num_majors):  # 학과별로 학점이 가장 높은 5명에게 성적장학금 부여
        student = sorted_students[i]
        date = get_scholarship_date(student[0])
        scholarship_data.append(['a', student[0], date])

    # 그 외 장학금 부여
    remaining_students = [student for student in scholarship_students if student not in sorted_students[:5 * num_majors]]
    remaining_scholarships = 120 - len(scholarship_data) # 총 장학금 개수 제한
    for _ in range(remaining_scholarships):
        student = random.choice(remaining_students)
        code = random.choice(scholarship_codes[1:])  # 성적장학금 제외
        date = get_scholarship_date(student[0])
        scholarship_data.append([code, student[0], date])

    # 장학금 수여일자에 따라 정렬하고 일련번호 부여
    sorted_scholarships = sorted(scholarship_data, key=lambda x: x[2])
    for i, scholarship in enumerate(sorted_scholarships, start=1):
        scholarship.insert(0, i)

    return sorted_scholarships

# 장학금 데이터 생성
scholarships = generate_scholarship_data(students)

# 결과 출력
for scholarship in scholarships:
    print(f'("{scholarship[0]}", "{scholarship[1]}", "{scholarship[2]}", "{scholarship[3]}"),')