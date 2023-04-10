class FrontsClass:
    def __init__(self, fronts_data: dict):
        if not fronts_data: fronts_data = {}
        self._fronts: dict = fronts_data
        self.front_id: str = fronts_data.get('front_id', '')
        self.front_name: str = fronts_data.get('front_name', '')
        self.url: str = fronts_data.get('url', '')

class GlobalmapEventsClass:
    def __init__(self, globalmap_events_data: dict):
        if not globalmap_events_data: globalmap_events_data = {}
        self._globalmap_events: dict = globalmap_events_data
        self.end: str = globalmap_events_data.get('end', '')
        self.event_id: str = globalmap_events_data.get('event_id', '')
        self.event_name: str = globalmap_events_data.get('event_name', '')
        self.start: str = globalmap_events_data.get('start', '')
        self.status: str = globalmap_events_data.get('status', '')

        fronts_temp: dict = self._globalmap_events.get('fronts')
        fronts_class = None
        if isinstance(fronts_temp, dict):
            for key in fronts_temp:
                if str(key).isnumeric():
                    fronts_class = {key: FrontsClass(data) for key, data in fronts_temp.items()}
                    break
                if key == 'front_id' or key == 'front_name' or key == 'url':
                    fronts_class = FrontsClass(fronts_temp)
                    break
        elif isinstance(fronts_temp, list):
            fronts_class = [FrontsClass(data) for data in fronts_temp]
        if not fronts_class:
            fronts_class: FrontsClass = FrontsClass(fronts_temp)
        self.fronts: FrontsClass | list[FrontsClass] | dict[str, FrontsClass] = fronts_class
        del fronts_temp, fronts_class


