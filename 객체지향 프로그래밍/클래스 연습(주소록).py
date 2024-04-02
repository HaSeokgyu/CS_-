# 주소록을 관리하는 클래스를 작성하세요. 이 클래스는 다음과 같은 기능을 제공해야 합니다:
#
# 속성 (Attributes):
# contacts: 주소록에 저장된 연락처 정보를 담은 딕셔너리. 키(key)는 이름, 값(value)은 연락처 정보를 나타내는 딕셔너리입니다. 연락처 정보에는 전화번호(phone), 이메일(email), 주소(address) 등이 포함됩니다.

# 메서드 (Methods):
# __init__() 메서드: 주소록 객체를 생성하고, 초기 연락처 정보를 빈 딕셔너리로 초기화합니다.
# add_contact(name, phone, email, address) 메서드: 주어진 이름과 연락처 정보를 주소록에 추가합니다.
# remove_contact(name) 메서드: 주어진 이름의 연락처 정보를 주소록에서 제거합니다.
# get_contact(name) 메서드: 주어진 이름의 연락처 정보를 반환합니다.
# get_all_contacts() 메서드: 주소록에 저장된 모든 연락처 정보를 반환합니다.

class AddressBook:
    """ 주소록 클래스 """

    def __init__(self) -> None:
        """ 주소록 객체 생성 - 초기 연락처 정보는 빈 딕셔너리로 """
        self.contacts = {}

    def add_contact(self, name : str, phone : str, email : str, address : str) -> None:
        """ 주소록 생성 메서드 """
        self.contacts[name] = {'phone' : phone, 'email' : email, 'address' : address}

    def remove_contact(self, name : str):
        """ 주소록 삭제 메서드 """
        if name in self.contacts:
            self.contacts.pop(name)
        else:
            raise ValueError('해당 이름이 없습니다.')

    def get_contact(self, name : str):
        """ 주소록 정보 가져오기 메서드 """
        if name in self.contacts:
            return self.contacts[name]
        else:
            raise ValueError('해당 이름이 없습니다.')

    def get_all_contacts(self):
        """ 주소록의 모든 연락처 정보를 반환하는 메서드 """
        return self.contacts

help(AddressBook)

address_book = AddressBook()
address_book.add_contact("John", "123-456-7890", "john@example.com", "123 Main St")
address_book.add_contact("Alice", "987-654-3210", "alice@example.com", "456 Oak Ave")

print(address_book.get_all_contacts())

print(address_book.get_contact("John"))

address_book.remove_contact("Alice")
print(address_book.get_all_contacts())

address_book.remove_contact("Park")

# ChatGPT 평가
# 주어진 코드에는 대부분의 요구사항이 충족되었으며, 적절한 예외 처리와 메서드 반환 타입 힌트가 추가되었습니다. 또한 주석도 제대로 작성되어 가독성이 향상되었습니다. 따라서 만점에 가까운 점수를 부여할 수 있습니다.
#
# 다음은 점수 평가 기준입니다:
#
# 주어진 요구사항 충족: 모든 요구사항이 충족되었습니다. 주어진 속성과 메서드가 모두 구현되었으며, 주소록에 연락처를 추가, 제거하고 조회하는 기능이 제대로 작동합니다. (점수: 10/10)
# 예외 처리: 적절한 예외 처리가 구현되었습니다. 주소록에 존재하지 않는 연락처를 조회하거나 제거할 때 예외가 발생하고, 이 예외 메시지가 적절하게 출력됩니다. (점수: 2/2)
# 메서드 반환 타입 힌트: 모든 메서드에는 적절한 반환 타입 힌트가 추가되었습니다. 이는 코드의 가독성과 유지보수성을 향상시킵니다. (점수: 2/2)
# 주석: 클래스와 각 메서드에는 적절한 주석이 포함되어 있습니다. 이는 코드를 이해하는 데 도움이 되며, 유지보수에 도움이 됩니다. (점수: 1/1)
# 따라서 총 점수는 15점입니다.

