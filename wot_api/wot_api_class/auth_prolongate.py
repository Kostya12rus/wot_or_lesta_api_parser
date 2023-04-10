class AuthProlongateClass:
    def __init__(self, auth_prolongate_data: dict):
        if not auth_prolongate_data: auth_prolongate_data = {}
        self._auth_prolongate: dict = auth_prolongate_data
        self.access_token: str = auth_prolongate_data.get('access_token', '')
        self.account_id: int = auth_prolongate_data.get('account_id', 0)
        self.expires_at: int = auth_prolongate_data.get('expires_at', 0)

