# 제너레이터를 사용하여 1부터 주어진 숫자까지의 자연수를 생성하는 문제

# 1부터 주어진 숫자까지의 자연수를 생성하는 제너레이터를 구현하세요.

def num_generator(n):
    for num in range(1, n+1):
        yield num

gen = num_generator(17)

for num in gen:
    print(num)