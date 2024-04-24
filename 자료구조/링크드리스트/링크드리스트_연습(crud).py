# 링크드리스트 연습 (CRUD)


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f'{self.data} -> '

class LinkedList:
    """ 링크드 리스트 클래스 """

    def __init__(self):
        self.head = None
        self.tail = None

    def create(self, data):
        """ 링크드리스트 추가 연산 메소드 """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def read(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next

    def get_node_at_index(self, index):
        """ 주어진 인덱스에 해당하는 노드 반환 """
        current = self.head
        count = 0
        while current:
            if count == index:
                return current
            current = current.next
            count += 1
        return None  # 인덱스가 범위를 벗어나면 None 반환


    def update(self, index, data):
        node = self.head
        count = 0
        while node:
            if index == count:
                print(f'인덱스 {index}의 노드 값을 {data}로 수정중입니다.')
                node.data = data
                print(f'노드가 {data}로 수정되었습니다.')
                return  # 갱신이 완료되면 함수 종료
            node = node.next
            count += 1

        # 반복문이 종료되면 인덱스가 범위를 벗어난 것임을 알 수 있음
        print('범위를 벗어난 인덱스입니다. 다시 시도해주세요.')

    def delete(self, index):
        if index == 0:
            if self.head:
                self.head = self.head.next
                if self.head is None:
                    self.tail = None
        else:
            prev = self.get_node_at_index(index - 1)
            if prev and prev.next:
                prev.next = prev.next.next
                if prev.next is None:
                    self.tail = prev
            else:
                print("인덱스가 범위를 벗어납니다.")




# 새로운 링크드 리스트 생성
my_list = LinkedList()

my_list.create(2)
my_list.create(3)
my_list.create(5)
my_list.create(7)
my_list.create(11)

my_list.read()

my_list.update(2,4)

my_list.read()

my_list.delete(2)

my_list.read()