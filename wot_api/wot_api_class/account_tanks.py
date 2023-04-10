class StatisticsClass:
    def __init__(self, statistics_data: dict):
        if not statistics_data: statistics_data = {}
        self._statistics: dict = statistics_data
        self.battles: int = statistics_data.get('battles', 0)
        self.wins: int = statistics_data.get('wins', 0)

class AccountTanksClass:
    def __init__(self, account_tanks_data: dict):
        if not account_tanks_data: account_tanks_data = {}
        self._account_tanks: dict = account_tanks_data
        self.mark_of_mastery: int = account_tanks_data.get('mark_of_mastery', 0)
        self.tank_id: int = account_tanks_data.get('tank_id', 0)

        statistics_temp: dict = self._account_tanks.get('statistics')
        statistics_class = None
        if isinstance(statistics_temp, dict):
            for key in statistics_temp:
                if str(key).isnumeric():
                    statistics_class = {key: StatisticsClass(data) for key, data in statistics_temp.items()}
                    break
                if key == 'battles' or key == 'wins':
                    statistics_class = StatisticsClass(statistics_temp)
                    break
        elif isinstance(statistics_temp, list):
            statistics_class = [StatisticsClass(data) for data in statistics_temp]
        if not statistics_class:
            statistics_class: StatisticsClass = StatisticsClass(statistics_temp)
        self.statistics: StatisticsClass | list[StatisticsClass] | dict[str, StatisticsClass] = statistics_class
        del statistics_temp, statistics_class


