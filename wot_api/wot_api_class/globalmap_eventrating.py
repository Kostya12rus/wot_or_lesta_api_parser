class GlobalmapEventratingClass:
    def __init__(self, globalmap_eventrating_data: dict):
        if not globalmap_eventrating_data: globalmap_eventrating_data = {}
        self._globalmap_eventrating: dict = globalmap_eventrating_data
        self.award_level: str = globalmap_eventrating_data.get('award_level', '')
        self.battle_fame_points: int = globalmap_eventrating_data.get('battle_fame_points', 0)
        self.clan_id: int = globalmap_eventrating_data.get('clan_id', 0)
        self.color: str = globalmap_eventrating_data.get('color', '')
        self.fame_points_to_improve_award: int = globalmap_eventrating_data.get('fame_points_to_improve_award', 0)
        self.name: str = globalmap_eventrating_data.get('name', '')
        self.rank: int = globalmap_eventrating_data.get('rank', 0)
        self.rank_delta: int = globalmap_eventrating_data.get('rank_delta', 0)
        self.tag: str = globalmap_eventrating_data.get('tag', '')
        self.task_fame_points: int = globalmap_eventrating_data.get('task_fame_points', 0)
        self.total_fame_points: int = globalmap_eventrating_data.get('total_fame_points', 0)
        self.updated_at: int = globalmap_eventrating_data.get('updated_at', 0)

