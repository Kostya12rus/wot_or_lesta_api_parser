class EventsClass:
    def __init__(self, events_data: dict):
        if not events_data: events_data = {}
        self._events: dict = events_data
        self.account_id: int = events_data.get('account_id', 0)
        self.award_level: str = events_data.get('award_level', '')
        self.battles: int = events_data.get('battles', 0)
        self.battles_to_award: int = events_data.get('battles_to_award', 0)
        self.clan_id: int = events_data.get('clan_id', 0)
        self.clan_rank: int = events_data.get('clan_rank', 0)
        self.event_id: str = events_data.get('event_id', '')
        self.fame_points: int = events_data.get('fame_points', 0)
        self.fame_points_since_turn: int = events_data.get('fame_points_since_turn', 0)
        self.fame_points_to_improve_award: int = events_data.get('fame_points_to_improve_award', 0)
        self.front_id: str = events_data.get('front_id', '')
        self.rank: int = events_data.get('rank', 0)
        self.rank_delta: int = events_data.get('rank_delta', 0)
        self.updated_at: int = events_data.get('updated_at', 0)
        self.url: str = events_data.get('url', '')

class GlobalmapEventaccountinfoClass:
    def __init__(self, globalmap_eventaccountinfo_data: dict):
        if not globalmap_eventaccountinfo_data: globalmap_eventaccountinfo_data = {}
        self._globalmap_eventaccountinfo: dict = globalmap_eventaccountinfo_data

        events_temp: dict = self._globalmap_eventaccountinfo.get('events')
        events_class = None
        if isinstance(events_temp, dict):
            for key in events_temp:
                if str(key).isnumeric():
                    events_class = {key: EventsClass(data) for key, data in events_temp.items()}
                    break
                if key == 'account_id' or key == 'award_level' or key == 'battles' or key == 'battles_to_award' or key == 'clan_id' or key == 'clan_rank' or key == 'event_id' or key == 'fame_points' or key == 'fame_points_since_turn' or key == 'fame_points_to_improve_award' or key == 'front_id' or key == 'rank' or key == 'rank_delta' or key == 'updated_at' or key == 'url':
                    events_class = EventsClass(events_temp)
                    break
        elif isinstance(events_temp, list):
            events_class = [EventsClass(data) for data in events_temp]
        if not events_class:
            events_class: EventsClass = EventsClass(events_temp)
        self.events: EventsClass | list[EventsClass] | dict[str, EventsClass] = events_class
        del events_temp, events_class


