class SeasonsClass:
    def __init__(self, seasons_data: dict):
        if not seasons_data: seasons_data = {}
        self._seasons: dict = seasons_data
        self.battles: int = seasons_data.get('battles', 0)
        self.elo: int = seasons_data.get('elo', 0)
        self.rank: int = seasons_data.get('rank', 0)
        self.rank_delta: int = seasons_data.get('rank_delta', 0)
        self.vehicle_level: int = seasons_data.get('vehicle_level', 0)
        self.victory_points: int = seasons_data.get('victory_points', 0)
        self.victory_points_since_turn: int = seasons_data.get('victory_points_since_turn', 0)
        self.wins: int = seasons_data.get('wins', 0)

class GlobalmapSeasonclaninfoClass:
    def __init__(self, globalmap_seasonclaninfo_data: dict):
        if not globalmap_seasonclaninfo_data: globalmap_seasonclaninfo_data = {}
        self._globalmap_seasonclaninfo: dict = globalmap_seasonclaninfo_data

        seasons_temp: dict = self._globalmap_seasonclaninfo.get('seasons')
        seasons_class = None
        if isinstance(seasons_temp, dict):
            for key in seasons_temp:
                if str(key).isnumeric():
                    seasons_class = {key: SeasonsClass(data) for key, data in seasons_temp.items()}
                    break
                if key == 'battles' or key == 'elo' or key == 'rank' or key == 'rank_delta' or key == 'vehicle_level' or key == 'victory_points' or key == 'victory_points_since_turn' or key == 'wins':
                    seasons_class = SeasonsClass(seasons_temp)
                    break
        elif isinstance(seasons_temp, list):
            seasons_class = [SeasonsClass(data) for data in seasons_temp]
        if not seasons_class:
            seasons_class: SeasonsClass = SeasonsClass(seasons_temp)
        self.seasons: SeasonsClass | list[SeasonsClass] | dict[str, SeasonsClass] = seasons_class
        del seasons_temp, seasons_class


