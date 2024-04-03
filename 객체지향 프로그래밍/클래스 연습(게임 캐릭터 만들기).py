# 한국의 최대 온라인 게임업체 넥손에서 일하는 대위는 최근 새 프로젝트인 '은행스토리'에 개발자로 참여하게 되었는데요. 대위가 맡은 부분은 게임 캐릭터를 '클래스'로 작성하는 것입니다. 이미 객체의 속성과 행동을 어떻게 할지에 대해서는 생각을 마친 상태입니다.
# 다음 조건들과 출력 예시에 맞게 GameCharacter 클래스를 작성하세요.
# 인스턴스 변수(타입)
# name(문자열): 캐릭터의 이름
# hp(숫자형): 캐릭터의 체력
# power(숫자형): 캐릭터의 공격력
# 인스턴스 메소드
# __init__: 사용할 모든 인스턴스 변수를 설정한다.
# is_alive: 게임 캐릭터의 체력이 0보다 큰지(살았는지 죽었는지) 확인한다.
# 0 초과이면 True를, 0 이하라면 False를 리턴한다.
# get_attacked: 게임 캐릭터의 체력이 0보다 큰 상태라면 파라미터로 받은 공격력만큼 체력을 깎는다.
# 조건:
# is_alive 메소드를 사용해서 인스턴스가 살아있을 때만 체력을 깎는다. 이미 캐릭터가 죽었으면 죽었다는 메시지를 출력한다.
# 남은 체력보다 공격력이 더 크면 체력(hp)을 0으로 설정한다.
# attack: 파라미터로 받은 다른 캐릭터의 체력을 자신의 공격력만큼 깎는다.
# 조건:
# is_alive 메소드를 이용해서 살아있는 인스턴스만 공격을 할 수 있도록 한다.
# get_attacked 메소드를 사용한다.
# __str__: 게임 캐릭터의 의미 있는 정보를 포함한 문자열을 리턴한다.

class GameCharacter:
    # 게임 캐릭터 클래스
    def __init__(self, name, hp, power):
        # 게임 캐릭터는 속성으로 이름, hp, 공격력을 갖는다
        self.name = name
        self.hp = hp
        self.power = power

    def is_alive(self):
        # 게임 캐릭터가 살아있는지(체력이 0이 넘는지) 확인하는 메소드
        if self.hp <= 0:
            return False
        else:
            return True

    def get_attacked(self, damage):
        """
        게임 캐릭터가 살아있으면 공격한 캐릭터의 공격력만큼 체력을 깎는 메소드
        조건:
            1. 이미 캐릭터가 죽었으면 죽었다는 메시지를 출력한다
            2. 남은 체력보다 공격력이 더 크면 체력은 0이 된다.
        """
        if self.is_alive():
            self.hp -= damage
            if self.hp < damage:
                self.hp = 0

    def attack(self, other_character):
        # 게임 캐릭터가 살아있으면 파라미터로 받은 다른 캐릭터의 체력을 자신의 공격력만큼 깎는다
        if other_character.is_alive():
            other_character.get_attacked(self.power)
        else:
            print(f'{other_character.name}님은 이미 죽었습니다.')

    def __str__(self):
        # 게임 캐릭터의 의미있는 정보를 포함한 문자열을 리턴한다
        return f'{self.name}님의 hp는 {self.hp}만큼 남았습니다.'


# 게임 캐릭터 인스턴스 생성
character_1 = GameCharacter("Ww영훈전사wW", 200, 30)
character_2 = GameCharacter("Xx지웅최고xX", 100, 50)

# 게임 캐릭터 인스턴스들 서로 공격
character_1.attack(character_2)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)

# 게임 캐릭터 인스턴스 출력
print(character_1)
print(character_2)