# 은행 계좌 클래스 (BankAccount Class) 설계

# BankAccount 클래스 작성
# BankAccount 클래스는 다음과 같은 속성을 가집니다:
# 계좌 번호(account_number)
# 예금주(owner)
# 잔액(balance)
# 입금(amount)과 출금(amount)을 처리하는 deposit()과 withdraw() 메서드 구현
# 계좌 정보를 출력하는 display_info() 메서드 구현

class BankAccount:
    """은행 계좌 클래스"""
    def __init__(self, account_number : str, owner : str, balance : int) -> None:
        """ account_nubmer = 은행계좌번호 / owner = 예금주명 / balance = 잔액 """
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, desposit_account : int):
        """ 입금 메서드 / desposit_account = 입금할 잔액"""
        transaction = AccountTransaction()
        transaction.deposit(self, desposit_account)

    def withdraw(self, withdraw_account : int):
        """ 출금 메서드 / withdraw_account = 출금할 잔액"""
        transaction = AccountTransaction()
        transaction.withdraw(self, withdraw_account)

    def display_info(self):
        """ 계좌 정보 출력 메서드 """
        print(f'계좌 번호 : {self.account_number}\n예금주 : {self.owner}\n잔액 : {self.balance}')


class AccountTransaction:
    """ 은행계좌 거래 처리 클래스 """
    def deposit(self, owner_account : str, deposit_account : int):
        """ 입금 메서드 / owner_account = BankAccount 인스턴스 / desposit_account = 입금할 잔액 """
        owner_account.balance = owner_account.balance + deposit_account
        return print(f'{owner_account.owner}님의 계좌에 {deposit_account}원이 정상적으로 입금되었습니다. \n현재 잔액 : {owner_account.balance}')

    def withdraw(self, owner_account : str, withdraw_account : int):
        """ 출금 메서드 / owner_account = BankAccount 인스턴스 / withdraw_account = 출금할 잔액 """
        if owner_account.balance < withdraw_account :
            print(f'잔액이 부족하여 출금할 수 없습니다. \n현재 잔액 : {owner_account.balance}')
        else:
            owner_account.balance = owner_account.balance - withdraw_account
            return print(f'{owner_account.owner}님의 계좌에서 {withdraw_account}원이 정상적으로 출금되었습니다. \n현재 잔액 : {owner_account.balance}')

help(BankAccount)
help(AccountTransaction)
account = BankAccount('123123-123-123','하석규',5000)
account.display_info()
account.deposit(10000)
account.withdraw(15000)
account.withdraw(20000)

# ChatGPT 평가
# 전체적인 평가:
# 코드는 은행 계좌와 관련된 기능을 잘 구현하고 있으며, 가독성이 좋고 각 기능이 명확하게 분리되어 있습니다. 입금과 출금 기능은 예상대로 작동하며, 잔액 부족 등의 예외 상황에 대한 처리도 충분히 고려되어 있습니다. 하지만 몇 가지 개선점이 있을 수 있습니다:
#
# AccountTransaction 클래스의 메서드에서 owner_account 파라미터는 BankAccount 객체를 기대하는데, 현재는 문자열로 타입 힌트가 되어있습니다. 이를 BankAccount로 수정하는 것이 좋습니다.
# 입금 및 출금 기능을 처리하는 메서드에서 출력문이 직접 호출되는 것보다는 예외를 발생시키는 것이 더 나을 수 있습니다. 예외를 발생시키면 사용자가 상황을 더 명확하게 이해할 수 있고, 다른 부분에서 예외를 잘 처리할 수 있습니다.
# 이러한 개선점을 고려하여 코드를 조금 더 발전시킬 수 있을 것입니다. 이 코드에 대한 점수는 8.5/10 입니다. 개선점을 고려하여 좀 더 완벽한 코드를 작성해보세요!