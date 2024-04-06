# 문제: 주어진 리스트에서 중복된 요소를 제외하고 유일한 값만 생성하는 제너레이터를 구현하세요.

def list_generator(list : list):
    list = set(list)
    for word in list:
        yield word

test = list_generator(['as','as','ds','ds','d','e','g'])

for word in test:
    print(word)


# GPT 답안

def unique_elements_generator(input_list):
    seen = set()
    for element in input_list:
        if element not in seen:
            seen.add(element)
            yield element

test = unique_elements_generator(['as', 'as', 'ds', 'ds', 'd', 'e', 'g'])

for element in test:
    print(element)
