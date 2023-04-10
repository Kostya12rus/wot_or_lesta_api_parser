class SeasonsClass:
    def __init__(self, seasons_data: dict):
        if not seasons_data: seasons_data = {}
        self._seasons: dict = seasons_data
        self.account_id: int = seasons_data.get('account_id', 0)
        self.award_level: str = seasons_data.get('award_level', '')
        self.battles: int = seasons_data.get('battles', 0)
        self.battles_to_award: int = seasons_data.get('battles_to_award', 0)
        self.clan_id: int = seasons_data.get('clan_id', 0)
        self.clan_rank: int = seasons_data.get('clan_rank', 0)
        self.season_id: str = seasons_data.get('season_id', '')
        self.updated_at: int = seasons_data.get('updated_at', 0)
        self.vehicle_level: int = seasons_data.get('vehicle_level', 0)

class GlobalmapSeasonaccountinfoClass:
    def __init__(self, globalmap_seasonaccountinfo_data: dict):
        if not globalmap_seasonaccountinfo_data: globalmap_seasonaccountinfo_data = {}
        self._globalmap_seasonaccountinfo: dict = globalmap_seasonaccountinfo_data

        seasons_temp: dict = self._globalmap_seasonaccountinfo.get('seasons')
        seasons_class = None
        if isinstance(seasons_temp, dict):
            for key in seasons_temp:
                if str(key).isnumeric():
                    seasons_class = {key: SeasonsClass(data) for key, data in seasons_temp.items()}
                    break
                if key == 'account_id' or key == 'award_level' or key == 'battles' or key == 'battles_to_award' or key == 'clan_id' or key == 'clan_rank' or key == 'season_id' or key == 'updated_at' or key == 'vehicle_level':
                    seasons_class = SeasonsClass(seasons_temp)
                    break
        elif isinstance(seasons_temp, list):
            seasons_class = [SeasonsClass(data) for data in seasons_temp]
        if not seasons_class:
            seasons_class: SeasonsClass = SeasonsClass(seasons_temp)
        self.seasons: SeasonsClass | list[SeasonsClass] | dict[str, SeasonsClass] = seasons_class
        del seasons_temp, seasons_class


