class Node:
    def __init__(self, data):
        # 노드가 저장 하는 데이터
        self.data = data
        # 다음 노드에 대한 래퍼 런스
        self.next = None


# 데이터 2, 3, 5, 7, 11
head_node = Node(2)
node_1 = Node(3)
node_2 = Node(5)
node_3 = Node(7)
tail_node = Node(11)

head_node.next = node_1
node_1.next = node_2
node_2.next = node_3
node_3.next = tail_node

# 연결 리스트 출력
# iterator = head_node
# while iterator is not None:
#     print(iterator.data, end=" -> ")
#     iterator = iterator.next
# print("None")

class LinkedList:
    """링크드리스트 클래스"""

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        iterator = my_list.head
        result = ''

        while iterator is not None:
            result += str(iterator.data) + " -> "
            iterator = iterator.next
        result += "None"
        return result

    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node


my_list = LinkedList()

my_list.append(3)
my_list.append(6)
my_list.append(7)
my_list.append(13)
my_list.append(15)

print(my_list)