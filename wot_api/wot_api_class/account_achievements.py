class AccountAchievementsClass:
    def __init__(self, account_achievements_data: dict):
        if not account_achievements_data: account_achievements_data = {}
        self._account_achievements: dict = account_achievements_data
        self.achievements: dict = account_achievements_data.get('achievements', {})
        self.frags: dict = account_achievements_data.get('frags', {})
        self.max_series: dict = account_achievements_data.get('max_series', {})

