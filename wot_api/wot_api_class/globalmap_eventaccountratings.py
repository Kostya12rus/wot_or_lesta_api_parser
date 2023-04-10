class GlobalmapEventaccountratingsClass:
    def __init__(self, globalmap_eventaccountratings_data: dict):
        if not globalmap_eventaccountratings_data: globalmap_eventaccountratings_data = {}
        self._globalmap_eventaccountratings: dict = globalmap_eventaccountratings_data
        self.account_id: int = globalmap_eventaccountratings_data.get('account_id', 0)
        self.award_level: str = globalmap_eventaccountratings_data.get('award_level', '')
        self.battles: int = globalmap_eventaccountratings_data.get('battles', 0)
        self.battles_to_award: int = globalmap_eventaccountratings_data.get('battles_to_award', 0)
        self.clan_id: int = globalmap_eventaccountratings_data.get('clan_id', 0)
        self.clan_rank: int = globalmap_eventaccountratings_data.get('clan_rank', 0)
        self.event_id: str = globalmap_eventaccountratings_data.get('event_id', '')
        self.fame_points: int = globalmap_eventaccountratings_data.get('fame_points', 0)
        self.fame_points_to_improve_award: int = globalmap_eventaccountratings_data.get('fame_points_to_improve_award', 0)
        self.front_id: str = globalmap_eventaccountratings_data.get('front_id', '')
        self.rank: int = globalmap_eventaccountratings_data.get('rank', 0)
        self.rank_delta: int = globalmap_eventaccountratings_data.get('rank_delta', 0)
        self.updated_at: int = globalmap_eventaccountratings_data.get('updated_at', 0)
        self.url: str = globalmap_eventaccountratings_data.get('url', '')

