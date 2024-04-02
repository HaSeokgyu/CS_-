# 속성 (Attributes):
#
# items: 자판기에 있는 상품들과 그들의 재고를 나타내는 딕셔너리. 키(key)는 상품명, 값(value)은 상품의 가격과 재고 수량을 나타내는 튜플입니다.
# 예시: {'음료수': (1000, 5), '과자': (500, 10), '아이스크림': (1500, 3)}
# 메서드 (Methods):
#
# __init__() 메서드: 초기 상품과 재고를 입력받아 새로운 자판기 객체를 생성합니다.
# add_item(name, price, quantity) 메서드: 새로운 상품을 자판기에 추가합니다.
# remove_item(name) 메서드: 주어진 상품을 자판기에서 제거합니다.
# purchase_item(name, quantity) 메서드: 주어진 상품을 지정된 수량만큼 구매합니다. 구매한 상품의 총 가격을 반환합니다.
# display_items() 메서드: 현재 자판기에 있는 상품들과 재고를 출력합니다.
# 주의:
#
# 재고가 없는 상품은 구매할 수 없습니다. 재고가 충분하지 않으면 "재고가 부족합니다"라는 메시지를 출력하세요.
# 상품을 제거할 때는 해당 상품이 자판기에 있는지 먼저 확인하세요.

class VendingMachine:
    """ 자판기 클래스 """

    def __init__(self, items : dict) -> None:
        self.items = items

    def add_item(self, name : str, price : int, quantity : int) -> None:
        """ 자판기 제품 추가 메서드 """
        self.items[name] = (price, quantity)

    def remove_item(self, name : str):
        """ 자판기 제품 삭제 메서드 """
        if name in self.items:
            self.items.pop(name)
        else:
            raise ValueError(f"{name}은 제품 목록에 없습니다.")

    def purchase_item(self, name : str, quantity : int):
        """ 자판기 제품 구매 메서드 """
        if name in self.items:
            price, stock = self.items[name]
            if quantity <= stock:
                total_price = price * quantity
                self.items[name] = (price, stock - quantity)
                return total_price
            else:
                raise ValueError(f"{name}제품은 {stock}개까지 구매 가능합니다.")
        else:
            raise ValueError(f"{name}제품은 자판기에 없습니다.")

    def display_items(self : dict):
        """ 자판기 제품 정보 반환 메서드 """
        for item, (price, quantity) in self.items.items():
            print(f'{item} - 가격 : {price}원, 재고 : {quantity}개')


help(VendingMachine)
vending_machine = VendingMachine({'음료수': (1000, 5), '과자': (500, 10), '아이스크림': (1500, 3)})
vending_machine.add_item('커피', 1200, 8)
vending_machine.display_items()
# 출력:
# 음료수 - 가격: 1000원, 재고: 5개
# 과자 - 가격: 500원, 재고: 10개
# 아이스크림 - 가격: 1500원, 재고: 3개
# 커피 - 가격: 1200원, 재고: 8개

vending_machine.remove_item('아이스크림')
vending_machine.display_items()
# 출력:
# 음료수 - 가격: 1000원, 재고: 5개
# 과자 - 가격: 500원, 재고: 10개
# 커피 - 가격: 1200원, 재고: 8개

vending_machine.purchase_item('음료수', 3)  # 출력: 3000
vending_machine.display_items()
# 출력:
# 음료수 - 가격: 1000원, 재고: 2개
# 과자 - 가격: 500원, 재고: 10개
# 커피 - 가격: 1200원, 재고: 8개

vending_machine.purchase_item('과자', 20)  # 출력: "재고가 부족합니다"

# ChatGPT 평
# 코드를 확인해보겠습니다.
#
# __init__() 메서드가 정의된 대로 자판기 객체가 생성되었습니다.
# add_item() 메서드를 사용하여 새로운 상품이 자판기에 추가되었습니다.
# display_items() 메서드가 자판기에 있는 상품들과 재고를 올바르게 출력했습니다.
# remove_item() 메서드를 사용하여 주어진 상품이 자판기에서 제거되었습니다.
# purchase_item() 메서드를 사용하여 상품을 지정된 수량만큼 구매했으며, 구매한 상품의 총 가격이 반환되었습니다.
# 코드가 모든 요구 사항을 만족하며 예상된 출력을 제공했습니다. 따라서 코드에 만점을 주겠습니다. 👍

# 몰랐던 점

# for item, (price, quantity) in self.items.items()
# self.items -> 딕셔너리 자체 / self.items.items() 딕셔너리의 키-값 쌍을 반환
