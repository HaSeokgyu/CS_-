# 시나리오: 주소록 관리 프로그램
#
# 주제: 연결 리스트를 사용하여 주소록을 관리하는 프로그램을 구현합니다.
#
# 시나리오 설명:
# 이 프로그램은 사용자가 개인 및 회사의 연락처 정보를 저장하고 관리하는 데 사용됩니다. 프로그램은 각 연락처의 이름, 전화번호, 이메일 주소 등의 정보를 저장하고 이를 검색, 추가, 수정, 삭제하는 기능을 제공합니다.
#
# 주요 기능:
#
# 연락처 추가: 새로운 연락처 정보를 주소록에 추가합니다.
# 연락처 검색: 주소록에서 특정 이름을 가진 연락처를 검색합니다.
# 연락처 수정: 주소록에 저장된 연락처의 정보를 수정합니다.
# 연락처 삭제: 주소록에서 특정 연락처를 삭제합니다.
# 전체 주소록 표시: 주소록에 저장된 모든 연락처 정보를 표시합니다.

class Contact:
    """ 연락처 클래스 """

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        self.next_contact = None

class AddressBook:
    """ 주소록 클래스 """

    count = 0

    def __init__(self):
        self.head = None

    @classmethod
    def cls_count_view(cls):
        return AddressBook.count

    def add_contact(self, name, phone, email):
        """ 연락처 추가 """
        AddressBook.count += 1
        new_contact = Contact(name, phone, email)
        if not self.head:
            self.head = new_contact
        else:
            current_contact = self.head
            while current_contact.next_contact:
                current_contact = current_contact.next_contact
            current_contact.next_contact = new_contact

    def display_contacts(self):
        """ 주소록 표시 """
        current_contact = self.head
        while current_contact:
            print(f'이름 : {current_contact.name}\n전화번호 : {current_contact.phone}\n이메일 : {current_contact.email}\n')
            current_contact = current_contact.next_contact


# 예시: 주소록 생성 및 사용
address_book = AddressBook()
address_book.add_contact("John Doe", "123-456-7890", "john@example.com")
address_book.add_contact("Jane Smith", "987-654-3210", "jane@example.com")
address_book.add_contact("Alice", "111-222-3333", "alice@example.com")

print(f'전체 연락처는 총 {address_book.cls_count_view()}개 입니다.')

print("전체 연락처:")
address_book.display_contacts()


