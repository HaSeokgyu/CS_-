# 문제: 주어진 문자열을 받아 각 문자를 하나씩 생성하는 제너레이터를 구현하세요.

def str_generator(str : str):
    for word in str:
        yield word

test = str_generator('wordesg')

for word in test:
    print(word)