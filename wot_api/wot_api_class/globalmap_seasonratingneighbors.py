class GlobalmapSeasonratingneighborsClass:
    def __init__(self, globalmap_seasonratingneighbors_data: dict):
        if not globalmap_seasonratingneighbors_data: globalmap_seasonratingneighbors_data = {}
        self._globalmap_seasonratingneighbors: dict = globalmap_seasonratingneighbors_data
        self.award_level: str = globalmap_seasonratingneighbors_data.get('award_level', '')
        self.clan_id: int = globalmap_seasonratingneighbors_data.get('clan_id', 0)
        self.color: str = globalmap_seasonratingneighbors_data.get('color', '')
        self.name: str = globalmap_seasonratingneighbors_data.get('name', '')
        self.rank: int = globalmap_seasonratingneighbors_data.get('rank', 0)
        self.rank_delta: int = globalmap_seasonratingneighbors_data.get('rank_delta', 0)
        self.tag: str = globalmap_seasonratingneighbors_data.get('tag', '')
        self.updated_at: int = globalmap_seasonratingneighbors_data.get('updated_at', 0)
        self.victory_points: int = globalmap_seasonratingneighbors_data.get('victory_points', 0)
        self.victory_points_to_next_award: int = globalmap_seasonratingneighbors_data.get('victory_points_to_next_award', 0)

