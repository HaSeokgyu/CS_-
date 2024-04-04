# class User:
#     def __init__(self, name, email, password):
#         self.name = name
#         self.email = email
#         self.password = password
# 그리고 아래와 같이 서로 다른 형태의 정보를 갖고 유저 인스턴스를 만들어야 한다면?
#
# info_string = "강영훈,younghoon@codeit.kr,123456"
# info_list = ["이윤수", "yoonsoo@codeit.kr", "abcdef"]
# 문자열은 쉼표(,)를 기준으로 분리하면 되겠고, 리스트는 각 인덱스의 요소를 가져오면 되겠죠?
# 아래 코드를 볼까요?
# 다양한 형태의 정보로 유저 인스턴스 만들기
#
# # 유저 인스턴스 만들기 (1): 문자열로 인스턴스 만들기
# parameter_list = info_string.split(",") # split 메소드를 사용해서 쉼표(,)를 기준으로 문자열을 리스트로 분리한다
#
# # 각 변수에 분리된 문자열 각각 저장
# younghoon_name = parameter_list[0]
# younghoon_email = parameter_list[1]
# younghoon_password = parameter_list[2]
#
# younghoon = User(younghoon_name, younghoon_email, younghoon_password)
#
# # 유저 인스턴스 만들기 (2): 리스트로 인스턴스 만들기
# yoonsoo_name = info_list[0]
# yoonsoo_email = info_list[1]
# yoonsoo_password = info_list[2]
#
# yoonsoo = User(yoonsoo_name, yoonsoo_email, yoonsoo_password)
#
# # 인스턴스가 제대로 생성되었는지 확인
# print(younghoon.name, younghoon.email, younghoon.password)
# print(yoonsoo.name, yoonsoo.email, yoonsoo.password)
# 실습 결과
#
# 강영훈 younghoon@codeit.kr 123456
# 이윤수 yoonsoo@codeit.kr abcdef
# 서로 다른 형태의 정보를 갖고도 User 인스턴스를 만들 수 있죠? 하지만 코드가 너무 깁니다.
# 이럴 때 User 클래스에 클래스 메소드를 두고 사용하면 훨씬 깔끔한 코드로 인스턴스를 생성할 수 있는데요. User 클래스의 클래스 메소드 from_string 과 from_list의 내용을 채워 봅시다.

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    @classmethod
    def from_string(cls, string_params):
        # 여기에 코드를 작성하세요
        params_list = string_params.split(",")
        name = params_list[0]
        email = params_list[1]
        password = params_list[2]
        return cls(name, email, password)

    @classmethod
    def from_list(cls, list_params):
        # 여기에 코드를 작성하세요
        name = list_params[0]
        email = list_params[1]
        password = list_params[2]
        return cls(name, email, password)

# 유저 생성 및 초기값 설정
younghoon = User.from_string("강영훈,younghoon@codeit.kr,123456")
yoonsoo = User.from_list(["이윤수", "yoonsoo@codeit.kr", "abcdef"])

print(younghoon.name, younghoon.email, younghoon.password)
print(yoonsoo.name, yoonsoo.email, yoonsoo.password)