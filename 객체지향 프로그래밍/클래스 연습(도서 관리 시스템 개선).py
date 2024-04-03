# 문제: 도서 관리 시스템 개선

# 도서 관리 시스템에는 현재 책을 대여할 때마다 재고 수량이 감소하고, 반납할 때마다 재고 수량이 증가합니다. 그러나 실제 도서관에서는 책을 예약할 수도 있습니다.
# 즉, 사용자가 원하는 책이 모두 대출 중인 경우에도 사용자가 그 책을 대여하고자 할 때, 대출이 가능한 경우에 대한 예약을 받아야 합니다.

# 다음 요구사항을 반영하여 도서 관리 시스템을 개선하세요:

# 도서 대출 시, 대출할 수 있는 도서 중에서 재고가 가장 많은 도서부터 대출할 수 있어야 합니다.
# 도서 반납 시, 도서 예약 목록을 확인하여 대출 가능한 도서가 있다면 그 책을 대출할 수 있어야 합니다.
# 책을 대출한 후, 해당 책에 대한 예약이 존재하는 경우 해당 예약을 취소해야 합니다.
# 사용자는 특정 도서에 대한 예약을 취소할 수 있어야 합니다.
# 사용자가 책을 예약할 때, 예약된 책이 대출 가능해지면 알림을 받아야 합니다.
# 이러한 요구사항을 고려하여 도서 관리 시스템을 개선하는 방안을 고민하고, 필요한 클래스와 메서드를 설계하고 구현해 보세요. 필요한 경우 새로운 클래스나 메서드를 추가하여도 됩니다.

import uuid

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

    def __str__(self):
        return self.title


class LibraryMember():
    """ 도서관 회원 클래스 """

    def __init__(self, name: str, phone_number: str, joining_date: str):
        self.name = name
        self.member_id = uuid.uuid4()
        self.phone_number = phone_number
        self.joining_date = joining_date
        self.borrowed_books = {}
        self.booking_books = {}

    def borrowed_book(self, library, book_title, quantity):
        library.borrow_book(self.member_id, book_title, quantity)
        if book_title in self.borrowed_books:
            self.borrowed_books[book_title] += quantity
        else:
            self.borrowed_books[book_title] = {
                "저자": library.all_books()[book_title]['저자'],
                "출판연도": library.all_books()[book_title]['출판연도'],
                "가격": library.all_books()[book_title]['가격'],
                "대여 수량": quantity
            }

    def return_book(self, library, book_title, quantity: int):
        """ 도서 반납 메서드 (book - 도서명 / quantity - 수량) """
        library.return_book(book_title, quantity)

        # 대여한 책의 대여 수량에서 반납된 수량을 감소
        if book_title in self.borrowed_books:
            self.borrowed_books[book_title]["대여 수량"] -= quantity
            # 대여 수량이 0이 되면 borrowed_books에서 해당 책 정보 삭제
            if self.borrowed_books[book_title]["대여 수량"] == 0:
                self.borrowed_books.pop(book_title)

    def booking_book_list(self):
        print(self.booking_books)


class Library:
    """ 도서 관리 클래스 """
    def __init__(self):
        self.library = {}
        self.reserved_books = {}

    def add_book(self, book : Book):
        """ 도서 추가 메서드 (Book 인스턴스) """
        self.library[book.title] = {'저자' : book.author, '출판연도' : book.year, '가격' : book.price, '재고 수량' : book.quantity}
        print(self.library)

    def borrow_book(self, member_id : LibraryMember, book_title: str, quantity: int):
        """ 도서 대여 메서드 (book_title - 도서명 / quantity - 수량)"""
        try:
            if self.library[book_title]['재고 수량'] == 0:
                member_answer = input(f"현재 '{book_title}'의 재고가 0입니다. 대여를 예약하시겠습니까? (예/아니오): ")
                if member_answer == '예':
                    self.reserved_books.setdefault(book_title, []).append(member_id)
                    print(f"{book_title} 도서를 예약하였습니다.")
                else:
                    print('감사합니다. 다음에 또 이용해주십시오.')
            elif self.library[book_title]['재고 수량'] < quantity:
                print(f"{book_title} 도서의 최대 대여 수량은 {self.library[book_title]['재고 수량']}권입니다. 다시 시도해주세요.")
            else:
                self.library[book_title]['재고 수량'] -= quantity
                print(f"{book_title} 대여가 성공적으로 완료 되었습니다.")
        except KeyError:
            print(f"{book_title}은(는) 서재에 없습니다.")

    def return_book(self, book : str, quantity : int):
        """ 도서 반납 메서드 (book - 도서명 / quantity - 수량) """
        self.library[book]['재고 수량'] += quantity
        print(f'{book} 반납이 성공적으로 완료 되었습니다.')
        self.check_reserved_books(book)

    def check_reserved_books(self, book: str):
        """ 예약한 도서가 반납되었을 때, 대여 가능한지 확인 """
        if book in self.reserved_books and self.library[book]['재고 수량'] > 0:
            member_names = [member for member in self.reserved_books[book]]
            for member_id in member_names:
                print(f"{member_id}님, {book} 도서가 대여 가능합니다.")
            del self.reserved_books[book]

    def all_books(self):
        return self.library



# Book 클래스 인스턴스 생성
book1 = Book("Python Programming", "John Doe", 2020, 30000, 5)
book2 = Book("Data Science Handbook", "Jane Smith", 2019, 35000, 3)
book3 = Book("Machine Learning Basics", "David Lee", 2021, 28000, 1)

# 도서관 객체 생성
library = Library()

print('----------------------------------------------------------------------------------------------------------')
# 책 추가
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print('----------------------------------------------------------------------------------------------------------')
# 도서관 회원 객체 생성
member1 = LibraryMember("Alice", "010-1234-5678", "2024-04-05")
member2 = LibraryMember("gyu", "010-1234-5678", "2024-04-05")
print('----------------------------------------------------------------------------------------------------------')
# 책 대출 및 정보 확인
print(library.all_books())
member1.borrowed_book(library, "Python Programming", 2)
print(library.all_books())
member1.borrowed_book(library, "Data Science Handbook", 1)
print(library.all_books())
member1.borrowed_book(library, "Machine Learning Basics", 1)
member2.borrowed_book(library, "Machine Learning Basics", 1)
#member1.borrowed_book(library, "Python", 5)
print('----------------------------------------------------------------------------------------------------------')
# 대출한 책 정보 확인
print("대출한 책 정보:")
for book, info in member1.borrowed_books.items():
    print(f"책 제목: {book}, 정보: {info}")
print('----------------------------------------------------------------------------------------------------------')

# 책 반납
member1.return_book(library, "Python Programming", 1)

print('----------------------------------------------------------------------------------------------------------')
# 반납 후 대출한 책 정보 확인
print("반납 후 대출한 책 정보:")
for book, info in member1.borrowed_books.items():
    print(f"책 제목: {book}, 정보: {info}")
print('----------------------------------------------------------------------------------------------------------')
print(library.all_books())
print('----------------------------------------------------------------------------------------------------------')
# 반납 전 예약 확인
print("반납 전 예약 목록:")
print(library.reserved_books)
print('----------------------------------------------------------------------------------------------------------')
# 책 반납
member1.return_book(library, "Machine Learning Basics", 1)
print('----------------------------------------------------------------------------------------------------------')
# 반납 후 예약 확인
print("반납 후 예약 목록:")
print(library.reserved_books)
print('----------------------------------------------------------------------------------------------------------')