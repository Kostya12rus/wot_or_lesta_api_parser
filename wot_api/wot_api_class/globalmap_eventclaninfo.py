class EventsClass:
    def __init__(self, events_data: dict):
        if not events_data: events_data = {}
        self._events: dict = events_data
        self.battle_fame_points: int = events_data.get('battle_fame_points', 0)
        self.battles: int = events_data.get('battles', 0)
        self.event_id: str = events_data.get('event_id', '')
        self.fame_points: int = events_data.get('fame_points', 0)
        self.fame_points_since_turn: int = events_data.get('fame_points_since_turn', 0)
        self.front_id: str = events_data.get('front_id', '')
        self.rank: int = events_data.get('rank', 0)
        self.rank_delta: int = events_data.get('rank_delta', 0)
        self.task_fame_points: int = events_data.get('task_fame_points', 0)
        self.url: str = events_data.get('url', '')
        self.wins: int = events_data.get('wins', 0)

class GlobalmapEventclaninfoClass:
    def __init__(self, globalmap_eventclaninfo_data: dict):
        if not globalmap_eventclaninfo_data: globalmap_eventclaninfo_data = {}
        self._globalmap_eventclaninfo: dict = globalmap_eventclaninfo_data

        events_temp: dict = self._globalmap_eventclaninfo.get('events')
        events_class = None
        if isinstance(events_temp, dict):
            for key in events_temp:
                if str(key).isnumeric():
                    events_class = {key: EventsClass(data) for key, data in events_temp.items()}
                    break
                if key == 'battle_fame_points' or key == 'battles' or key == 'event_id' or key == 'fame_points' or key == 'fame_points_since_turn' or key == 'front_id' or key == 'rank' or key == 'rank_delta' or key == 'task_fame_points' or key == 'url' or key == 'wins':
                    events_class = EventsClass(events_temp)
                    break
        elif isinstance(events_temp, list):
            events_class = [EventsClass(data) for data in events_temp]
        if not events_class:
            events_class: EventsClass = EventsClass(events_temp)
        self.events: EventsClass | list[EventsClass] | dict[str, EventsClass] = events_class
        del events_temp, events_class


