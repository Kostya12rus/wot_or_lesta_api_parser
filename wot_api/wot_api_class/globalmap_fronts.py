class AvailableExtensionsClass:
    def __init__(self, available_extensions_data: dict):
        if not available_extensions_data: available_extensions_data = {}
        self._available_extensions: dict = available_extensions_data
        self.cost: int = available_extensions_data.get('cost', 0)
        self.description_strategic: str = available_extensions_data.get('description_strategic', '')
        self.description_tactical: str = available_extensions_data.get('description_tactical', '')
        self.extension_id: str = available_extensions_data.get('extension_id', '')
        self.name: str = available_extensions_data.get('name', '')
        self.wage: int = available_extensions_data.get('wage', 0)

class GlobalmapFrontsClass:
    def __init__(self, globalmap_fronts_data: dict):
        if not globalmap_fronts_data: globalmap_fronts_data = {}
        self._globalmap_fronts: dict = globalmap_fronts_data
        self.avg_clans_rating: int = globalmap_fronts_data.get('avg_clans_rating', 0)
        self.avg_min_bet: int = globalmap_fronts_data.get('avg_min_bet', 0)
        self.avg_won_bet: int = globalmap_fronts_data.get('avg_won_bet', 0)
        self.battle_time_limit: int = globalmap_fronts_data.get('battle_time_limit', 0)
        self.division_cost: int = globalmap_fronts_data.get('division_cost', 0)
        self.fog_of_war: bool = globalmap_fronts_data.get('fog_of_war', False)
        self.front_id: str = globalmap_fronts_data.get('front_id', '')
        self.front_name: str = globalmap_fronts_data.get('front_name', '')
        self.is_active: bool = globalmap_fronts_data.get('is_active', False)
        self.is_event: bool = globalmap_fronts_data.get('is_event', False)
        self.max_tanks_per_division: int = globalmap_fronts_data.get('max_tanks_per_division', 0)
        self.max_vehicle_level: int = globalmap_fronts_data.get('max_vehicle_level', 0)
        self.min_tanks_per_division: int = globalmap_fronts_data.get('min_tanks_per_division', 0)
        self.min_vehicle_level: int = globalmap_fronts_data.get('min_vehicle_level', 0)
        self.provinces_count: int = globalmap_fronts_data.get('provinces_count', 0)
        self.vehicle_freeze: bool = globalmap_fronts_data.get('vehicle_freeze', False)

        available_extensions_temp: dict = self._globalmap_fronts.get('available_extensions')
        available_extensions_class = None
        if isinstance(available_extensions_temp, dict):
            for key in available_extensions_temp:
                if str(key).isnumeric():
                    available_extensions_class = {key: AvailableExtensionsClass(data) for key, data in available_extensions_temp.items()}
                    break
                if key == 'cost' or key == 'description_strategic' or key == 'description_tactical' or key == 'extension_id' or key == 'name' or key == 'wage':
                    available_extensions_class = AvailableExtensionsClass(available_extensions_temp)
                    break
        elif isinstance(available_extensions_temp, list):
            available_extensions_class = [AvailableExtensionsClass(data) for data in available_extensions_temp]
        if not available_extensions_class:
            available_extensions_class: AvailableExtensionsClass = AvailableExtensionsClass(available_extensions_temp)
        self.available_extensions: AvailableExtensionsClass | list[AvailableExtensionsClass] | dict[str, AvailableExtensionsClass] = available_extensions_class
        del available_extensions_temp, available_extensions_class


