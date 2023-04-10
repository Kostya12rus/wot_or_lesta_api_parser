class PrivateClass:
    def __init__(self, private_data: dict):
        if not private_data: private_data = {}
        self._private: dict = private_data
        self.hq_connected: bool = private_data.get('hq_connected', False)
        self.is_revenue_limit_exceeded: bool = private_data.get('is_revenue_limit_exceeded', False)

class GlobalmapClanprovincesClass:
    def __init__(self, globalmap_clanprovinces_data: dict):
        if not globalmap_clanprovinces_data: globalmap_clanprovinces_data = {}
        self._globalmap_clanprovinces: dict = globalmap_clanprovinces_data
        self.arena_id: str = globalmap_clanprovinces_data.get('arena_id', '')
        self.arena_name: str = globalmap_clanprovinces_data.get('arena_name', '')
        self.clan_id: int = globalmap_clanprovinces_data.get('clan_id', 0)
        self.daily_revenue: int = globalmap_clanprovinces_data.get('daily_revenue', 0)
        self.front_id: str = globalmap_clanprovinces_data.get('front_id', '')
        self.front_name: str = globalmap_clanprovinces_data.get('front_name', '')
        self.landing_type: str = globalmap_clanprovinces_data.get('landing_type', '')
        self.max_vehicle_level: int = globalmap_clanprovinces_data.get('max_vehicle_level', 0)
        self.pillage_end_at: str = globalmap_clanprovinces_data.get('pillage_end_at', '')
        self.prime_time: str = globalmap_clanprovinces_data.get('prime_time', '')
        self.province_id: str = globalmap_clanprovinces_data.get('province_id', '')
        self.province_name: str = globalmap_clanprovinces_data.get('province_name', '')
        self.revenue_level: int = globalmap_clanprovinces_data.get('revenue_level', 0)
        self.turns_owned: int = globalmap_clanprovinces_data.get('turns_owned', 0)

        private_temp: dict = self._globalmap_clanprovinces.get('private')
        private_class = None
        if isinstance(private_temp, dict):
            for key in private_temp:
                if str(key).isnumeric():
                    private_class = {key: PrivateClass(data) for key, data in private_temp.items()}
                    break
                if key == 'hq_connected' or key == 'is_revenue_limit_exceeded':
                    private_class = PrivateClass(private_temp)
                    break
        elif isinstance(private_temp, list):
            private_class = [PrivateClass(data) for data in private_temp]
        if not private_class:
            private_class: PrivateClass = PrivateClass(private_temp)
        self.private: PrivateClass | list[PrivateClass] | dict[str, PrivateClass] = private_class
        del private_temp, private_class


