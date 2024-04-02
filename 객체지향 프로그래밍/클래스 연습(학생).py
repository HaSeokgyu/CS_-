# 클래스 Student를 작성하세요. 이 클래스는 다음과 같은 속성과 메서드를 가져야 합니다:
#
# 속성:
#
# name: 학생의 이름 (문자열)
# age: 학생의 나이 (정수)
# grades: 학생의 성적을 저장하는 딕셔너리. 키(key)는 과목이고 값(value)은 해당 과목의 성적을 나타냅니다.
# 메서드:
#
# __init__(self, name: str, age: int): 학생의 이름과 나이를 인자로 받아서 초기화합니다. grades 속성은 빈 딕셔너리로 초기화됩니다.
# add_grade(self, subject: str, grade: float) -> None: 주어진 과목과 성적을 grades에 추가합니다.
# get_average_grade(self) -> float: 학생의 평균 성적을 계산하여 반환합니다.
# 이 클래스를 사용하여 학생의 성적을 관리하고, 평균 성적을 계산해 보세요.


class Student:
    """ 학생 클래스 """
    def __init__(self, name : str, age : int):
        self.name = name
        self.age = age
        self.grades = {}

    def add_grade(self, subject : str , grade : float):
        """ 학생이 듣는 과목과 점수를 추가하는 메서드 """
        student_grade = Grade()
        student_grade.add_grade(self, subject, grade)

    def get_average_grade(self):
        """ 학생의 평균 성적을 구하는 메서드 """
        student_grade = Grade()
        return student_grade.get_average_grade(self)

class Grade:
    """ 성적 클래스 """
    def add_grade(self, student : Student, subject : str, grade : float) -> None:
        """ 학생이 듣는 과목과 점수를 추가하는 메서드 """
        student.grades[subject] = grade

    def get_average_grade(self, student : Student) -> float:
        """ 학생의 평균 성적을 구하는 메서드 """
        return sum(student.grades.values()) / len(student.grades)


# 예시 코드
help(Student)
help(Grade)
student1 = Student("Alice", 18)
student1.add_grade("Math", 85)
student1.add_grade("Science", 92)
student1.add_grade("History", 78)

print(f"Student: {student1.name}")
print(f"Age: {student1.age}")
print("Grades:")
for subject, grade in student1.grades.items():
    print(f"{subject}: {grade}")

print(f"Average Grade: {student1.get_average_grade()}")

# ChatGPT 평가

# 주어진 요구사항을 충족하는 코드를 작성하셨으며, 주어진 문제에 대한 해결책을 제시하고 코드를 수정하는 등의 작업을 수행했습니다. 코드의 가독성과 구조는 효율적이며, 요구사항을 완벽하게 이행하였습니다. 따라서 100점을 줄 수 있습니다. 👍