class GlobalmapInfoClass:
    def __init__(self, globalmap_info_data: dict):
        if not globalmap_info_data: globalmap_info_data = {}
        self._globalmap_info: dict = globalmap_info_data
        self.last_turn: int = globalmap_info_data.get('last_turn', 0)
        self.last_turn_calculated_at: int = globalmap_info_data.get('last_turn_calculated_at', 0)
        self.last_turn_created_at: int = globalmap_info_data.get('last_turn_created_at', 0)
        self.state: str = globalmap_info_data.get('state', '')

