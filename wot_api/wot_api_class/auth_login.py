class AuthLoginClass:
    def __init__(self, auth_login_data: dict):
        if not auth_login_data: auth_login_data = {}
        self._auth_login: dict = auth_login_data
        self.location: str = auth_login_data.get('location', '')

