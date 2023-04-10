class ClanAClass:
    def __init__(self, clan_a_data: dict):
        if not clan_a_data: clan_a_data = {}
        self._clan_a: dict = clan_a_data
        self.battle_reward: int = clan_a_data.get('battle_reward', 0)
        self.clan_id: int = clan_a_data.get('clan_id', 0)
        self.loose_elo_delta: int = clan_a_data.get('loose_elo_delta', 0)
        self.win_elo_delta: int = clan_a_data.get('win_elo_delta', 0)

class ClanBClass:
    def __init__(self, clan_b_data: dict):
        if not clan_b_data: clan_b_data = {}
        self._clan_b: dict = clan_b_data
        self.battle_reward: int = clan_b_data.get('battle_reward', 0)
        self.clan_id: int = clan_b_data.get('clan_id', 0)
        self.loose_elo_delta: int = clan_b_data.get('loose_elo_delta', 0)
        self.win_elo_delta: int = clan_b_data.get('win_elo_delta', 0)

class ActiveBattlesClass:
    def __init__(self, active_battles_data: dict):
        if not active_battles_data: active_battles_data = {}
        self._active_battles: dict = active_battles_data
        self.battle_reward: int = active_battles_data.get('battle_reward', 0)
        self.round: int = active_battles_data.get('round', 0)
        self.start_at: str = active_battles_data.get('start_at', '')

        clan_a_temp: dict = self._active_battles.get('clan_a')
        clan_a_class = None
        if isinstance(clan_a_temp, dict):
            for key in clan_a_temp:
                if str(key).isnumeric():
                    clan_a_class = {key: ClanAClass(data) for key, data in clan_a_temp.items()}
                    break
                if key == 'battle_reward' or key == 'clan_id' or key == 'loose_elo_delta' or key == 'win_elo_delta':
                    clan_a_class = ClanAClass(clan_a_temp)
                    break
        elif isinstance(clan_a_temp, list):
            clan_a_class = [ClanAClass(data) for data in clan_a_temp]
        if not clan_a_class:
            clan_a_class: ClanAClass = ClanAClass(clan_a_temp)
        self.clan_a: ClanAClass | list[ClanAClass] | dict[str, ClanAClass] = clan_a_class
        del clan_a_temp, clan_a_class


        clan_b_temp: dict = self._active_battles.get('clan_b')
        clan_b_class = None
        if isinstance(clan_b_temp, dict):
            for key in clan_b_temp:
                if str(key).isnumeric():
                    clan_b_class = {key: ClanBClass(data) for key, data in clan_b_temp.items()}
                    break
                if key == 'battle_reward' or key == 'clan_id' or key == 'loose_elo_delta' or key == 'win_elo_delta':
                    clan_b_class = ClanBClass(clan_b_temp)
                    break
        elif isinstance(clan_b_temp, list):
            clan_b_class = [ClanBClass(data) for data in clan_b_temp]
        if not clan_b_class:
            clan_b_class: ClanBClass = ClanBClass(clan_b_temp)
        self.clan_b: ClanBClass | list[ClanBClass] | dict[str, ClanBClass] = clan_b_class
        del clan_b_temp, clan_b_class


class GlobalmapProvincesClass:
    def __init__(self, globalmap_provinces_data: dict):
        if not globalmap_provinces_data: globalmap_provinces_data = {}
        self._globalmap_provinces: dict = globalmap_provinces_data
        self.arena_id: str = globalmap_provinces_data.get('arena_id', '')
        self.arena_name: str = globalmap_provinces_data.get('arena_name', '')
        self.attackers: list = globalmap_provinces_data.get('attackers', [])
        self.battles_start_at: str = globalmap_provinces_data.get('battles_start_at', '')
        self.competitors: list = globalmap_provinces_data.get('competitors', [])
        self.current_min_bet: int = globalmap_provinces_data.get('current_min_bet', 0)
        self.daily_revenue: int = globalmap_provinces_data.get('daily_revenue', 0)
        self.front_id: str = globalmap_provinces_data.get('front_id', '')
        self.front_name: str = globalmap_provinces_data.get('front_name', '')
        self.is_borders_disabled: bool = globalmap_provinces_data.get('is_borders_disabled', False)
        self.landing_type: str = globalmap_provinces_data.get('landing_type', '')
        self.last_won_bet: int = globalmap_provinces_data.get('last_won_bet', 0)
        self.max_bets: int = globalmap_provinces_data.get('max_bets', 0)
        self.neighbours: list = globalmap_provinces_data.get('neighbours', [])
        self.owner_clan_id: int = globalmap_provinces_data.get('owner_clan_id', 0)
        self.pillage_end_at: str = globalmap_provinces_data.get('pillage_end_at', '')
        self.prime_time: str = globalmap_provinces_data.get('prime_time', '')
        self.province_id: str = globalmap_provinces_data.get('province_id', '')
        self.province_name: str = globalmap_provinces_data.get('province_name', '')
        self.revenue_level: int = globalmap_provinces_data.get('revenue_level', 0)
        self.round_number: int = globalmap_provinces_data.get('round_number', 0)
        self.server: str = globalmap_provinces_data.get('server', '')
        self.status: str = globalmap_provinces_data.get('status', '')
        self.uri: str = globalmap_provinces_data.get('uri', '')
        self.world_redivision: bool = globalmap_provinces_data.get('world_redivision', False)

        active_battles_temp: dict = self._globalmap_provinces.get('active_battles')
        active_battles_class = None
        if isinstance(active_battles_temp, dict):
            for key in active_battles_temp:
                if str(key).isnumeric():
                    active_battles_class = {key: ActiveBattlesClass(data) for key, data in active_battles_temp.items()}
                    break
                if key == 'battle_reward' or key == 'round' or key == 'start_at' or key == 'clan_a' or key == 'clan_b':
                    active_battles_class = ActiveBattlesClass(active_battles_temp)
                    break
        elif isinstance(active_battles_temp, list):
            active_battles_class = [ActiveBattlesClass(data) for data in active_battles_temp]
        if not active_battles_class:
            active_battles_class: ActiveBattlesClass = ActiveBattlesClass(active_battles_temp)
        self.active_battles: ActiveBattlesClass | list[ActiveBattlesClass] | dict[str, ActiveBattlesClass] = active_battles_class
        del active_battles_temp, active_battles_class


