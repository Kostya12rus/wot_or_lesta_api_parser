class TanksAchievementsClass:
    def __init__(self, tanks_achievements_data: dict):
        if not tanks_achievements_data: tanks_achievements_data = {}
        self._tanks_achievements: dict = tanks_achievements_data
        self.account_id: int = tanks_achievements_data.get('account_id', 0)
        self.achievements: dict = tanks_achievements_data.get('achievements', {})
        self.max_series: dict = tanks_achievements_data.get('max_series', {})
        self.series: dict = tanks_achievements_data.get('series', {})
        self.tank_id: int = tanks_achievements_data.get('tank_id', 0)

