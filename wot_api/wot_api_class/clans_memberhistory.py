class ClansMemberhistoryClass:
    def __init__(self, clans_memberhistory_data: dict):
        if not clans_memberhistory_data: clans_memberhistory_data = {}
        self._clans_memberhistory: dict = clans_memberhistory_data
        self.account_id: int = clans_memberhistory_data.get('account_id', 0)
        self.clan_id: int = clans_memberhistory_data.get('clan_id', 0)
        self.joined_at: int = clans_memberhistory_data.get('joined_at', 0)
        self.left_at: int = clans_memberhistory_data.get('left_at', 0)
        self.role: str = clans_memberhistory_data.get('role', '')

