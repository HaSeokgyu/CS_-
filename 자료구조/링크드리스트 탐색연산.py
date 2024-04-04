# 탐색 연산은 자료 구조에서 원하는 조건의 데이터를 찾아내는 연산입니다.
# 링크드 리스트 탐색 연산은 특정 데이터를 갖는 노드를 리턴합니다.
# 이렇게
#
# | 2 | 3 | 5 | 7 | 11
# 링크드 리스트에 2, 3, 5, 7, 11이 저장돼 있다고 합시다. 여기서 5를 갖는 노드를 탐색하면, 링크드 리스트 안에서 5를 가지고 있는 노드를 찾아서 리턴하는 거죠.
# 배열에서 탐색 연산을 어떻게 하셨는지 기억 나시나요?
# 선형적으로 가장 앞부터 마지막 인덱스까지 돌면서 탐색을 했습니다.
# 링크드 리스트도 배열과 마찬가지로 선형 탐색을 사용합니다. 가장 앞 노드부터 끝 노드까지 돌면서 원하는 데이터를 갖는 노드를 리턴하죠.
# 이번 과제에서는 링크드 리스트의 탐색 연산을 직접 구현해 볼게요.
# 메소드 find_node_with_data는 찾으려는 데이터를 파라미터 data로 받아서 링크드 리스트 내에서 원하는 데이터를 갖고 있는 노드를 리턴합니다.
# 단, 원하는 데이터가 링크드 리스트 안에 없을 때는 None을 리턴합니다.
# 실습 결과
#
# 2
# 11
# 6을 갖는 노드는 없습니다

class Node:
    """링크드 리스트의 노드 클래스"""

    def __init__(self, data):
        self.data = data  # 실제 노드가 저장하는 데이터
        self.next = None  # 다음 노드에 대한 레퍼런스


class LinkedList:
    """링크드 리스트 클래스"""

    def __init__(self):
        self.head = None  # 링크드 리스트의 가장 앞 노드
        self.tail = None  # 링크드 리스트의 가장 뒤 노드

    def find_node_with_data(self, data):
        """링크드 리스트에서 탐색 연산 메소드. 단, 해당 노드가 없으면 None을 리턴한다"""
        # 여기에 코드를 작성하세요
        iterator = self.head

        while iterator:
            if iterator.data == data:
                return iterator
            iterator = iterator.next

        return None

    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)

        # 링크드 리스트가 비어 있으면 새로운 노드가 링크드 리스트의 처음이자 마지막 노드다
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # 링크드 리스트가 비어 있지 않으면
        else:
            self.tail.next = new_node  # 가장 마지막 노드 뒤에 새로운 노드를 추가하고
            self.tail = new_node  # 마지막 노드를 추가한 노드로 바꿔준다

    def __str__(self):
        """링크드  리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        # 링크드  리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        # 링크드  리스트 끝까지 돈다
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            res_str += " {} |".format(iterator.data)
            iterator = iterator.next  # 다음 노드로 넘어간다

        return res_str


# 새로운 링크드 리스트 생성
linked_list = LinkedList()

# 여러 데이터를 링크드 리스트 마지막에 추가
linked_list.append(2)
linked_list.append(3)
linked_list.append(5)
linked_list.append(7)
linked_list.append(11)

# 데이터 2를 갖는 노드 탐색
node_with_2 = linked_list.find_node_with_data(2)

if not node_with_2 is None:
    print(node_with_2.data)
else:
    print("2를 갖는 노드는 없습니다")

# 데이터 11을 갖는 노드 탐색
node_with_11 = linked_list.find_node_with_data(11)

if not node_with_11 is None:
    print(node_with_11.data)
else:
    print("11을 갖는 노드는 없습니다")

# 데이터 6 갖는 노드 탐색
node_with_6 = linked_list.find_node_with_data(6)

if not node_with_6 is None:
    print(node_with_6.data)
else:
    print("6을 갖는 노드는 없습니다")

