class PrivateClass:
    def __init__(self, private_data: dict):
        if not private_data: private_data = {}
        self._private: dict = private_data
        self.daily_wage: int = private_data.get('daily_wage', 0)
        self.influence: int = private_data.get('influence', 0)

class RatingsClass:
    def __init__(self, ratings_data: dict):
        if not ratings_data: ratings_data = {}
        self._ratings: dict = ratings_data
        self.elo_10: int = ratings_data.get('elo_10', 0)
        self.elo_6: int = ratings_data.get('elo_6', 0)
        self.elo_8: int = ratings_data.get('elo_8', 0)
        self.updated_at: int = ratings_data.get('updated_at', 0)

class StatisticsClass:
    def __init__(self, statistics_data: dict):
        if not statistics_data: statistics_data = {}
        self._statistics: dict = statistics_data
        self.battles: int = statistics_data.get('battles', 0)
        self.battles_10_level: int = statistics_data.get('battles_10_level', 0)
        self.battles_6_level: int = statistics_data.get('battles_6_level', 0)
        self.battles_8_level: int = statistics_data.get('battles_8_level', 0)
        self.captures: int = statistics_data.get('captures', 0)
        self.losses: int = statistics_data.get('losses', 0)
        self.provinces_count: int = statistics_data.get('provinces_count', 0)
        self.wins: int = statistics_data.get('wins', 0)
        self.wins_10_level: int = statistics_data.get('wins_10_level', 0)
        self.wins_6_level: int = statistics_data.get('wins_6_level', 0)
        self.wins_8_level: int = statistics_data.get('wins_8_level', 0)

class GlobalmapClaninfoClass:
    def __init__(self, globalmap_claninfo_data: dict):
        if not globalmap_claninfo_data: globalmap_claninfo_data = {}
        self._globalmap_claninfo: dict = globalmap_claninfo_data
        self.clan_id: int = globalmap_claninfo_data.get('clan_id', 0)
        self.name: str = globalmap_claninfo_data.get('name', '')
        self.tag: str = globalmap_claninfo_data.get('tag', '')

        private_temp: dict = self._globalmap_claninfo.get('private')
        private_class = None
        if isinstance(private_temp, dict):
            for key in private_temp:
                if str(key).isnumeric():
                    private_class = {key: PrivateClass(data) for key, data in private_temp.items()}
                    break
                if key == 'daily_wage' or key == 'influence':
                    private_class = PrivateClass(private_temp)
                    break
        elif isinstance(private_temp, list):
            private_class = [PrivateClass(data) for data in private_temp]
        if not private_class:
            private_class: PrivateClass = PrivateClass(private_temp)
        self.private: PrivateClass | list[PrivateClass] | dict[str, PrivateClass] = private_class
        del private_temp, private_class


        ratings_temp: dict = self._globalmap_claninfo.get('ratings')
        ratings_class = None
        if isinstance(ratings_temp, dict):
            for key in ratings_temp:
                if str(key).isnumeric():
                    ratings_class = {key: RatingsClass(data) for key, data in ratings_temp.items()}
                    break
                if key == 'elo_10' or key == 'elo_6' or key == 'elo_8' or key == 'updated_at':
                    ratings_class = RatingsClass(ratings_temp)
                    break
        elif isinstance(ratings_temp, list):
            ratings_class = [RatingsClass(data) for data in ratings_temp]
        if not ratings_class:
            ratings_class: RatingsClass = RatingsClass(ratings_temp)
        self.ratings: RatingsClass | list[RatingsClass] | dict[str, RatingsClass] = ratings_class
        del ratings_temp, ratings_class


        statistics_temp: dict = self._globalmap_claninfo.get('statistics')
        statistics_class = None
        if isinstance(statistics_temp, dict):
            for key in statistics_temp:
                if str(key).isnumeric():
                    statistics_class = {key: StatisticsClass(data) for key, data in statistics_temp.items()}
                    break
                if key == 'battles' or key == 'battles_10_level' or key == 'battles_6_level' or key == 'battles_8_level' or key == 'captures' or key == 'losses' or key == 'provinces_count' or key == 'wins' or key == 'wins_10_level' or key == 'wins_6_level' or key == 'wins_8_level':
                    statistics_class = StatisticsClass(statistics_temp)
                    break
        elif isinstance(statistics_temp, list):
            statistics_class = [StatisticsClass(data) for data in statistics_temp]
        if not statistics_class:
            statistics_class: StatisticsClass = StatisticsClass(statistics_temp)
        self.statistics: StatisticsClass | list[StatisticsClass] | dict[str, StatisticsClass] = statistics_class
        del statistics_temp, statistics_class


