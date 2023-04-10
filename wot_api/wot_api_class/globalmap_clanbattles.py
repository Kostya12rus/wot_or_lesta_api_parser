class GlobalmapClanbattlesClass:
    def __init__(self, globalmap_clanbattles_data: dict):
        if not globalmap_clanbattles_data: globalmap_clanbattles_data = {}
        self._globalmap_clanbattles: dict = globalmap_clanbattles_data
        self.attack_type: str = globalmap_clanbattles_data.get('attack_type', '')
        self.competitor_id: int = globalmap_clanbattles_data.get('competitor_id', 0)
        self.front_id: str = globalmap_clanbattles_data.get('front_id', '')
        self.front_name: str = globalmap_clanbattles_data.get('front_name', '')
        self.province_id: str = globalmap_clanbattles_data.get('province_id', '')
        self.province_name: str = globalmap_clanbattles_data.get('province_name', '')
        self.time: int = globalmap_clanbattles_data.get('time', 0)
        self.type: str = globalmap_clanbattles_data.get('type', '')
        self.vehicle_level: int = globalmap_clanbattles_data.get('vehicle_level', 0)

