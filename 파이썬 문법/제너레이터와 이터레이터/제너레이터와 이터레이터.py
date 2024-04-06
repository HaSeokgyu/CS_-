# 제너레이터(generator)와 이터레이터(iterator)는 파이썬에서 메모리를 효율적으로 사용하면서 데이터를 처리할 수 있는 강력한 도구입니다.
#
# 1. 제너레이터(generator):
# 제너레이터는 이터레이터를 생성하는 함수입니다. 제너레이터를 만들 때는 일반 함수와 비슷하게 정의하지만, return 대신에 yield 문을 사용합니다.
# 이 yield 문은 제너레이터가 값을 반환하고 실행 상태를 일시 중지하며, 다음 호출에서 중지된 지점부터 실행을 재개합니다.
# 이러한 특징으로 인해 제너레이터는 큰 데이터셋을 처리할 때 메모리를 효율적으로 사용할 수 있습니다.

def square_generator(n):
    for i in range(1, n + 1):
        yield i ** 2

# 제너레이터를 호출하여 값을 생성합니다.
gen = square_generator(5)

# 제너레이터를 이터레이션하면서 값을 출력합니다.
for num in gen:
    print(num)

# 위의 코드에서 square_generator 함수는 제너레이터를 생성합니다.
# 이 함수는 1부터 n까지의 제곱을 순차적으로 생성하며, yield 문을 통해 값을 반환합니다.
# 그리고 이 값을 for 루프를 통해 순차적으로 출력할 수 있습니다.
#
# 제너레이터를 사용하면 반복 가능한 객체를 생성할 때 일반적인 반복자(iterator)보다 간결하고 메모리 효율적으로 작성할 수 있습니다.
# 이를 통해 대용량 데이터 처리와 같은 작업을 더욱 효율적으로 처리할 수 있습니다.

# 일반적인 방법 (리스트 사용)

import time

start_time = time.time()

numbers = list(range(1, 1000001))
squared_numbers = [x ** 2 for x in numbers]

end_time = time.time()

print("메모리 사용량(대략적인 평가):", len(numbers) * 4 + len(squared_numbers) * 8, "bytes")  # 각 숫자는 4바이트, 각 제곱값은 8바이트
print("실행 시간:", end_time - start_time, "초")

# 제너레이터 및 이터레이터 사용

import time

def squared_generator(n):
    for i in range(1, n + 1):
        yield i ** 2

start_time = time.time()

gen = squared_generator(1000000)
squared_numbers = list(gen)

end_time = time.time()

print("메모리 사용량(대략적인 평가):", len(squared_numbers) * 8, "bytes")  # 각 제곱값은 8바이트
print("실행 시간:", end_time - start_time, "초")
