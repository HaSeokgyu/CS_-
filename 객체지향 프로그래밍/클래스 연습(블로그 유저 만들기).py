# 프로그래밍에 관심이 많은 영준이는 여러 사람들이 자신의 글을 올릴 수 있는 블로그를 만들려고 합니다. 영준이는 일단 아래와 같이 게시글을 나타내는 Post 클래스를 정의했습니다.

# class Post:
#     # 게시글 클래스
#     def __init__(self, date, content):
#         # 게시글은 속성으로 작성 날짜와 내용을 갖는다
#         self.date = date
#         self.content = content
#
#     def __str__(self):
#         # 게시글의 정보를 문자열로 리턴하는 메소드
#         return "게시일: {}\n내용: {}".format(self.date, self.content)

# 이제 블로그 유저를 나타내는 클래스를 정의해 볼까요? 다음 조건들과 출력 예시를 보고 BlogUser 클래스를 정의해 보세요.
# 인스턴스 변수(타입)
# name(문자열): 블로그 사용자의 이름
# posts(리스트): 블로그 게시글들을 담을 리스트
# 메소드
# __init__: 인스턴스 변수가 설정되는 메소드
# add_post: 블로그 사용자의 블로그 게시글 리스트에 새로운 게시글 인스턴스를 추가하는 메소드
# show_all_posts: 블로그 사용자가 올린 모든 게시글을 출력하는 메소드
# __str__: 블로그 사용자의 간단한 인사와 이름을 문자열로 리턴하는 메소드

class Post:
    # 게시글 클래스
    def __init__(self, date, content):
        # 게시글은 속성으로 작성 날짜와 내용을 갖는다
        self.date = date
        self.content = content

    def __str__(self):
        # 게시글의 정보를 문자열로 리턴하는 메소드
        return "작성 날짜: {}\n내용: {}".format(self.date, self.content)


class BlogUser:
    # 블로그 유저 클래스
    def __init__(self, name):
        """
        블로그 유저는 속성으로 이름, 게시글들을 갖는다
        posts는 빈 배열로 초기화한다
        """
        self.name = name
        self.posts = []

    def add_post(self, date, content):
        # 새로운 게시글 추가
        self.posts.append(Post(date, content))

    def show_all_posts(self):
        # 블로그 유저의 모든 게시글 출력
        for post in self.posts:
            print(post)

    def __str__(self):
        # 간단한 인사와 이름을 문자열로 리턴
        return f'안녕하세요 {self.name}입니다.\n'


# 블로그 유저 인스턴스 생성
blog_user_1 = BlogUser("성태호")

# 블로그 유저 인스턴스 출력(인사, 이름)
print(blog_user_1)

# 블로그 유저 게시글 2개 추가
blog_user_1.add_post("2019년 8월 30일", """
오늘은 내 생일이었다.
많은 사람들이 축하해줬다.
행복했다.
""")

blog_user_1.add_post("2019년 8월 31일", """
재밌는 코딩 교육 사이트를 찾았다.
코드잇이란 곳인데 최고다.
같이 공부하실 분들은 www.codeit.kr로 오세요!
""")

# 블로그 유저의 모든 게시글 출력
blog_user_1.show_all_posts()