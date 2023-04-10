class AuthLogoutClass:
    def __init__(self, auth_logout_data: dict):
        if not auth_logout_data: auth_logout_data = {}
        self._auth_logout: dict = auth_logout_data

