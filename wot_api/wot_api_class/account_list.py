class AccountListClass:
    def __init__(self, account_list_data: dict):
        if not account_list_data: account_list_data = {}
        self._account_list: dict = account_list_data
        self.account_id: int = account_list_data.get('account_id', 0)
        self.nickname: str = account_list_data.get('nickname', '')

