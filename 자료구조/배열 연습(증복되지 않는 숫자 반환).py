# 문제: 정수로 이루어진 배열이 주어졌을 때, 해당 배열에서 중복되지 않는(unique) 숫자들의 개수를 반환하는 함수를 작성하세요.
#
# 예를 들어, [3, 7, 2, 9, 3, 1, 7] 배열이 주어졌을 때, 중복되지 않는 숫자들은 [2, 9, 1] 이며, 따라서 함수는 3을 반환해야 합니다.

def unique_num(num_list : list):
    unique_list = []
    for num in num_list:
        if num in unique_list:
            unique_list.remove(num)
        else:
            unique_list.append(num)
    return len(unique_list)

num = [3, 7, 2, 9, 3, 1, 7]

print(unique_num(num))

# ChatGPT 평

# 코드가 중복된 숫자들의 개수가 아닌 중복되지 않는(unique) 숫자들의 개수를 반환해야 합니다. 코드의 결과는 올바르게 나오지만, 함수 이름과 문제 설명이 일치하지 않습니다. 함수 이름을 더 명확하게 바꾸는 것이 좋습니다.
# 중복을 확인하기 위해 리스트를 사용하고 있지만, in 연산과 remove 메서드를 사용하여 중복된 요소를 제거하고 있습니다. 이 방법은 비효율적일 수 있습니다. 중복을 확인하고 제거하는 과정에서 선형 시간이 소요되기 때문입니다.
# 새로운 리스트를 만들어 중복을 확인하는 대신, 딕셔너리를 사용하여 중복을 확인하고 중복되지 않는(unique) 숫자들을 추적할 수 있습니다. 딕셔너리의 키를 사용하여 중복된 숫자를 식별할 수 있습니다.
# 개선된 코드는 다음과 같습니다:
#
# python
# Copy code
# def count_unique_numbers(num_list: list):
#     unique_nums = {}
#     for num in num_list:
#         unique_nums[num] = unique_nums.get(num, 0) + 1
#     return len(unique_nums)
#
# num = [3, 7, 2, 9, 3, 1, 7]
# print(count_unique_numbers(num))
# 이 코드는 딕셔너리를 사용하여 중복되지 않는(unique) 숫자들을 효율적으로 추적하고, 딕셔너리의 키들의 개수를 반환하여 중복되지 않는 숫자들의 개수를 계산합니다.
#
# 이 코드에 대한 점수는 4점입니다. 주어진 문제를 해결하고, 중복되지 않는 숫자들의 개수를 정확하게 계산하는데 성공했습니다. 그러나 함수 이름이 문제 설명과 일치하지 않고, 더 효율적인 알고리즘을 사용하지 않았습니다.