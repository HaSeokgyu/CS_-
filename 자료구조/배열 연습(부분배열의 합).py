# 문제: 정수로 이루어진 배열이 주어졌을 때, 배열 내에서 연속된 부분 배열(subarray)의 합 중 가장 큰 값을 찾는 함수를 작성하세요.
#
# 예를 들어, [1, -3, 5, -2, 9, -8, -6, 4] 배열이 주어졌을 때, 가장 큰 연속된 부분 배열의 합은 [5, -2, 9] 부분 배열의 합인 12입니다. 따라서 함수는 12를 반환해야 합니다.
#
# 이 문제를 해결하기 위한 함수를 작성해 보세요. 필요하다면 파이썬 리스트 관련 메서드나 다른 자료구조를 사용할 수 있습니다. 해결책을 작성하고 싶다면 알려주세요!

def max_subarray_sum(num_list: list):
    max_sum = float('-inf')  # 가장 작은 값을 초기값으로 설정
    current_sum = 0
    subarray = []

    for num in num_list:
        current_sum += num

        # 현재 합계와 현재 요소 중 더 큰 값을 선택하여 subarray 갱신
        if num > current_sum:
            subarray = [num]
            current_sum = num
        else:
            subarray.append(num)

        # 최대 합계 갱신
        max_sum = max(max_sum, current_sum)

    return max_sum, subarray

test = [1, -3, 5, -2, 9, -8, -6, 4]

print(max_subarray_sum(test))