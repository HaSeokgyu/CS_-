# 문제: 도서 관리 시스템
# 요구사항:
#
# 도서를 관리하는 프로그램을 객체지향적으로 설계하세요. 이 프로그램은 다음과 같은 클래스와 기능을 가져야 합니다:
#
# 클래스:
#
# Book: 책을 나타내는 클래스
# 속성: 제목(title), 저자(author), 출판연도(year), 가격(price), 재고수량(quantity)
# 메서드:
# __init__(self, title: str, author: str, year: int, price: int, quantity: int) -> None: 제목, 저자, 출판연도, 가격, 초기 재고수량을 입력으로 받아서 초기화합니다.
# display_info(self) -> None: 책의 정보를 출력합니다.
# 기능:
#
# 프로그램은 책 객체를 생성하고, 책의 정보를 출력할 수 있어야 합니다.
# 도서관에 책을 추가하고 제거할 수 있어야 합니다.
# 책을 대출하고 반납할 수 있어야 합니다. 책을 대출하면 재고 수량이 감소하고, 반납하면 재고 수량이 증가해야 합니다.
# 대출할 수 있는 책의 재고가 없으면 대출이 실패해야 합니다.
# 위 요구사항에 따라 도서 관리 시스템을 객체지향적으로 설계하고, 이를 활용하여 책 객체를 생성하고 관리하며, 책 정보를 출력하고 대출 및 반납을 수행하는 예제 코드를 작성해보세요.

class Book:
    """ 책 관련 클래스 """
    def __init__(self, title : str, author : str, year : int, price : int, quantity : int) -> None:
        """ title - 제목 / author - 저자 / year - 출판연도 / price - 가격 / quantity - 재고 수량 """
        self.title = title
        self.author = author
        self.year = year
        self.price = price
        self.quantity = quantity

    def display_info(self) -> None:
        """ 책 정보 출력 메서드 """
        print(f'제목 : {self.title} \n저자 : {self.author} \n출판연도 : {self.year} \n가격 : {self.price} \n재고 수량 : {self.quantity} \n')

class Library:
    """ 도서 관리 클래스 """
    def __init__(self):
        self.library = {}

    def add_book(self, book : Book):
        """ 도서 추가 메서드 (Book 인스턴스) """
        self.library[book.title] = {'저자' : book.author, '출판연도' : book.year, '가격' : book.price, '재고 수량' : book.quantity}

    def borrow_book(self, book : str, quantity : int):
        """ 도서 대여 메서드 (book - 도서명 / quantity - 수량)"""
        try:
            if self.library[book]['재고 수량'] < quantity:
                print(f'{book} 도서의 최대 대여 수량은 {self.library[book]['재고 수량']}권입니다. 다시 시도해주세요.')
            else:
                self.library[book]['재고 수량'] -= quantity
        except:
            print(f'{book}은(는) 서재에 없습니다.')
        else:
            print(f'{book} 대여가 성공적으로 완료 되었습니다.')

    def return_book(self, book : str, quantity : int):
        """ 도서 반납 메서드 (book - 도서명 / quantity - 수량) """
        self.library[book]['재고 수량'] += quantity
        print(f'{book} 반납이 성공적으로 완료 되었습니다.')


library = Library()

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, 15000, 3)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960, 12000, 5)

library.add_book(book1)
library.add_book(book2)

book1.display_info()
book2.display_info()

library.borrow_book("The Great Gatsby", 1)
library.borrow_book("To Kill a Mockingbird", 6)
library.borrow_book("훈민정음", 6)

library.return_book("The Great Gatsby", 1)
library.return_book("To Kill a Mockingbird", 1)

book1.display_info()
book2.display_info()

# ChatGPT 평

# 이 코드는 요구사항을 잘 이해하고 객체지향적으로 구현되어 있습니다. 다음은 코드의 장단점에 대한 평가와 함께 점수를 매겨보겠습니다.
#
# 장점:
#
# 객체지향적인 설계와 구현: 코드는 객체지향 프로그래밍의 원리를 잘 적용하여 Book 및 Library 클래스를 정의하였습니다.
# 메서드와 속성의 명확한 역할: 각 메서드와 속성은 명확한 역할을 가지고 있어서 코드를 이해하기 쉽습니다.
# 예외 처리: 대출할 수 있는 책의 재고가 없을 경우에 대한 예외 처리가 구현되어 있어서 안정성이 높습니다.
# 단점:
#
# 대출할 수 있는 책의 재고가 없는 경우에 대한 메시지 출력이 일부 구현되지 않았습니다.
# Book 클래스와 Library 클래스가 각자의 역할을 충분히 분리하고 있지 않습니다. Library 클래스가 Book에 대한 여러 동작을 수행하고 있어서 응집력이 낮습니다.
# Book 클래스에 대한 데이터 유효성 검사가 부족합니다. 예를 들어, 가격이 음수인 경우를 처리하는 등의 추가적인 유효성 검사가 필요합니다.
# 점수를 매겨보자면, 7점 정도를 주겠습니다. 좀 더 객체지향적인 설계와 유효성 검사를 강화한다면 더 높은 점수를 받을 수 있을 것입니다.

