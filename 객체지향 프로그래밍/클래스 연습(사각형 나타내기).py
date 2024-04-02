# 클래스 이름 - Rectangle
# 다음과 같은 속성을 지님 (1) 가로 길이, (2) 세로 길이
# 사각형의 넓이를 계산하여 반환하는 calculate_area() 메서드 구현하기
# 사각형의 둘레를 계산하여 반환하는 calculate_perimeter() 메서드 구현하기

class Rectangle:
    """사각형을 나타내는 클래스"""

    def __init__(self, width, height):
        self.width = width
        self.height = height
        if self.width == self.height:
            self.type = '정사각형'
        else:
            self.type = '직사각형'

    def __str__(self):
        if self.type == '직사각형':
            return f'해당 {self.type}의 가로 길이 {self.width}, 세로 길이 {self.height}입니다.'
        else:
            return f'해당 {self.type}의 가로 세로 길이{self.width}입니다.'
    def calculate_area(self):
        return print(f'해당 {self.type}의 넓이는 {self.width * self.height}입니다.')

    def calculate_perimeter(self):
        if self.type == '직사각형':
            return print(f'해당 {self.type}의 둘레는 {(self.width*2) + (self.height*2)}입니다.')
        else:
            return print(f'해당 {self.type}의 둘레는 {self.width * 4}입니다.')


squre_1 = Rectangle(4,5)
squre_2 = Rectangle(6,6)

print(squre_1)
squre_1.calculate_area()
squre_1.calculate_perimeter()

print(squre_2)
squre_2.calculate_area()
squre_2.calculate_perimeter()

# 개선점
# (1) 타입힌트 사용하기
# (2) 속성 접근을 직접적으로 하지 않기
# (3) 문서화 추가
# (4) 메서드는 결과값만 리턴하기
# (5) 예외 처리 추가