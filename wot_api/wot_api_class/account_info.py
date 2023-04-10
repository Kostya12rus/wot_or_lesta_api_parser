class BoostersClass:
    def __init__(self, boosters_data: dict):
        if not boosters_data: boosters_data = {}
        self._boosters: dict = boosters_data
        self.count: int = boosters_data.get('count', 0)
        self.expiration_time: int = boosters_data.get('expiration_time', 0)
        self.state: str = boosters_data.get('state', '')

class GroupedContactsClass:
    def __init__(self, grouped_contacts_data: dict):
        if not grouped_contacts_data: grouped_contacts_data = {}
        self._grouped_contacts: dict = grouped_contacts_data
        self.blocked: list = grouped_contacts_data.get('blocked', [])
        self.groups: dict = grouped_contacts_data.get('groups', {})
        self.ignored: list = grouped_contacts_data.get('ignored', [])
        self.muted: list = grouped_contacts_data.get('muted', [])
        self.ungrouped: list = grouped_contacts_data.get('ungrouped', [])

class RentedClass:
    def __init__(self, rented_data: dict):
        if not rented_data: rented_data = {}
        self._rented: dict = rented_data
        self.compensation_credits: int = rented_data.get('compensation_credits', 0)
        self.compensation_gold: int = rented_data.get('compensation_gold', 0)
        self.expiration_time: int = rented_data.get('expiration_time', 0)
        self.tank_id: int = rented_data.get('tank_id', 0)

class RestrictionsClass:
    def __init__(self, restrictions_data: dict):
        if not restrictions_data: restrictions_data = {}
        self._restrictions: dict = restrictions_data
        self.chat_ban_time: int = restrictions_data.get('chat_ban_time', 0)

class PrivateClass:
    def __init__(self, private_data: dict):
        if not private_data: private_data = {}
        self._private: dict = private_data
        self.ban_info: str = private_data.get('ban_info', '')
        self.ban_time: int = private_data.get('ban_time', 0)
        self.battle_life_time: int = private_data.get('battle_life_time', 0)
        self.bonds: int = private_data.get('bonds', 0)
        self.credits: int = private_data.get('credits', 0)
        self.free_xp: int = private_data.get('free_xp', 0)
        self.garage: list = private_data.get('garage', [])
        self.gold: int = private_data.get('gold', 0)
        self.is_bound_to_phone: bool = private_data.get('is_bound_to_phone', False)
        self.is_premium: bool = private_data.get('is_premium', False)
        self.personal_missions: dict = private_data.get('personal_missions', {})
        self.premium_expires_at: int = private_data.get('premium_expires_at', 0)

        boosters_temp: dict = self._private.get('boosters')
        boosters_class = None
        if isinstance(boosters_temp, dict):
            for key in boosters_temp:
                if str(key).isnumeric():
                    boosters_class = {key: BoostersClass(data) for key, data in boosters_temp.items()}
                    break
                if key == 'count' or key == 'expiration_time' or key == 'state':
                    boosters_class = BoostersClass(boosters_temp)
                    break
        elif isinstance(boosters_temp, list):
            boosters_class = [BoostersClass(data) for data in boosters_temp]
        if not boosters_class:
            boosters_class: BoostersClass = BoostersClass(boosters_temp)
        self.boosters: BoostersClass | list[BoostersClass] | dict[str, BoostersClass] = boosters_class
        del boosters_temp, boosters_class


        grouped_contacts_temp: dict = self._private.get('grouped_contacts')
        grouped_contacts_class = None
        if isinstance(grouped_contacts_temp, dict):
            for key in grouped_contacts_temp:
                if str(key).isnumeric():
                    grouped_contacts_class = {key: GroupedContactsClass(data) for key, data in grouped_contacts_temp.items()}
                    break
                if key == 'blocked' or key == 'groups' or key == 'ignored' or key == 'muted' or key == 'ungrouped':
                    grouped_contacts_class = GroupedContactsClass(grouped_contacts_temp)
                    break
        elif isinstance(grouped_contacts_temp, list):
            grouped_contacts_class = [GroupedContactsClass(data) for data in grouped_contacts_temp]
        if not grouped_contacts_class:
            grouped_contacts_class: GroupedContactsClass = GroupedContactsClass(grouped_contacts_temp)
        self.grouped_contacts: GroupedContactsClass | list[GroupedContactsClass] | dict[str, GroupedContactsClass] = grouped_contacts_class
        del grouped_contacts_temp, grouped_contacts_class


        rented_temp: dict = self._private.get('rented')
        rented_class = None
        if isinstance(rented_temp, dict):
            for key in rented_temp:
                if str(key).isnumeric():
                    rented_class = {key: RentedClass(data) for key, data in rented_temp.items()}
                    break
                if key == 'compensation_credits' or key == 'compensation_gold' or key == 'expiration_time' or key == 'tank_id':
                    rented_class = RentedClass(rented_temp)
                    break
        elif isinstance(rented_temp, list):
            rented_class = [RentedClass(data) for data in rented_temp]
        if not rented_class:
            rented_class: RentedClass = RentedClass(rented_temp)
        self.rented: RentedClass | list[RentedClass] | dict[str, RentedClass] = rented_class
        del rented_temp, rented_class


        restrictions_temp: dict = self._private.get('restrictions')
        restrictions_class = None
        if isinstance(restrictions_temp, dict):
            for key in restrictions_temp:
                if str(key).isnumeric():
                    restrictions_class = {key: RestrictionsClass(data) for key, data in restrictions_temp.items()}
                    break
                if key == 'chat_ban_time':
                    restrictions_class = RestrictionsClass(restrictions_temp)
                    break
        elif isinstance(restrictions_temp, list):
            restrictions_class = [RestrictionsClass(data) for data in restrictions_temp]
        if not restrictions_class:
            restrictions_class: RestrictionsClass = RestrictionsClass(restrictions_temp)
        self.restrictions: RestrictionsClass | list[RestrictionsClass] | dict[str, RestrictionsClass] = restrictions_class
        del restrictions_temp, restrictions_class


class AllClass:
    def __init__(self, all_data: dict):
        if not all_data: all_data = {}
        self._all: dict = all_data
        self.avg_damage_assisted: float = all_data.get('avg_damage_assisted', 0.0)
        self.avg_damage_assisted_radio: float = all_data.get('avg_damage_assisted_radio', 0.0)
        self.avg_damage_assisted_track: float = all_data.get('avg_damage_assisted_track', 0.0)
        self.avg_damage_blocked: float = all_data.get('avg_damage_blocked', 0.0)
        self.battle_avg_xp: int = all_data.get('battle_avg_xp', 0)
        self.battles: int = all_data.get('battles', 0)
        self.battles_on_stunning_vehicles: int = all_data.get('battles_on_stunning_vehicles', 0)
        self.capture_points: int = all_data.get('capture_points', 0)
        self.damage_dealt: int = all_data.get('damage_dealt', 0)
        self.damage_received: int = all_data.get('damage_received', 0)
        self.direct_hits_received: int = all_data.get('direct_hits_received', 0)
        self.draws: int = all_data.get('draws', 0)
        self.dropped_capture_points: int = all_data.get('dropped_capture_points', 0)
        self.explosion_hits: int = all_data.get('explosion_hits', 0)
        self.explosion_hits_received: int = all_data.get('explosion_hits_received', 0)
        self.frags: int = all_data.get('frags', 0)
        self.hits: int = all_data.get('hits', 0)
        self.hits_percents: int = all_data.get('hits_percents', 0)
        self.losses: int = all_data.get('losses', 0)
        self.max_damage: int = all_data.get('max_damage', 0)
        self.max_damage_tank_id: int = all_data.get('max_damage_tank_id', 0)
        self.max_frags: int = all_data.get('max_frags', 0)
        self.max_frags_tank_id: int = all_data.get('max_frags_tank_id', 0)
        self.max_xp: int = all_data.get('max_xp', 0)
        self.max_xp_tank_id: int = all_data.get('max_xp_tank_id', 0)
        self.no_damage_direct_hits_received: int = all_data.get('no_damage_direct_hits_received', 0)
        self.piercings: int = all_data.get('piercings', 0)
        self.piercings_received: int = all_data.get('piercings_received', 0)
        self.shots: int = all_data.get('shots', 0)
        self.spotted: int = all_data.get('spotted', 0)
        self.stun_assisted_damage: int = all_data.get('stun_assisted_damage', 0)
        self.stun_number: int = all_data.get('stun_number', 0)
        self.survived_battles: int = all_data.get('survived_battles', 0)
        self.tanking_factor: float = all_data.get('tanking_factor', 0.0)
        self.wins: int = all_data.get('wins', 0)
        self.xp: int = all_data.get('xp', 0)

class ClanClass:
    def __init__(self, clan_data: dict):
        if not clan_data: clan_data = {}
        self._clan: dict = clan_data
        self.avg_damage_assisted: float = clan_data.get('avg_damage_assisted', 0.0)
        self.avg_damage_assisted_radio: float = clan_data.get('avg_damage_assisted_radio', 0.0)
        self.avg_damage_assisted_track: float = clan_data.get('avg_damage_assisted_track', 0.0)
        self.avg_damage_blocked: float = clan_data.get('avg_damage_blocked', 0.0)
        self.battle_avg_xp: int = clan_data.get('battle_avg_xp', 0)
        self.battles: int = clan_data.get('battles', 0)
        self.battles_on_stunning_vehicles: int = clan_data.get('battles_on_stunning_vehicles', 0)
        self.capture_points: int = clan_data.get('capture_points', 0)
        self.damage_dealt: int = clan_data.get('damage_dealt', 0)
        self.damage_received: int = clan_data.get('damage_received', 0)
        self.direct_hits_received: int = clan_data.get('direct_hits_received', 0)
        self.draws: int = clan_data.get('draws', 0)
        self.dropped_capture_points: int = clan_data.get('dropped_capture_points', 0)
        self.explosion_hits: int = clan_data.get('explosion_hits', 0)
        self.explosion_hits_received: int = clan_data.get('explosion_hits_received', 0)
        self.frags: int = clan_data.get('frags', 0)
        self.hits: int = clan_data.get('hits', 0)
        self.hits_percents: int = clan_data.get('hits_percents', 0)
        self.losses: int = clan_data.get('losses', 0)
        self.no_damage_direct_hits_received: int = clan_data.get('no_damage_direct_hits_received', 0)
        self.piercings: int = clan_data.get('piercings', 0)
        self.piercings_received: int = clan_data.get('piercings_received', 0)
        self.shots: int = clan_data.get('shots', 0)
        self.spotted: int = clan_data.get('spotted', 0)
        self.stun_assisted_damage: int = clan_data.get('stun_assisted_damage', 0)
        self.stun_number: int = clan_data.get('stun_number', 0)
        self.survived_battles: int = clan_data.get('survived_battles', 0)
        self.tanking_factor: float = clan_data.get('tanking_factor', 0.0)
        self.wins: int = clan_data.get('wins', 0)
        self.xp: int = clan_data.get('xp', 0)

class CompanyClass:
    def __init__(self, company_data: dict):
        if not company_data: company_data = {}
        self._company: dict = company_data
        self.avg_damage_assisted: float = company_data.get('avg_damage_assisted', 0.0)
        self.avg_damage_assisted_radio: float = company_data.get('avg_damage_assisted_radio', 0.0)
        self.avg_damage_assisted_track: float = company_data.get('avg_damage_assisted_track', 0.0)
        self.avg_damage_blocked: float = company_data.get('avg_damage_blocked', 0.0)
        self.battle_avg_xp: int = company_data.get('battle_avg_xp', 0)
        self.battles: int = company_data.get('battles', 0)
        self.battles_on_stunning_vehicles: int = company_data.get('battles_on_stunning_vehicles', 0)
        self.capture_points: int = company_data.get('capture_points', 0)
        self.damage_dealt: int = company_data.get('damage_dealt', 0)
        self.damage_received: int = company_data.get('damage_received', 0)
        self.direct_hits_received: int = company_data.get('direct_hits_received', 0)
        self.draws: int = company_data.get('draws', 0)
        self.dropped_capture_points: int = company_data.get('dropped_capture_points', 0)
        self.explosion_hits: int = company_data.get('explosion_hits', 0)
        self.explosion_hits_received: int = company_data.get('explosion_hits_received', 0)
        self.frags: int = company_data.get('frags', 0)
        self.hits: int = company_data.get('hits', 0)
        self.hits_percents: int = company_data.get('hits_percents', 0)
        self.losses: int = company_data.get('losses', 0)
        self.no_damage_direct_hits_received: int = company_data.get('no_damage_direct_hits_received', 0)
        self.piercings: int = company_data.get('piercings', 0)
        self.piercings_received: int = company_data.get('piercings_received', 0)
        self.shots: int = company_data.get('shots', 0)
        self.spotted: int = company_data.get('spotted', 0)
        self.stun_assisted_damage: int = company_data.get('stun_assisted_damage', 0)
        self.stun_number: int = company_data.get('stun_number', 0)
        self.survived_battles: int = company_data.get('survived_battles', 0)
        self.tanking_factor: float = company_data.get('tanking_factor', 0.0)
        self.wins: int = company_data.get('wins', 0)
        self.xp: int = company_data.get('xp', 0)

class EpicClass:
    def __init__(self, epic_data: dict):
        if not epic_data: epic_data = {}
        self._epic: dict = epic_data
        self.avg_damage_assisted: float = epic_data.get('avg_damage_assisted', 0.0)
        self.avg_damage_assisted_radio: float = epic_data.get('avg_damage_assisted_radio', 0.0)
        self.avg_damage_assisted_track: float = epic_data.get('avg_damage_assisted_track', 0.0)
        self.avg_damage_blocked: float = epic_data.get('avg_damage_blocked', 0.0)
        self.battle_avg_xp: int = epic_data.get('battle_avg_xp', 0)
        self.battles: int = epic_data.get('battles', 0)
        self.battles_on_stunning_vehicles: int = epic_data.get('battles_on_stunning_vehicles', 0)
        self.capture_points: int = epic_data.get('capture_points', 0)
        self.damage_dealt: int = epic_data.get('damage_dealt', 0)
        self.damage_received: int = epic_data.get('damage_received', 0)
        self.direct_hits_received: int = epic_data.get('direct_hits_received', 0)
        self.draws: int = epic_data.get('draws', 0)
        self.dropped_capture_points: int = epic_data.get('dropped_capture_points', 0)
        self.explosion_hits: int = epic_data.get('explosion_hits', 0)
        self.explosion_hits_received: int = epic_data.get('explosion_hits_received', 0)
        self.frags: int = epic_data.get('frags', 0)
        self.hits: int = epic_data.get('hits', 0)
        self.hits_percents: int = epic_data.get('hits_percents', 0)
        self.losses: int = epic_data.get('losses', 0)
        self.max_damage: int = epic_data.get('max_damage', 0)
        self.max_damage_tank_id: int = epic_data.get('max_damage_tank_id', 0)
        self.max_frags: int = epic_data.get('max_frags', 0)
        self.max_frags_tank_id: int = epic_data.get('max_frags_tank_id', 0)
        self.max_xp: int = epic_data.get('max_xp', 0)
        self.max_xp_tank_id: int = epic_data.get('max_xp_tank_id', 0)
        self.no_damage_direct_hits_received: int = epic_data.get('no_damage_direct_hits_received', 0)
        self.piercings: int = epic_data.get('piercings', 0)
        self.piercings_received: int = epic_data.get('piercings_received', 0)
        self.shots: int = epic_data.get('shots', 0)
        self.spotted: int = epic_data.get('spotted', 0)
        self.stun_assisted_damage: int = epic_data.get('stun_assisted_damage', 0)
        self.stun_number: int = epic_data.get('stun_number', 0)
        self.survived_battles: int = epic_data.get('survived_battles', 0)
        self.tanking_factor: float = epic_data.get('tanking_factor', 0.0)
        self.wins: int = epic_data.get('wins', 0)
        self.xp: int = epic_data.get('xp', 0)

class FalloutClass:
    def __init__(self, fallout_data: dict):
        if not fallout_data: fallout_data = {}
        self._fallout: dict = fallout_data
        self.avatar_damage_dealt: int = fallout_data.get('avatar_damage_dealt', 0)
        self.avatar_frags: int = fallout_data.get('avatar_frags', 0)
        self.avg_damage_assisted: float = fallout_data.get('avg_damage_assisted', 0.0)
        self.avg_damage_assisted_radio: float = fallout_data.get('avg_damage_assisted_radio', 0.0)
        self.avg_damage_assisted_track: float = fallout_data.get('avg_damage_assisted_track', 0.0)
        self.avg_damage_blocked: float = fallout_data.get('avg_damage_blocked', 0.0)
        self.battle_avg_xp: int = fallout_data.get('battle_avg_xp', 0)
        self.battles: int = fallout_data.get('battles', 0)
        self.battles_on_stunning_vehicles: int = fallout_data.get('battles_on_stunning_vehicles', 0)
        self.capture_points: int = fallout_data.get('capture_points', 0)
        self.damage_dealt: int = fallout_data.get('damage_dealt', 0)
        self.damage_received: int = fallout_data.get('damage_received', 0)
        self.death_count: int = fallout_data.get('death_count', 0)
        self.direct_hits_received: int = fallout_data.get('direct_hits_received', 0)
        self.draws: int = fallout_data.get('draws', 0)
        self.dropped_capture_points: int = fallout_data.get('dropped_capture_points', 0)
        self.explosion_hits: int = fallout_data.get('explosion_hits', 0)
        self.explosion_hits_received: int = fallout_data.get('explosion_hits_received', 0)
        self.flag_capture: int = fallout_data.get('flag_capture', 0)
        self.flag_capture_solo: int = fallout_data.get('flag_capture_solo', 0)
        self.frags: int = fallout_data.get('frags', 0)
        self.hits: int = fallout_data.get('hits', 0)
        self.hits_percents: int = fallout_data.get('hits_percents', 0)
        self.losses: int = fallout_data.get('losses', 0)
        self.max_damage: int = fallout_data.get('max_damage', 0)
        self.max_damage_tank_id: int = fallout_data.get('max_damage_tank_id', 0)
        self.max_damage_with_avatar: int = fallout_data.get('max_damage_with_avatar', 0)
        self.max_frags: int = fallout_data.get('max_frags', 0)
        self.max_frags_tank_id: int = fallout_data.get('max_frags_tank_id', 0)
        self.max_frags_with_avatar: int = fallout_data.get('max_frags_with_avatar', 0)
        self.max_win_points: int = fallout_data.get('max_win_points', 0)
        self.max_xp: int = fallout_data.get('max_xp', 0)
        self.max_xp_tank_id: int = fallout_data.get('max_xp_tank_id', 0)
        self.no_damage_direct_hits_received: int = fallout_data.get('no_damage_direct_hits_received', 0)
        self.piercings: int = fallout_data.get('piercings', 0)
        self.piercings_received: int = fallout_data.get('piercings_received', 0)
        self.resource_absorbed: int = fallout_data.get('resource_absorbed', 0)
        self.shots: int = fallout_data.get('shots', 0)
        self.spotted: int = fallout_data.get('spotted', 0)
        self.stun_assisted_damage: int = fallout_data.get('stun_assisted_damage', 0)
        self.stun_number: int = fallout_data.get('stun_number', 0)
        self.survived_battles: int = fallout_data.get('survived_battles', 0)
        self.tanking_factor: float = fallout_data.get('tanking_factor', 0.0)
        self.win_points: int = fallout_data.get('win_points', 0)
        self.wins: int = fallout_data.get('wins', 0)
        self.xp: int = fallout_data.get('xp', 0)

class GlobalmapAbsoluteClass:
    def __init__(self, globalmap_absolute_data: dict):
        if not globalmap_absolute_data: globalmap_absolute_data = {}
        self._globalmap_absolute: dict = globalmap_absolute_data
        self.avg_damage_assisted: float = globalmap_absolute_data.get('avg_damage_assisted', 0.0)
        self.avg_damage_assisted_radio: float = globalmap_absolute_data.get('avg_damage_assisted_radio', 0.0)
        self.avg_damage_assisted_track: float = globalmap_absolute_data.get('avg_damage_assisted_track', 0.0)
        self.avg_damage_blocked: float = globalmap_absolute_data.get('avg_damage_blocked', 0.0)
        self.battle_avg_xp: int = globalmap_absolute_data.get('battle_avg_xp', 0)
        self.battles: int = globalmap_absolute_data.get('battles', 0)
        self.battles_on_stunning_vehicles: int = globalmap_absolute_data.get('battles_on_stunning_vehicles', 0)
        self.capture_points: int = globalmap_absolute_data.get('capture_points', 0)
        self.damage_dealt: int = globalmap_absolute_data.get('damage_dealt', 0)
        self.damage_received: int = globalmap_absolute_data.get('damage_received', 0)
        self.direct_hits_received: int = globalmap_absolute_data.get('direct_hits_received', 0)
        self.draws: int = globalmap_absolute_data.get('draws', 0)
        self.dropped_capture_points: int = globalmap_absolute_data.get('dropped_capture_points', 0)
        self.explosion_hits: int = globalmap_absolute_data.get('explosion_hits', 0)
        self.explosion_hits_received: int = globalmap_absolute_data.get('explosion_hits_received', 0)
        self.frags: int = globalmap_absolute_data.get('frags', 0)
        self.hits: int = globalmap_absolute_data.get('hits', 0)
        self.hits_percents: int = globalmap_absolute_data.get('hits_percents', 0)
        self.losses: int = globalmap_absolute_data.get('losses', 0)
        self.no_damage_direct_hits_received: int = globalmap_absolute_data.get('no_damage_direct_hits_received', 0)
        self.piercings: int = globalmap_absolute_data.get('piercings', 0)
        self.piercings_received: int = globalmap_absolute_data.get('piercings_received', 0)
        self.shots: int = globalmap_absolute_data.get('shots', 0)
        self.spotted: int = globalmap_absolute_data.get('spotted', 0)
        self.stun_assisted_damage: int = globalmap_absolute_data.get('stun_assisted_damage', 0)
        self.stun_number: int = globalmap_absolute_data.get('stun_number', 0)
        self.survived_battles: int = globalmap_absolute_data.get('survived_battles', 0)
        self.tanking_factor: float = globalmap_absolute_data.get('tanking_factor', 0.0)
        self.wins: int = globalmap_absolute_data.get('wins', 0)
        self.xp: int = globalmap_absolute_data.get('xp', 0)

class GlobalmapChampionClass:
    def __init__(self, globalmap_champion_data: dict):
        if not globalmap_champion_data: globalmap_champion_data = {}
        self._globalmap_champion: dict = globalmap_champion_data
        self.avg_damage_assisted: float = globalmap_champion_data.get('avg_damage_assisted', 0.0)
        self.avg_damage_assisted_radio: float = globalmap_champion_data.get('avg_damage_assisted_radio', 0.0)
        self.avg_damage_assisted_track: float = globalmap_champion_data.get('avg_damage_assisted_track', 0.0)
        self.avg_damage_blocked: float = globalmap_champion_data.get('avg_damage_blocked', 0.0)
        self.battle_avg_xp: int = globalmap_champion_data.get('battle_avg_xp', 0)
        self.battles: int = globalmap_champion_data.get('battles', 0)
        self.battles_on_stunning_vehicles: int = globalmap_champion_data.get('battles_on_stunning_vehicles', 0)
        self.capture_points: int = globalmap_champion_data.get('capture_points', 0)
        self.damage_dealt: int = globalmap_champion_data.get('damage_dealt', 0)
        self.damage_received: int = globalmap_champion_data.get('damage_received', 0)
        self.direct_hits_received: int = globalmap_champion_data.get('direct_hits_received', 0)
        self.draws: int = globalmap_champion_data.get('draws', 0)
        self.dropped_capture_points: int = globalmap_champion_data.get('dropped_capture_points', 0)
        self.explosion_hits: int = globalmap_champion_data.get('explosion_hits', 0)
        self.explosion_hits_received: int = globalmap_champion_data.get('explosion_hits_received', 0)
        self.frags: int = globalmap_champion_data.get('frags', 0)
        self.hits: int = globalmap_champion_data.get('hits', 0)
        self.hits_percents: int = globalmap_champion_data.get('hits_percents', 0)
        self.losses: int = globalmap_champion_data.get('losses', 0)
        self.no_damage_direct_hits_received: int = globalmap_champion_data.get('no_damage_direct_hits_received', 0)
        self.piercings: int = globalmap_champion_data.get('piercings', 0)
        self.piercings_received: int = globalmap_champion_data.get('piercings_received', 0)
        self.shots: int = globalmap_champion_data.get('shots', 0)
        self.spotted: int = globalmap_champion_data.get('spotted', 0)
        self.stun_assisted_damage: int = globalmap_champion_data.get('stun_assisted_damage', 0)
        self.stun_number: int = globalmap_champion_data.get('stun_number', 0)
        self.survived_battles: int = globalmap_champion_data.get('survived_battles', 0)
        self.tanking_factor: float = globalmap_champion_data.get('tanking_factor', 0.0)
        self.wins: int = globalmap_champion_data.get('wins', 0)
        self.xp: int = globalmap_champion_data.get('xp', 0)

class GlobalmapMiddleClass:
    def __init__(self, globalmap_middle_data: dict):
        if not globalmap_middle_data: globalmap_middle_data = {}
        self._globalmap_middle: dict = globalmap_middle_data
        self.avg_damage_assisted: float = globalmap_middle_data.get('avg_damage_assisted', 0.0)
        self.avg_damage_assisted_radio: float = globalmap_middle_data.get('avg_damage_assisted_radio', 0.0)
        self.avg_damage_assisted_track: float = globalmap_middle_data.get('avg_damage_assisted_track', 0.0)
        self.avg_damage_blocked: float = globalmap_middle_data.get('avg_damage_blocked', 0.0)
        self.battle_avg_xp: int = globalmap_middle_data.get('battle_avg_xp', 0)
        self.battles: int = globalmap_middle_data.get('battles', 0)
        self.battles_on_stunning_vehicles: int = globalmap_middle_data.get('battles_on_stunning_vehicles', 0)
        self.capture_points: int = globalmap_middle_data.get('capture_points', 0)
        self.damage_dealt: int = globalmap_middle_data.get('damage_dealt', 0)
        self.damage_received: int = globalmap_middle_data.get('damage_received', 0)
        self.direct_hits_received: int = globalmap_middle_data.get('direct_hits_received', 0)
        self.draws: int = globalmap_middle_data.get('draws', 0)
        self.dropped_capture_points: int = globalmap_middle_data.get('dropped_capture_points', 0)
        self.explosion_hits: int = globalmap_middle_data.get('explosion_hits', 0)
        self.explosion_hits_received: int = globalmap_middle_data.get('explosion_hits_received', 0)
        self.frags: int = globalmap_middle_data.get('frags', 0)
        self.hits: int = globalmap_middle_data.get('hits', 0)
        self.hits_percents: int = globalmap_middle_data.get('hits_percents', 0)
        self.losses: int = globalmap_middle_data.get('losses', 0)
        self.no_damage_direct_hits_received: int = globalmap_middle_data.get('no_damage_direct_hits_received', 0)
        self.piercings: int = globalmap_middle_data.get('piercings', 0)
        self.piercings_received: int = globalmap_middle_data.get('piercings_received', 0)
        self.shots: int = globalmap_middle_data.get('shots', 0)
        self.spotted: int = globalmap_middle_data.get('spotted', 0)
        self.stun_assisted_damage: int = globalmap_middle_data.get('stun_assisted_damage', 0)
        self.stun_number: int = globalmap_middle_data.get('stun_number', 0)
        self.survived_battles: int = globalmap_middle_data.get('survived_battles', 0)
        self.tanking_factor: float = globalmap_middle_data.get('tanking_factor', 0.0)
        self.wins: int = globalmap_middle_data.get('wins', 0)
        self.xp: int = globalmap_middle_data.get('xp', 0)

class HistoricalClass:
    def __init__(self, historical_data: dict):
        if not historical_data: historical_data = {}
        self._historical: dict = historical_data
        self.avg_damage_assisted: float = historical_data.get('avg_damage_assisted', 0.0)
        self.avg_damage_assisted_radio: float = historical_data.get('avg_damage_assisted_radio', 0.0)
        self.avg_damage_assisted_track: float = historical_data.get('avg_damage_assisted_track', 0.0)
        self.avg_damage_blocked: float = historical_data.get('avg_damage_blocked', 0.0)
        self.battle_avg_xp: int = historical_data.get('battle_avg_xp', 0)
        self.battles: int = historical_data.get('battles', 0)
        self.battles_on_stunning_vehicles: int = historical_data.get('battles_on_stunning_vehicles', 0)
        self.capture_points: int = historical_data.get('capture_points', 0)
        self.damage_dealt: int = historical_data.get('damage_dealt', 0)
        self.damage_received: int = historical_data.get('damage_received', 0)
        self.direct_hits_received: int = historical_data.get('direct_hits_received', 0)
        self.draws: int = historical_data.get('draws', 0)
        self.dropped_capture_points: int = historical_data.get('dropped_capture_points', 0)
        self.explosion_hits: int = historical_data.get('explosion_hits', 0)
        self.explosion_hits_received: int = historical_data.get('explosion_hits_received', 0)
        self.frags: int = historical_data.get('frags', 0)
        self.hits: int = historical_data.get('hits', 0)
        self.hits_percents: int = historical_data.get('hits_percents', 0)
        self.losses: int = historical_data.get('losses', 0)
        self.max_damage: int = historical_data.get('max_damage', 0)
        self.max_damage_tank_id: int = historical_data.get('max_damage_tank_id', 0)
        self.max_frags: int = historical_data.get('max_frags', 0)
        self.max_frags_tank_id: int = historical_data.get('max_frags_tank_id', 0)
        self.max_xp: int = historical_data.get('max_xp', 0)
        self.max_xp_tank_id: int = historical_data.get('max_xp_tank_id', 0)
        self.no_damage_direct_hits_received: int = historical_data.get('no_damage_direct_hits_received', 0)
        self.piercings: int = historical_data.get('piercings', 0)
        self.piercings_received: int = historical_data.get('piercings_received', 0)
        self.shots: int = historical_data.get('shots', 0)
        self.spotted: int = historical_data.get('spotted', 0)
        self.stun_assisted_damage: int = historical_data.get('stun_assisted_damage', 0)
        self.stun_number: int = historical_data.get('stun_number', 0)
        self.survived_battles: int = historical_data.get('survived_battles', 0)
        self.tanking_factor: float = historical_data.get('tanking_factor', 0.0)
        self.wins: int = historical_data.get('wins', 0)
        self.xp: int = historical_data.get('xp', 0)

class RandomClass:
    def __init__(self, random_data: dict):
        if not random_data: random_data = {}
        self._random: dict = random_data
        self.avg_damage_assisted: float = random_data.get('avg_damage_assisted', 0.0)
        self.avg_damage_assisted_radio: float = random_data.get('avg_damage_assisted_radio', 0.0)
        self.avg_damage_assisted_track: float = random_data.get('avg_damage_assisted_track', 0.0)
        self.avg_damage_blocked: float = random_data.get('avg_damage_blocked', 0.0)
        self.battle_avg_xp: int = random_data.get('battle_avg_xp', 0)
        self.battles: int = random_data.get('battles', 0)
        self.battles_on_stunning_vehicles: int = random_data.get('battles_on_stunning_vehicles', 0)
        self.capture_points: int = random_data.get('capture_points', 0)
        self.damage_dealt: int = random_data.get('damage_dealt', 0)
        self.damage_received: int = random_data.get('damage_received', 0)
        self.direct_hits_received: int = random_data.get('direct_hits_received', 0)
        self.draws: int = random_data.get('draws', 0)
        self.dropped_capture_points: int = random_data.get('dropped_capture_points', 0)
        self.explosion_hits: int = random_data.get('explosion_hits', 0)
        self.explosion_hits_received: int = random_data.get('explosion_hits_received', 0)
        self.frags: int = random_data.get('frags', 0)
        self.hits: int = random_data.get('hits', 0)
        self.hits_percents: int = random_data.get('hits_percents', 0)
        self.losses: int = random_data.get('losses', 0)
        self.no_damage_direct_hits_received: int = random_data.get('no_damage_direct_hits_received', 0)
        self.piercings: int = random_data.get('piercings', 0)
        self.piercings_received: int = random_data.get('piercings_received', 0)
        self.shots: int = random_data.get('shots', 0)
        self.spotted: int = random_data.get('spotted', 0)
        self.stun_assisted_damage: int = random_data.get('stun_assisted_damage', 0)
        self.stun_number: int = random_data.get('stun_number', 0)
        self.survived_battles: int = random_data.get('survived_battles', 0)
        self.tanking_factor: float = random_data.get('tanking_factor', 0.0)
        self.wins: int = random_data.get('wins', 0)
        self.xp: int = random_data.get('xp', 0)

class Ranked10X10Class:
    def __init__(self, ranked_10x10_data: dict):
        if not ranked_10x10_data: ranked_10x10_data = {}
        self._ranked_10x10: dict = ranked_10x10_data
        self.avg_damage_assisted: float = ranked_10x10_data.get('avg_damage_assisted', 0.0)
        self.avg_damage_assisted_radio: float = ranked_10x10_data.get('avg_damage_assisted_radio', 0.0)
        self.avg_damage_assisted_track: float = ranked_10x10_data.get('avg_damage_assisted_track', 0.0)
        self.avg_damage_blocked: float = ranked_10x10_data.get('avg_damage_blocked', 0.0)
        self.battle_avg_xp: int = ranked_10x10_data.get('battle_avg_xp', 0)
        self.battles: int = ranked_10x10_data.get('battles', 0)
        self.battles_on_stunning_vehicles: int = ranked_10x10_data.get('battles_on_stunning_vehicles', 0)
        self.capture_points: int = ranked_10x10_data.get('capture_points', 0)
        self.damage_dealt: int = ranked_10x10_data.get('damage_dealt', 0)
        self.damage_received: int = ranked_10x10_data.get('damage_received', 0)
        self.direct_hits_received: int = ranked_10x10_data.get('direct_hits_received', 0)
        self.draws: int = ranked_10x10_data.get('draws', 0)
        self.dropped_capture_points: int = ranked_10x10_data.get('dropped_capture_points', 0)
        self.explosion_hits: int = ranked_10x10_data.get('explosion_hits', 0)
        self.explosion_hits_received: int = ranked_10x10_data.get('explosion_hits_received', 0)
        self.frags: int = ranked_10x10_data.get('frags', 0)
        self.hits: int = ranked_10x10_data.get('hits', 0)
        self.hits_percents: int = ranked_10x10_data.get('hits_percents', 0)
        self.losses: int = ranked_10x10_data.get('losses', 0)
        self.max_damage: int = ranked_10x10_data.get('max_damage', 0)
        self.max_damage_tank_id: int = ranked_10x10_data.get('max_damage_tank_id', 0)
        self.max_frags: int = ranked_10x10_data.get('max_frags', 0)
        self.max_frags_tank_id: int = ranked_10x10_data.get('max_frags_tank_id', 0)
        self.max_xp: int = ranked_10x10_data.get('max_xp', 0)
        self.max_xp_tank_id: int = ranked_10x10_data.get('max_xp_tank_id', 0)
        self.no_damage_direct_hits_received: int = ranked_10x10_data.get('no_damage_direct_hits_received', 0)
        self.piercings: int = ranked_10x10_data.get('piercings', 0)
        self.piercings_received: int = ranked_10x10_data.get('piercings_received', 0)
        self.shots: int = ranked_10x10_data.get('shots', 0)
        self.spotted: int = ranked_10x10_data.get('spotted', 0)
        self.stun_assisted_damage: int = ranked_10x10_data.get('stun_assisted_damage', 0)
        self.stun_number: int = ranked_10x10_data.get('stun_number', 0)
        self.survived_battles: int = ranked_10x10_data.get('survived_battles', 0)
        self.tanking_factor: float = ranked_10x10_data.get('tanking_factor', 0.0)
        self.wins: int = ranked_10x10_data.get('wins', 0)
        self.xp: int = ranked_10x10_data.get('xp', 0)

class Ranked15X15Class:
    def __init__(self, ranked_15x15_data: dict):
        if not ranked_15x15_data: ranked_15x15_data = {}
        self._ranked_15x15: dict = ranked_15x15_data
        self.avg_damage_assisted: float = ranked_15x15_data.get('avg_damage_assisted', 0.0)
        self.avg_damage_assisted_radio: float = ranked_15x15_data.get('avg_damage_assisted_radio', 0.0)
        self.avg_damage_assisted_track: float = ranked_15x15_data.get('avg_damage_assisted_track', 0.0)
        self.avg_damage_blocked: float = ranked_15x15_data.get('avg_damage_blocked', 0.0)
        self.battle_avg_xp: int = ranked_15x15_data.get('battle_avg_xp', 0)
        self.battles: int = ranked_15x15_data.get('battles', 0)
        self.battles_on_stunning_vehicles: int = ranked_15x15_data.get('battles_on_stunning_vehicles', 0)
        self.capture_points: int = ranked_15x15_data.get('capture_points', 0)
        self.damage_dealt: int = ranked_15x15_data.get('damage_dealt', 0)
        self.damage_received: int = ranked_15x15_data.get('damage_received', 0)
        self.direct_hits_received: int = ranked_15x15_data.get('direct_hits_received', 0)
        self.draws: int = ranked_15x15_data.get('draws', 0)
        self.dropped_capture_points: int = ranked_15x15_data.get('dropped_capture_points', 0)
        self.explosion_hits: int = ranked_15x15_data.get('explosion_hits', 0)
        self.explosion_hits_received: int = ranked_15x15_data.get('explosion_hits_received', 0)
        self.frags: int = ranked_15x15_data.get('frags', 0)
        self.hits: int = ranked_15x15_data.get('hits', 0)
        self.hits_percents: int = ranked_15x15_data.get('hits_percents', 0)
        self.losses: int = ranked_15x15_data.get('losses', 0)
        self.max_damage: int = ranked_15x15_data.get('max_damage', 0)
        self.max_damage_tank_id: int = ranked_15x15_data.get('max_damage_tank_id', 0)
        self.max_frags: int = ranked_15x15_data.get('max_frags', 0)
        self.max_frags_tank_id: int = ranked_15x15_data.get('max_frags_tank_id', 0)
        self.max_xp: int = ranked_15x15_data.get('max_xp', 0)
        self.max_xp_tank_id: int = ranked_15x15_data.get('max_xp_tank_id', 0)
        self.no_damage_direct_hits_received: int = ranked_15x15_data.get('no_damage_direct_hits_received', 0)
        self.piercings: int = ranked_15x15_data.get('piercings', 0)
        self.piercings_received: int = ranked_15x15_data.get('piercings_received', 0)
        self.shots: int = ranked_15x15_data.get('shots', 0)
        self.spotted: int = ranked_15x15_data.get('spotted', 0)
        self.stun_assisted_damage: int = ranked_15x15_data.get('stun_assisted_damage', 0)
        self.stun_number: int = ranked_15x15_data.get('stun_number', 0)
        self.survived_battles: int = ranked_15x15_data.get('survived_battles', 0)
        self.tanking_factor: float = ranked_15x15_data.get('tanking_factor', 0.0)
        self.wins: int = ranked_15x15_data.get('wins', 0)
        self.xp: int = ranked_15x15_data.get('xp', 0)

class RankedBattlesClass:
    def __init__(self, ranked_battles_data: dict):
        if not ranked_battles_data: ranked_battles_data = {}
        self._ranked_battles: dict = ranked_battles_data
        self.avg_damage_assisted: float = ranked_battles_data.get('avg_damage_assisted', 0.0)
        self.avg_damage_assisted_radio: float = ranked_battles_data.get('avg_damage_assisted_radio', 0.0)
        self.avg_damage_assisted_track: float = ranked_battles_data.get('avg_damage_assisted_track', 0.0)
        self.avg_damage_blocked: float = ranked_battles_data.get('avg_damage_blocked', 0.0)
        self.battle_avg_xp: int = ranked_battles_data.get('battle_avg_xp', 0)
        self.battles: int = ranked_battles_data.get('battles', 0)
        self.battles_on_stunning_vehicles: int = ranked_battles_data.get('battles_on_stunning_vehicles', 0)
        self.capture_points: int = ranked_battles_data.get('capture_points', 0)
        self.damage_dealt: int = ranked_battles_data.get('damage_dealt', 0)
        self.damage_received: int = ranked_battles_data.get('damage_received', 0)
        self.direct_hits_received: int = ranked_battles_data.get('direct_hits_received', 0)
        self.draws: int = ranked_battles_data.get('draws', 0)
        self.dropped_capture_points: int = ranked_battles_data.get('dropped_capture_points', 0)
        self.explosion_hits: int = ranked_battles_data.get('explosion_hits', 0)
        self.explosion_hits_received: int = ranked_battles_data.get('explosion_hits_received', 0)
        self.frags: int = ranked_battles_data.get('frags', 0)
        self.hits: int = ranked_battles_data.get('hits', 0)
        self.hits_percents: int = ranked_battles_data.get('hits_percents', 0)
        self.losses: int = ranked_battles_data.get('losses', 0)
        self.max_damage: int = ranked_battles_data.get('max_damage', 0)
        self.max_damage_tank_id: int = ranked_battles_data.get('max_damage_tank_id', 0)
        self.max_frags: int = ranked_battles_data.get('max_frags', 0)
        self.max_frags_tank_id: int = ranked_battles_data.get('max_frags_tank_id', 0)
        self.max_xp: int = ranked_battles_data.get('max_xp', 0)
        self.max_xp_tank_id: int = ranked_battles_data.get('max_xp_tank_id', 0)
        self.no_damage_direct_hits_received: int = ranked_battles_data.get('no_damage_direct_hits_received', 0)
        self.piercings: int = ranked_battles_data.get('piercings', 0)
        self.piercings_received: int = ranked_battles_data.get('piercings_received', 0)
        self.shots: int = ranked_battles_data.get('shots', 0)
        self.spotted: int = ranked_battles_data.get('spotted', 0)
        self.stun_assisted_damage: int = ranked_battles_data.get('stun_assisted_damage', 0)
        self.stun_number: int = ranked_battles_data.get('stun_number', 0)
        self.survived_battles: int = ranked_battles_data.get('survived_battles', 0)
        self.tanking_factor: float = ranked_battles_data.get('tanking_factor', 0.0)
        self.wins: int = ranked_battles_data.get('wins', 0)
        self.xp: int = ranked_battles_data.get('xp', 0)

class RankedBattlesCurrentClass:
    def __init__(self, ranked_battles_current_data: dict):
        if not ranked_battles_current_data: ranked_battles_current_data = {}
        self._ranked_battles_current: dict = ranked_battles_current_data
        self.avg_damage_assisted: float = ranked_battles_current_data.get('avg_damage_assisted', 0.0)
        self.avg_damage_assisted_radio: float = ranked_battles_current_data.get('avg_damage_assisted_radio', 0.0)
        self.avg_damage_assisted_track: float = ranked_battles_current_data.get('avg_damage_assisted_track', 0.0)
        self.avg_damage_blocked: float = ranked_battles_current_data.get('avg_damage_blocked', 0.0)
        self.battle_avg_xp: int = ranked_battles_current_data.get('battle_avg_xp', 0)
        self.battles: int = ranked_battles_current_data.get('battles', 0)
        self.battles_on_stunning_vehicles: int = ranked_battles_current_data.get('battles_on_stunning_vehicles', 0)
        self.capture_points: int = ranked_battles_current_data.get('capture_points', 0)
        self.damage_dealt: int = ranked_battles_current_data.get('damage_dealt', 0)
        self.damage_received: int = ranked_battles_current_data.get('damage_received', 0)
        self.direct_hits_received: int = ranked_battles_current_data.get('direct_hits_received', 0)
        self.draws: int = ranked_battles_current_data.get('draws', 0)
        self.dropped_capture_points: int = ranked_battles_current_data.get('dropped_capture_points', 0)
        self.explosion_hits: int = ranked_battles_current_data.get('explosion_hits', 0)
        self.explosion_hits_received: int = ranked_battles_current_data.get('explosion_hits_received', 0)
        self.frags: int = ranked_battles_current_data.get('frags', 0)
        self.hits: int = ranked_battles_current_data.get('hits', 0)
        self.hits_percents: int = ranked_battles_current_data.get('hits_percents', 0)
        self.losses: int = ranked_battles_current_data.get('losses', 0)
        self.max_damage: int = ranked_battles_current_data.get('max_damage', 0)
        self.max_damage_tank_id: int = ranked_battles_current_data.get('max_damage_tank_id', 0)
        self.max_frags: int = ranked_battles_current_data.get('max_frags', 0)
        self.max_frags_tank_id: int = ranked_battles_current_data.get('max_frags_tank_id', 0)
        self.max_xp: int = ranked_battles_current_data.get('max_xp', 0)
        self.max_xp_tank_id: int = ranked_battles_current_data.get('max_xp_tank_id', 0)
        self.no_damage_direct_hits_received: int = ranked_battles_current_data.get('no_damage_direct_hits_received', 0)
        self.piercings: int = ranked_battles_current_data.get('piercings', 0)
        self.piercings_received: int = ranked_battles_current_data.get('piercings_received', 0)
        self.shots: int = ranked_battles_current_data.get('shots', 0)
        self.spotted: int = ranked_battles_current_data.get('spotted', 0)
        self.stun_assisted_damage: int = ranked_battles_current_data.get('stun_assisted_damage', 0)
        self.stun_number: int = ranked_battles_current_data.get('stun_number', 0)
        self.survived_battles: int = ranked_battles_current_data.get('survived_battles', 0)
        self.tanking_factor: float = ranked_battles_current_data.get('tanking_factor', 0.0)
        self.wins: int = ranked_battles_current_data.get('wins', 0)
        self.xp: int = ranked_battles_current_data.get('xp', 0)

class RankedBattlesPreviousClass:
    def __init__(self, ranked_battles_previous_data: dict):
        if not ranked_battles_previous_data: ranked_battles_previous_data = {}
        self._ranked_battles_previous: dict = ranked_battles_previous_data
        self.avg_damage_assisted: float = ranked_battles_previous_data.get('avg_damage_assisted', 0.0)
        self.avg_damage_assisted_radio: float = ranked_battles_previous_data.get('avg_damage_assisted_radio', 0.0)
        self.avg_damage_assisted_track: float = ranked_battles_previous_data.get('avg_damage_assisted_track', 0.0)
        self.avg_damage_blocked: float = ranked_battles_previous_data.get('avg_damage_blocked', 0.0)
        self.battle_avg_xp: int = ranked_battles_previous_data.get('battle_avg_xp', 0)
        self.battles: int = ranked_battles_previous_data.get('battles', 0)
        self.battles_on_stunning_vehicles: int = ranked_battles_previous_data.get('battles_on_stunning_vehicles', 0)
        self.capture_points: int = ranked_battles_previous_data.get('capture_points', 0)
        self.damage_dealt: int = ranked_battles_previous_data.get('damage_dealt', 0)
        self.damage_received: int = ranked_battles_previous_data.get('damage_received', 0)
        self.direct_hits_received: int = ranked_battles_previous_data.get('direct_hits_received', 0)
        self.draws: int = ranked_battles_previous_data.get('draws', 0)
        self.dropped_capture_points: int = ranked_battles_previous_data.get('dropped_capture_points', 0)
        self.explosion_hits: int = ranked_battles_previous_data.get('explosion_hits', 0)
        self.explosion_hits_received: int = ranked_battles_previous_data.get('explosion_hits_received', 0)
        self.frags: int = ranked_battles_previous_data.get('frags', 0)
        self.hits: int = ranked_battles_previous_data.get('hits', 0)
        self.hits_percents: int = ranked_battles_previous_data.get('hits_percents', 0)
        self.losses: int = ranked_battles_previous_data.get('losses', 0)
        self.max_damage: int = ranked_battles_previous_data.get('max_damage', 0)
        self.max_damage_tank_id: int = ranked_battles_previous_data.get('max_damage_tank_id', 0)
        self.max_frags: int = ranked_battles_previous_data.get('max_frags', 0)
        self.max_frags_tank_id: int = ranked_battles_previous_data.get('max_frags_tank_id', 0)
        self.max_xp: int = ranked_battles_previous_data.get('max_xp', 0)
        self.max_xp_tank_id: int = ranked_battles_previous_data.get('max_xp_tank_id', 0)
        self.no_damage_direct_hits_received: int = ranked_battles_previous_data.get('no_damage_direct_hits_received', 0)
        self.piercings: int = ranked_battles_previous_data.get('piercings', 0)
        self.piercings_received: int = ranked_battles_previous_data.get('piercings_received', 0)
        self.shots: int = ranked_battles_previous_data.get('shots', 0)
        self.spotted: int = ranked_battles_previous_data.get('spotted', 0)
        self.stun_assisted_damage: int = ranked_battles_previous_data.get('stun_assisted_damage', 0)
        self.stun_number: int = ranked_battles_previous_data.get('stun_number', 0)
        self.survived_battles: int = ranked_battles_previous_data.get('survived_battles', 0)
        self.tanking_factor: float = ranked_battles_previous_data.get('tanking_factor', 0.0)
        self.wins: int = ranked_battles_previous_data.get('wins', 0)
        self.xp: int = ranked_battles_previous_data.get('xp', 0)

class RankedSeason1Class:
    def __init__(self, ranked_season_1_data: dict):
        if not ranked_season_1_data: ranked_season_1_data = {}
        self._ranked_season_1: dict = ranked_season_1_data
        self.avg_damage_assisted: float = ranked_season_1_data.get('avg_damage_assisted', 0.0)
        self.avg_damage_assisted_radio: float = ranked_season_1_data.get('avg_damage_assisted_radio', 0.0)
        self.avg_damage_assisted_track: float = ranked_season_1_data.get('avg_damage_assisted_track', 0.0)
        self.avg_damage_blocked: float = ranked_season_1_data.get('avg_damage_blocked', 0.0)
        self.battle_avg_xp: int = ranked_season_1_data.get('battle_avg_xp', 0)
        self.battles: int = ranked_season_1_data.get('battles', 0)
        self.battles_on_stunning_vehicles: int = ranked_season_1_data.get('battles_on_stunning_vehicles', 0)
        self.capture_points: int = ranked_season_1_data.get('capture_points', 0)
        self.damage_dealt: int = ranked_season_1_data.get('damage_dealt', 0)
        self.damage_received: int = ranked_season_1_data.get('damage_received', 0)
        self.direct_hits_received: int = ranked_season_1_data.get('direct_hits_received', 0)
        self.draws: int = ranked_season_1_data.get('draws', 0)
        self.dropped_capture_points: int = ranked_season_1_data.get('dropped_capture_points', 0)
        self.explosion_hits: int = ranked_season_1_data.get('explosion_hits', 0)
        self.explosion_hits_received: int = ranked_season_1_data.get('explosion_hits_received', 0)
        self.frags: int = ranked_season_1_data.get('frags', 0)
        self.hits: int = ranked_season_1_data.get('hits', 0)
        self.hits_percents: int = ranked_season_1_data.get('hits_percents', 0)
        self.losses: int = ranked_season_1_data.get('losses', 0)
        self.max_damage: int = ranked_season_1_data.get('max_damage', 0)
        self.max_damage_tank_id: int = ranked_season_1_data.get('max_damage_tank_id', 0)
        self.max_frags: int = ranked_season_1_data.get('max_frags', 0)
        self.max_frags_tank_id: int = ranked_season_1_data.get('max_frags_tank_id', 0)
        self.max_xp: int = ranked_season_1_data.get('max_xp', 0)
        self.max_xp_tank_id: int = ranked_season_1_data.get('max_xp_tank_id', 0)
        self.no_damage_direct_hits_received: int = ranked_season_1_data.get('no_damage_direct_hits_received', 0)
        self.piercings: int = ranked_season_1_data.get('piercings', 0)
        self.piercings_received: int = ranked_season_1_data.get('piercings_received', 0)
        self.shots: int = ranked_season_1_data.get('shots', 0)
        self.spotted: int = ranked_season_1_data.get('spotted', 0)
        self.stun_assisted_damage: int = ranked_season_1_data.get('stun_assisted_damage', 0)
        self.stun_number: int = ranked_season_1_data.get('stun_number', 0)
        self.survived_battles: int = ranked_season_1_data.get('survived_battles', 0)
        self.tanking_factor: float = ranked_season_1_data.get('tanking_factor', 0.0)
        self.wins: int = ranked_season_1_data.get('wins', 0)
        self.xp: int = ranked_season_1_data.get('xp', 0)

class RankedSeason2Class:
    def __init__(self, ranked_season_2_data: dict):
        if not ranked_season_2_data: ranked_season_2_data = {}
        self._ranked_season_2: dict = ranked_season_2_data
        self.avg_damage_assisted: float = ranked_season_2_data.get('avg_damage_assisted', 0.0)
        self.avg_damage_assisted_radio: float = ranked_season_2_data.get('avg_damage_assisted_radio', 0.0)
        self.avg_damage_assisted_track: float = ranked_season_2_data.get('avg_damage_assisted_track', 0.0)
        self.avg_damage_blocked: float = ranked_season_2_data.get('avg_damage_blocked', 0.0)
        self.battle_avg_xp: int = ranked_season_2_data.get('battle_avg_xp', 0)
        self.battles: int = ranked_season_2_data.get('battles', 0)
        self.battles_on_stunning_vehicles: int = ranked_season_2_data.get('battles_on_stunning_vehicles', 0)
        self.capture_points: int = ranked_season_2_data.get('capture_points', 0)
        self.damage_dealt: int = ranked_season_2_data.get('damage_dealt', 0)
        self.damage_received: int = ranked_season_2_data.get('damage_received', 0)
        self.direct_hits_received: int = ranked_season_2_data.get('direct_hits_received', 0)
        self.draws: int = ranked_season_2_data.get('draws', 0)
        self.dropped_capture_points: int = ranked_season_2_data.get('dropped_capture_points', 0)
        self.explosion_hits: int = ranked_season_2_data.get('explosion_hits', 0)
        self.explosion_hits_received: int = ranked_season_2_data.get('explosion_hits_received', 0)
        self.frags: int = ranked_season_2_data.get('frags', 0)
        self.hits: int = ranked_season_2_data.get('hits', 0)
        self.hits_percents: int = ranked_season_2_data.get('hits_percents', 0)
        self.losses: int = ranked_season_2_data.get('losses', 0)
        self.max_damage: int = ranked_season_2_data.get('max_damage', 0)
        self.max_damage_tank_id: int = ranked_season_2_data.get('max_damage_tank_id', 0)
        self.max_frags: int = ranked_season_2_data.get('max_frags', 0)
        self.max_frags_tank_id: int = ranked_season_2_data.get('max_frags_tank_id', 0)
        self.max_xp: int = ranked_season_2_data.get('max_xp', 0)
        self.max_xp_tank_id: int = ranked_season_2_data.get('max_xp_tank_id', 0)
        self.no_damage_direct_hits_received: int = ranked_season_2_data.get('no_damage_direct_hits_received', 0)
        self.piercings: int = ranked_season_2_data.get('piercings', 0)
        self.piercings_received: int = ranked_season_2_data.get('piercings_received', 0)
        self.shots: int = ranked_season_2_data.get('shots', 0)
        self.spotted: int = ranked_season_2_data.get('spotted', 0)
        self.stun_assisted_damage: int = ranked_season_2_data.get('stun_assisted_damage', 0)
        self.stun_number: int = ranked_season_2_data.get('stun_number', 0)
        self.survived_battles: int = ranked_season_2_data.get('survived_battles', 0)
        self.tanking_factor: float = ranked_season_2_data.get('tanking_factor', 0.0)
        self.wins: int = ranked_season_2_data.get('wins', 0)
        self.xp: int = ranked_season_2_data.get('xp', 0)

class RankedSeason3Class:
    def __init__(self, ranked_season_3_data: dict):
        if not ranked_season_3_data: ranked_season_3_data = {}
        self._ranked_season_3: dict = ranked_season_3_data
        self.avg_damage_assisted: float = ranked_season_3_data.get('avg_damage_assisted', 0.0)
        self.avg_damage_assisted_radio: float = ranked_season_3_data.get('avg_damage_assisted_radio', 0.0)
        self.avg_damage_assisted_track: float = ranked_season_3_data.get('avg_damage_assisted_track', 0.0)
        self.avg_damage_blocked: float = ranked_season_3_data.get('avg_damage_blocked', 0.0)
        self.battle_avg_xp: int = ranked_season_3_data.get('battle_avg_xp', 0)
        self.battles: int = ranked_season_3_data.get('battles', 0)
        self.battles_on_stunning_vehicles: int = ranked_season_3_data.get('battles_on_stunning_vehicles', 0)
        self.capture_points: int = ranked_season_3_data.get('capture_points', 0)
        self.damage_dealt: int = ranked_season_3_data.get('damage_dealt', 0)
        self.damage_received: int = ranked_season_3_data.get('damage_received', 0)
        self.direct_hits_received: int = ranked_season_3_data.get('direct_hits_received', 0)
        self.draws: int = ranked_season_3_data.get('draws', 0)
        self.dropped_capture_points: int = ranked_season_3_data.get('dropped_capture_points', 0)
        self.explosion_hits: int = ranked_season_3_data.get('explosion_hits', 0)
        self.explosion_hits_received: int = ranked_season_3_data.get('explosion_hits_received', 0)
        self.frags: int = ranked_season_3_data.get('frags', 0)
        self.hits: int = ranked_season_3_data.get('hits', 0)
        self.hits_percents: int = ranked_season_3_data.get('hits_percents', 0)
        self.losses: int = ranked_season_3_data.get('losses', 0)
        self.max_damage: int = ranked_season_3_data.get('max_damage', 0)
        self.max_damage_tank_id: int = ranked_season_3_data.get('max_damage_tank_id', 0)
        self.max_frags: int = ranked_season_3_data.get('max_frags', 0)
        self.max_frags_tank_id: int = ranked_season_3_data.get('max_frags_tank_id', 0)
        self.max_xp: int = ranked_season_3_data.get('max_xp', 0)
        self.max_xp_tank_id: int = ranked_season_3_data.get('max_xp_tank_id', 0)
        self.no_damage_direct_hits_received: int = ranked_season_3_data.get('no_damage_direct_hits_received', 0)
        self.piercings: int = ranked_season_3_data.get('piercings', 0)
        self.piercings_received: int = ranked_season_3_data.get('piercings_received', 0)
        self.shots: int = ranked_season_3_data.get('shots', 0)
        self.spotted: int = ranked_season_3_data.get('spotted', 0)
        self.stun_assisted_damage: int = ranked_season_3_data.get('stun_assisted_damage', 0)
        self.stun_number: int = ranked_season_3_data.get('stun_number', 0)
        self.survived_battles: int = ranked_season_3_data.get('survived_battles', 0)
        self.tanking_factor: float = ranked_season_3_data.get('tanking_factor', 0.0)
        self.wins: int = ranked_season_3_data.get('wins', 0)
        self.xp: int = ranked_season_3_data.get('xp', 0)

class RegularTeamClass:
    def __init__(self, regular_team_data: dict):
        if not regular_team_data: regular_team_data = {}
        self._regular_team: dict = regular_team_data
        self.avg_damage_assisted: float = regular_team_data.get('avg_damage_assisted', 0.0)
        self.avg_damage_assisted_radio: float = regular_team_data.get('avg_damage_assisted_radio', 0.0)
        self.avg_damage_assisted_track: float = regular_team_data.get('avg_damage_assisted_track', 0.0)
        self.avg_damage_blocked: float = regular_team_data.get('avg_damage_blocked', 0.0)
        self.battle_avg_xp: int = regular_team_data.get('battle_avg_xp', 0)
        self.battles: int = regular_team_data.get('battles', 0)
        self.battles_on_stunning_vehicles: int = regular_team_data.get('battles_on_stunning_vehicles', 0)
        self.capture_points: int = regular_team_data.get('capture_points', 0)
        self.damage_dealt: int = regular_team_data.get('damage_dealt', 0)
        self.damage_received: int = regular_team_data.get('damage_received', 0)
        self.direct_hits_received: int = regular_team_data.get('direct_hits_received', 0)
        self.draws: int = regular_team_data.get('draws', 0)
        self.dropped_capture_points: int = regular_team_data.get('dropped_capture_points', 0)
        self.explosion_hits: int = regular_team_data.get('explosion_hits', 0)
        self.explosion_hits_received: int = regular_team_data.get('explosion_hits_received', 0)
        self.frags: int = regular_team_data.get('frags', 0)
        self.hits: int = regular_team_data.get('hits', 0)
        self.hits_percents: int = regular_team_data.get('hits_percents', 0)
        self.losses: int = regular_team_data.get('losses', 0)
        self.max_damage: int = regular_team_data.get('max_damage', 0)
        self.max_damage_tank_id: int = regular_team_data.get('max_damage_tank_id', 0)
        self.max_frags: int = regular_team_data.get('max_frags', 0)
        self.max_frags_tank_id: int = regular_team_data.get('max_frags_tank_id', 0)
        self.max_xp: int = regular_team_data.get('max_xp', 0)
        self.max_xp_tank_id: int = regular_team_data.get('max_xp_tank_id', 0)
        self.no_damage_direct_hits_received: int = regular_team_data.get('no_damage_direct_hits_received', 0)
        self.piercings: int = regular_team_data.get('piercings', 0)
        self.piercings_received: int = regular_team_data.get('piercings_received', 0)
        self.shots: int = regular_team_data.get('shots', 0)
        self.spotted: int = regular_team_data.get('spotted', 0)
        self.stun_assisted_damage: int = regular_team_data.get('stun_assisted_damage', 0)
        self.stun_number: int = regular_team_data.get('stun_number', 0)
        self.survived_battles: int = regular_team_data.get('survived_battles', 0)
        self.tanking_factor: float = regular_team_data.get('tanking_factor', 0.0)
        self.wins: int = regular_team_data.get('wins', 0)
        self.xp: int = regular_team_data.get('xp', 0)

class StrongholdDefenseClass:
    def __init__(self, stronghold_defense_data: dict):
        if not stronghold_defense_data: stronghold_defense_data = {}
        self._stronghold_defense: dict = stronghold_defense_data
        self.battle_avg_xp: int = stronghold_defense_data.get('battle_avg_xp', 0)
        self.battles: int = stronghold_defense_data.get('battles', 0)
        self.battles_on_stunning_vehicles: int = stronghold_defense_data.get('battles_on_stunning_vehicles', 0)
        self.capture_points: int = stronghold_defense_data.get('capture_points', 0)
        self.damage_dealt: int = stronghold_defense_data.get('damage_dealt', 0)
        self.damage_received: int = stronghold_defense_data.get('damage_received', 0)
        self.direct_hits_received: int = stronghold_defense_data.get('direct_hits_received', 0)
        self.draws: int = stronghold_defense_data.get('draws', 0)
        self.dropped_capture_points: int = stronghold_defense_data.get('dropped_capture_points', 0)
        self.explosion_hits: int = stronghold_defense_data.get('explosion_hits', 0)
        self.explosion_hits_received: int = stronghold_defense_data.get('explosion_hits_received', 0)
        self.frags: int = stronghold_defense_data.get('frags', 0)
        self.hits: int = stronghold_defense_data.get('hits', 0)
        self.hits_percents: int = stronghold_defense_data.get('hits_percents', 0)
        self.losses: int = stronghold_defense_data.get('losses', 0)
        self.max_damage: int = stronghold_defense_data.get('max_damage', 0)
        self.max_damage_tank_id: int = stronghold_defense_data.get('max_damage_tank_id', 0)
        self.max_frags: int = stronghold_defense_data.get('max_frags', 0)
        self.max_frags_tank_id: int = stronghold_defense_data.get('max_frags_tank_id', 0)
        self.max_xp: int = stronghold_defense_data.get('max_xp', 0)
        self.max_xp_tank_id: int = stronghold_defense_data.get('max_xp_tank_id', 0)
        self.no_damage_direct_hits_received: int = stronghold_defense_data.get('no_damage_direct_hits_received', 0)
        self.piercings: int = stronghold_defense_data.get('piercings', 0)
        self.piercings_received: int = stronghold_defense_data.get('piercings_received', 0)
        self.shots: int = stronghold_defense_data.get('shots', 0)
        self.spotted: int = stronghold_defense_data.get('spotted', 0)
        self.stun_assisted_damage: int = stronghold_defense_data.get('stun_assisted_damage', 0)
        self.stun_number: int = stronghold_defense_data.get('stun_number', 0)
        self.survived_battles: int = stronghold_defense_data.get('survived_battles', 0)
        self.tanking_factor: float = stronghold_defense_data.get('tanking_factor', 0.0)
        self.wins: int = stronghold_defense_data.get('wins', 0)
        self.xp: int = stronghold_defense_data.get('xp', 0)

class StrongholdSkirmishClass:
    def __init__(self, stronghold_skirmish_data: dict):
        if not stronghold_skirmish_data: stronghold_skirmish_data = {}
        self._stronghold_skirmish: dict = stronghold_skirmish_data
        self.battle_avg_xp: int = stronghold_skirmish_data.get('battle_avg_xp', 0)
        self.battles: int = stronghold_skirmish_data.get('battles', 0)
        self.battles_on_stunning_vehicles: int = stronghold_skirmish_data.get('battles_on_stunning_vehicles', 0)
        self.capture_points: int = stronghold_skirmish_data.get('capture_points', 0)
        self.damage_dealt: int = stronghold_skirmish_data.get('damage_dealt', 0)
        self.damage_received: int = stronghold_skirmish_data.get('damage_received', 0)
        self.direct_hits_received: int = stronghold_skirmish_data.get('direct_hits_received', 0)
        self.draws: int = stronghold_skirmish_data.get('draws', 0)
        self.dropped_capture_points: int = stronghold_skirmish_data.get('dropped_capture_points', 0)
        self.explosion_hits: int = stronghold_skirmish_data.get('explosion_hits', 0)
        self.explosion_hits_received: int = stronghold_skirmish_data.get('explosion_hits_received', 0)
        self.frags: int = stronghold_skirmish_data.get('frags', 0)
        self.hits: int = stronghold_skirmish_data.get('hits', 0)
        self.hits_percents: int = stronghold_skirmish_data.get('hits_percents', 0)
        self.losses: int = stronghold_skirmish_data.get('losses', 0)
        self.max_damage: int = stronghold_skirmish_data.get('max_damage', 0)
        self.max_damage_tank_id: int = stronghold_skirmish_data.get('max_damage_tank_id', 0)
        self.max_frags: int = stronghold_skirmish_data.get('max_frags', 0)
        self.max_frags_tank_id: int = stronghold_skirmish_data.get('max_frags_tank_id', 0)
        self.max_xp: int = stronghold_skirmish_data.get('max_xp', 0)
        self.max_xp_tank_id: int = stronghold_skirmish_data.get('max_xp_tank_id', 0)
        self.no_damage_direct_hits_received: int = stronghold_skirmish_data.get('no_damage_direct_hits_received', 0)
        self.piercings: int = stronghold_skirmish_data.get('piercings', 0)
        self.piercings_received: int = stronghold_skirmish_data.get('piercings_received', 0)
        self.shots: int = stronghold_skirmish_data.get('shots', 0)
        self.spotted: int = stronghold_skirmish_data.get('spotted', 0)
        self.stun_assisted_damage: int = stronghold_skirmish_data.get('stun_assisted_damage', 0)
        self.stun_number: int = stronghold_skirmish_data.get('stun_number', 0)
        self.survived_battles: int = stronghold_skirmish_data.get('survived_battles', 0)
        self.tanking_factor: float = stronghold_skirmish_data.get('tanking_factor', 0.0)
        self.wins: int = stronghold_skirmish_data.get('wins', 0)
        self.xp: int = stronghold_skirmish_data.get('xp', 0)

class TeamClass:
    def __init__(self, team_data: dict):
        if not team_data: team_data = {}
        self._team: dict = team_data
        self.avg_damage_assisted: float = team_data.get('avg_damage_assisted', 0.0)
        self.avg_damage_assisted_radio: float = team_data.get('avg_damage_assisted_radio', 0.0)
        self.avg_damage_assisted_track: float = team_data.get('avg_damage_assisted_track', 0.0)
        self.avg_damage_blocked: float = team_data.get('avg_damage_blocked', 0.0)
        self.battle_avg_xp: int = team_data.get('battle_avg_xp', 0)
        self.battles: int = team_data.get('battles', 0)
        self.battles_on_stunning_vehicles: int = team_data.get('battles_on_stunning_vehicles', 0)
        self.capture_points: int = team_data.get('capture_points', 0)
        self.damage_dealt: int = team_data.get('damage_dealt', 0)
        self.damage_received: int = team_data.get('damage_received', 0)
        self.direct_hits_received: int = team_data.get('direct_hits_received', 0)
        self.draws: int = team_data.get('draws', 0)
        self.dropped_capture_points: int = team_data.get('dropped_capture_points', 0)
        self.explosion_hits: int = team_data.get('explosion_hits', 0)
        self.explosion_hits_received: int = team_data.get('explosion_hits_received', 0)
        self.frags: int = team_data.get('frags', 0)
        self.hits: int = team_data.get('hits', 0)
        self.hits_percents: int = team_data.get('hits_percents', 0)
        self.losses: int = team_data.get('losses', 0)
        self.max_damage: int = team_data.get('max_damage', 0)
        self.max_damage_tank_id: int = team_data.get('max_damage_tank_id', 0)
        self.max_frags: int = team_data.get('max_frags', 0)
        self.max_frags_tank_id: int = team_data.get('max_frags_tank_id', 0)
        self.max_xp: int = team_data.get('max_xp', 0)
        self.max_xp_tank_id: int = team_data.get('max_xp_tank_id', 0)
        self.no_damage_direct_hits_received: int = team_data.get('no_damage_direct_hits_received', 0)
        self.piercings: int = team_data.get('piercings', 0)
        self.piercings_received: int = team_data.get('piercings_received', 0)
        self.shots: int = team_data.get('shots', 0)
        self.spotted: int = team_data.get('spotted', 0)
        self.stun_assisted_damage: int = team_data.get('stun_assisted_damage', 0)
        self.stun_number: int = team_data.get('stun_number', 0)
        self.survived_battles: int = team_data.get('survived_battles', 0)
        self.tanking_factor: float = team_data.get('tanking_factor', 0.0)
        self.wins: int = team_data.get('wins', 0)
        self.xp: int = team_data.get('xp', 0)

class StatisticsClass:
    def __init__(self, statistics_data: dict):
        if not statistics_data: statistics_data = {}
        self._statistics: dict = statistics_data
        self.frags: dict = statistics_data.get('frags', {})
        self.trees_cut: int = statistics_data.get('trees_cut', 0)

        all_temp: dict = self._statistics.get('all')
        all_class = None
        if isinstance(all_temp, dict):
            for key in all_temp:
                if str(key).isnumeric():
                    all_class = {key: AllClass(data) for key, data in all_temp.items()}
                    break
                if key == 'avg_damage_assisted' or key == 'avg_damage_assisted_radio' or key == 'avg_damage_assisted_track' or key == 'avg_damage_blocked' or key == 'battle_avg_xp' or key == 'battles' or key == 'battles_on_stunning_vehicles' or key == 'capture_points' or key == 'damage_dealt' or key == 'damage_received' or key == 'direct_hits_received' or key == 'draws' or key == 'dropped_capture_points' or key == 'explosion_hits' or key == 'explosion_hits_received' or key == 'frags' or key == 'hits' or key == 'hits_percents' or key == 'losses' or key == 'max_damage' or key == 'max_damage_tank_id' or key == 'max_frags' or key == 'max_frags_tank_id' or key == 'max_xp' or key == 'max_xp_tank_id' or key == 'no_damage_direct_hits_received' or key == 'piercings' or key == 'piercings_received' or key == 'shots' or key == 'spotted' or key == 'stun_assisted_damage' or key == 'stun_number' or key == 'survived_battles' or key == 'tanking_factor' or key == 'wins' or key == 'xp':
                    all_class = AllClass(all_temp)
                    break
        elif isinstance(all_temp, list):
            all_class = [AllClass(data) for data in all_temp]
        if not all_class:
            all_class: AllClass = AllClass(all_temp)
        self.all: AllClass | list[AllClass] | dict[str, AllClass] = all_class
        del all_temp, all_class


        clan_temp: dict = self._statistics.get('clan')
        clan_class = None
        if isinstance(clan_temp, dict):
            for key in clan_temp:
                if str(key).isnumeric():
                    clan_class = {key: ClanClass(data) for key, data in clan_temp.items()}
                    break
                if key == 'avg_damage_assisted' or key == 'avg_damage_assisted_radio' or key == 'avg_damage_assisted_track' or key == 'avg_damage_blocked' or key == 'battle_avg_xp' or key == 'battles' or key == 'battles_on_stunning_vehicles' or key == 'capture_points' or key == 'damage_dealt' or key == 'damage_received' or key == 'direct_hits_received' or key == 'draws' or key == 'dropped_capture_points' or key == 'explosion_hits' or key == 'explosion_hits_received' or key == 'frags' or key == 'hits' or key == 'hits_percents' or key == 'losses' or key == 'no_damage_direct_hits_received' or key == 'piercings' or key == 'piercings_received' or key == 'shots' or key == 'spotted' or key == 'stun_assisted_damage' or key == 'stun_number' or key == 'survived_battles' or key == 'tanking_factor' or key == 'wins' or key == 'xp':
                    clan_class = ClanClass(clan_temp)
                    break
        elif isinstance(clan_temp, list):
            clan_class = [ClanClass(data) for data in clan_temp]
        if not clan_class:
            clan_class: ClanClass = ClanClass(clan_temp)
        self.clan: ClanClass | list[ClanClass] | dict[str, ClanClass] = clan_class
        del clan_temp, clan_class


        company_temp: dict = self._statistics.get('company')
        company_class = None
        if isinstance(company_temp, dict):
            for key in company_temp:
                if str(key).isnumeric():
                    company_class = {key: CompanyClass(data) for key, data in company_temp.items()}
                    break
                if key == 'avg_damage_assisted' or key == 'avg_damage_assisted_radio' or key == 'avg_damage_assisted_track' or key == 'avg_damage_blocked' or key == 'battle_avg_xp' or key == 'battles' or key == 'battles_on_stunning_vehicles' or key == 'capture_points' or key == 'damage_dealt' or key == 'damage_received' or key == 'direct_hits_received' or key == 'draws' or key == 'dropped_capture_points' or key == 'explosion_hits' or key == 'explosion_hits_received' or key == 'frags' or key == 'hits' or key == 'hits_percents' or key == 'losses' or key == 'no_damage_direct_hits_received' or key == 'piercings' or key == 'piercings_received' or key == 'shots' or key == 'spotted' or key == 'stun_assisted_damage' or key == 'stun_number' or key == 'survived_battles' or key == 'tanking_factor' or key == 'wins' or key == 'xp':
                    company_class = CompanyClass(company_temp)
                    break
        elif isinstance(company_temp, list):
            company_class = [CompanyClass(data) for data in company_temp]
        if not company_class:
            company_class: CompanyClass = CompanyClass(company_temp)
        self.company: CompanyClass | list[CompanyClass] | dict[str, CompanyClass] = company_class
        del company_temp, company_class


        epic_temp: dict = self._statistics.get('epic')
        epic_class = None
        if isinstance(epic_temp, dict):
            for key in epic_temp:
                if str(key).isnumeric():
                    epic_class = {key: EpicClass(data) for key, data in epic_temp.items()}
                    break
                if key == 'avg_damage_assisted' or key == 'avg_damage_assisted_radio' or key == 'avg_damage_assisted_track' or key == 'avg_damage_blocked' or key == 'battle_avg_xp' or key == 'battles' or key == 'battles_on_stunning_vehicles' or key == 'capture_points' or key == 'damage_dealt' or key == 'damage_received' or key == 'direct_hits_received' or key == 'draws' or key == 'dropped_capture_points' or key == 'explosion_hits' or key == 'explosion_hits_received' or key == 'frags' or key == 'hits' or key == 'hits_percents' or key == 'losses' or key == 'max_damage' or key == 'max_damage_tank_id' or key == 'max_frags' or key == 'max_frags_tank_id' or key == 'max_xp' or key == 'max_xp_tank_id' or key == 'no_damage_direct_hits_received' or key == 'piercings' or key == 'piercings_received' or key == 'shots' or key == 'spotted' or key == 'stun_assisted_damage' or key == 'stun_number' or key == 'survived_battles' or key == 'tanking_factor' or key == 'wins' or key == 'xp':
                    epic_class = EpicClass(epic_temp)
                    break
        elif isinstance(epic_temp, list):
            epic_class = [EpicClass(data) for data in epic_temp]
        if not epic_class:
            epic_class: EpicClass = EpicClass(epic_temp)
        self.epic: EpicClass | list[EpicClass] | dict[str, EpicClass] = epic_class
        del epic_temp, epic_class


        fallout_temp: dict = self._statistics.get('fallout')
        fallout_class = None
        if isinstance(fallout_temp, dict):
            for key in fallout_temp:
                if str(key).isnumeric():
                    fallout_class = {key: FalloutClass(data) for key, data in fallout_temp.items()}
                    break
                if key == 'avatar_damage_dealt' or key == 'avatar_frags' or key == 'avg_damage_assisted' or key == 'avg_damage_assisted_radio' or key == 'avg_damage_assisted_track' or key == 'avg_damage_blocked' or key == 'battle_avg_xp' or key == 'battles' or key == 'battles_on_stunning_vehicles' or key == 'capture_points' or key == 'damage_dealt' or key == 'damage_received' or key == 'death_count' or key == 'direct_hits_received' or key == 'draws' or key == 'dropped_capture_points' or key == 'explosion_hits' or key == 'explosion_hits_received' or key == 'flag_capture' or key == 'flag_capture_solo' or key == 'frags' or key == 'hits' or key == 'hits_percents' or key == 'losses' or key == 'max_damage' or key == 'max_damage_tank_id' or key == 'max_damage_with_avatar' or key == 'max_frags' or key == 'max_frags_tank_id' or key == 'max_frags_with_avatar' or key == 'max_win_points' or key == 'max_xp' or key == 'max_xp_tank_id' or key == 'no_damage_direct_hits_received' or key == 'piercings' or key == 'piercings_received' or key == 'resource_absorbed' or key == 'shots' or key == 'spotted' or key == 'stun_assisted_damage' or key == 'stun_number' or key == 'survived_battles' or key == 'tanking_factor' or key == 'win_points' or key == 'wins' or key == 'xp':
                    fallout_class = FalloutClass(fallout_temp)
                    break
        elif isinstance(fallout_temp, list):
            fallout_class = [FalloutClass(data) for data in fallout_temp]
        if not fallout_class:
            fallout_class: FalloutClass = FalloutClass(fallout_temp)
        self.fallout: FalloutClass | list[FalloutClass] | dict[str, FalloutClass] = fallout_class
        del fallout_temp, fallout_class


        globalmap_absolute_temp: dict = self._statistics.get('globalmap_absolute')
        globalmap_absolute_class = None
        if isinstance(globalmap_absolute_temp, dict):
            for key in globalmap_absolute_temp:
                if str(key).isnumeric():
                    globalmap_absolute_class = {key: GlobalmapAbsoluteClass(data) for key, data in globalmap_absolute_temp.items()}
                    break
                if key == 'avg_damage_assisted' or key == 'avg_damage_assisted_radio' or key == 'avg_damage_assisted_track' or key == 'avg_damage_blocked' or key == 'battle_avg_xp' or key == 'battles' or key == 'battles_on_stunning_vehicles' or key == 'capture_points' or key == 'damage_dealt' or key == 'damage_received' or key == 'direct_hits_received' or key == 'draws' or key == 'dropped_capture_points' or key == 'explosion_hits' or key == 'explosion_hits_received' or key == 'frags' or key == 'hits' or key == 'hits_percents' or key == 'losses' or key == 'no_damage_direct_hits_received' or key == 'piercings' or key == 'piercings_received' or key == 'shots' or key == 'spotted' or key == 'stun_assisted_damage' or key == 'stun_number' or key == 'survived_battles' or key == 'tanking_factor' or key == 'wins' or key == 'xp':
                    globalmap_absolute_class = GlobalmapAbsoluteClass(globalmap_absolute_temp)
                    break
        elif isinstance(globalmap_absolute_temp, list):
            globalmap_absolute_class = [GlobalmapAbsoluteClass(data) for data in globalmap_absolute_temp]
        if not globalmap_absolute_class:
            globalmap_absolute_class: GlobalmapAbsoluteClass = GlobalmapAbsoluteClass(globalmap_absolute_temp)
        self.globalmap_absolute: GlobalmapAbsoluteClass | list[GlobalmapAbsoluteClass] | dict[str, GlobalmapAbsoluteClass] = globalmap_absolute_class
        del globalmap_absolute_temp, globalmap_absolute_class


        globalmap_champion_temp: dict = self._statistics.get('globalmap_champion')
        globalmap_champion_class = None
        if isinstance(globalmap_champion_temp, dict):
            for key in globalmap_champion_temp:
                if str(key).isnumeric():
                    globalmap_champion_class = {key: GlobalmapChampionClass(data) for key, data in globalmap_champion_temp.items()}
                    break
                if key == 'avg_damage_assisted' or key == 'avg_damage_assisted_radio' or key == 'avg_damage_assisted_track' or key == 'avg_damage_blocked' or key == 'battle_avg_xp' or key == 'battles' or key == 'battles_on_stunning_vehicles' or key == 'capture_points' or key == 'damage_dealt' or key == 'damage_received' or key == 'direct_hits_received' or key == 'draws' or key == 'dropped_capture_points' or key == 'explosion_hits' or key == 'explosion_hits_received' or key == 'frags' or key == 'hits' or key == 'hits_percents' or key == 'losses' or key == 'no_damage_direct_hits_received' or key == 'piercings' or key == 'piercings_received' or key == 'shots' or key == 'spotted' or key == 'stun_assisted_damage' or key == 'stun_number' or key == 'survived_battles' or key == 'tanking_factor' or key == 'wins' or key == 'xp':
                    globalmap_champion_class = GlobalmapChampionClass(globalmap_champion_temp)
                    break
        elif isinstance(globalmap_champion_temp, list):
            globalmap_champion_class = [GlobalmapChampionClass(data) for data in globalmap_champion_temp]
        if not globalmap_champion_class:
            globalmap_champion_class: GlobalmapChampionClass = GlobalmapChampionClass(globalmap_champion_temp)
        self.globalmap_champion: GlobalmapChampionClass | list[GlobalmapChampionClass] | dict[str, GlobalmapChampionClass] = globalmap_champion_class
        del globalmap_champion_temp, globalmap_champion_class


        globalmap_middle_temp: dict = self._statistics.get('globalmap_middle')
        globalmap_middle_class = None
        if isinstance(globalmap_middle_temp, dict):
            for key in globalmap_middle_temp:
                if str(key).isnumeric():
                    globalmap_middle_class = {key: GlobalmapMiddleClass(data) for key, data in globalmap_middle_temp.items()}
                    break
                if key == 'avg_damage_assisted' or key == 'avg_damage_assisted_radio' or key == 'avg_damage_assisted_track' or key == 'avg_damage_blocked' or key == 'battle_avg_xp' or key == 'battles' or key == 'battles_on_stunning_vehicles' or key == 'capture_points' or key == 'damage_dealt' or key == 'damage_received' or key == 'direct_hits_received' or key == 'draws' or key == 'dropped_capture_points' or key == 'explosion_hits' or key == 'explosion_hits_received' or key == 'frags' or key == 'hits' or key == 'hits_percents' or key == 'losses' or key == 'no_damage_direct_hits_received' or key == 'piercings' or key == 'piercings_received' or key == 'shots' or key == 'spotted' or key == 'stun_assisted_damage' or key == 'stun_number' or key == 'survived_battles' or key == 'tanking_factor' or key == 'wins' or key == 'xp':
                    globalmap_middle_class = GlobalmapMiddleClass(globalmap_middle_temp)
                    break
        elif isinstance(globalmap_middle_temp, list):
            globalmap_middle_class = [GlobalmapMiddleClass(data) for data in globalmap_middle_temp]
        if not globalmap_middle_class:
            globalmap_middle_class: GlobalmapMiddleClass = GlobalmapMiddleClass(globalmap_middle_temp)
        self.globalmap_middle: GlobalmapMiddleClass | list[GlobalmapMiddleClass] | dict[str, GlobalmapMiddleClass] = globalmap_middle_class
        del globalmap_middle_temp, globalmap_middle_class


        historical_temp: dict = self._statistics.get('historical')
        historical_class = None
        if isinstance(historical_temp, dict):
            for key in historical_temp:
                if str(key).isnumeric():
                    historical_class = {key: HistoricalClass(data) for key, data in historical_temp.items()}
                    break
                if key == 'avg_damage_assisted' or key == 'avg_damage_assisted_radio' or key == 'avg_damage_assisted_track' or key == 'avg_damage_blocked' or key == 'battle_avg_xp' or key == 'battles' or key == 'battles_on_stunning_vehicles' or key == 'capture_points' or key == 'damage_dealt' or key == 'damage_received' or key == 'direct_hits_received' or key == 'draws' or key == 'dropped_capture_points' or key == 'explosion_hits' or key == 'explosion_hits_received' or key == 'frags' or key == 'hits' or key == 'hits_percents' or key == 'losses' or key == 'max_damage' or key == 'max_damage_tank_id' or key == 'max_frags' or key == 'max_frags_tank_id' or key == 'max_xp' or key == 'max_xp_tank_id' or key == 'no_damage_direct_hits_received' or key == 'piercings' or key == 'piercings_received' or key == 'shots' or key == 'spotted' or key == 'stun_assisted_damage' or key == 'stun_number' or key == 'survived_battles' or key == 'tanking_factor' or key == 'wins' or key == 'xp':
                    historical_class = HistoricalClass(historical_temp)
                    break
        elif isinstance(historical_temp, list):
            historical_class = [HistoricalClass(data) for data in historical_temp]
        if not historical_class:
            historical_class: HistoricalClass = HistoricalClass(historical_temp)
        self.historical: HistoricalClass | list[HistoricalClass] | dict[str, HistoricalClass] = historical_class
        del historical_temp, historical_class


        random_temp: dict = self._statistics.get('random')
        random_class = None
        if isinstance(random_temp, dict):
            for key in random_temp:
                if str(key).isnumeric():
                    random_class = {key: RandomClass(data) for key, data in random_temp.items()}
                    break
                if key == 'avg_damage_assisted' or key == 'avg_damage_assisted_radio' or key == 'avg_damage_assisted_track' or key == 'avg_damage_blocked' or key == 'battle_avg_xp' or key == 'battles' or key == 'battles_on_stunning_vehicles' or key == 'capture_points' or key == 'damage_dealt' or key == 'damage_received' or key == 'direct_hits_received' or key == 'draws' or key == 'dropped_capture_points' or key == 'explosion_hits' or key == 'explosion_hits_received' or key == 'frags' or key == 'hits' or key == 'hits_percents' or key == 'losses' or key == 'no_damage_direct_hits_received' or key == 'piercings' or key == 'piercings_received' or key == 'shots' or key == 'spotted' or key == 'stun_assisted_damage' or key == 'stun_number' or key == 'survived_battles' or key == 'tanking_factor' or key == 'wins' or key == 'xp':
                    random_class = RandomClass(random_temp)
                    break
        elif isinstance(random_temp, list):
            random_class = [RandomClass(data) for data in random_temp]
        if not random_class:
            random_class: RandomClass = RandomClass(random_temp)
        self.random: RandomClass | list[RandomClass] | dict[str, RandomClass] = random_class
        del random_temp, random_class


        ranked_10x10_temp: dict = self._statistics.get('ranked_10x10')
        ranked_10x10_class = None
        if isinstance(ranked_10x10_temp, dict):
            for key in ranked_10x10_temp:
                if str(key).isnumeric():
                    ranked_10x10_class = {key: Ranked10X10Class(data) for key, data in ranked_10x10_temp.items()}
                    break
                if key == 'avg_damage_assisted' or key == 'avg_damage_assisted_radio' or key == 'avg_damage_assisted_track' or key == 'avg_damage_blocked' or key == 'battle_avg_xp' or key == 'battles' or key == 'battles_on_stunning_vehicles' or key == 'capture_points' or key == 'damage_dealt' or key == 'damage_received' or key == 'direct_hits_received' or key == 'draws' or key == 'dropped_capture_points' or key == 'explosion_hits' or key == 'explosion_hits_received' or key == 'frags' or key == 'hits' or key == 'hits_percents' or key == 'losses' or key == 'max_damage' or key == 'max_damage_tank_id' or key == 'max_frags' or key == 'max_frags_tank_id' or key == 'max_xp' or key == 'max_xp_tank_id' or key == 'no_damage_direct_hits_received' or key == 'piercings' or key == 'piercings_received' or key == 'shots' or key == 'spotted' or key == 'stun_assisted_damage' or key == 'stun_number' or key == 'survived_battles' or key == 'tanking_factor' or key == 'wins' or key == 'xp':
                    ranked_10x10_class = Ranked10X10Class(ranked_10x10_temp)
                    break
        elif isinstance(ranked_10x10_temp, list):
            ranked_10x10_class = [Ranked10X10Class(data) for data in ranked_10x10_temp]
        if not ranked_10x10_class:
            ranked_10x10_class: Ranked10X10Class = Ranked10X10Class(ranked_10x10_temp)
        self.ranked_10x10: Ranked10X10Class | list[Ranked10X10Class] | dict[str, Ranked10X10Class] = ranked_10x10_class
        del ranked_10x10_temp, ranked_10x10_class


        ranked_15x15_temp: dict = self._statistics.get('ranked_15x15')
        ranked_15x15_class = None
        if isinstance(ranked_15x15_temp, dict):
            for key in ranked_15x15_temp:
                if str(key).isnumeric():
                    ranked_15x15_class = {key: Ranked15X15Class(data) for key, data in ranked_15x15_temp.items()}
                    break
                if key == 'avg_damage_assisted' or key == 'avg_damage_assisted_radio' or key == 'avg_damage_assisted_track' or key == 'avg_damage_blocked' or key == 'battle_avg_xp' or key == 'battles' or key == 'battles_on_stunning_vehicles' or key == 'capture_points' or key == 'damage_dealt' or key == 'damage_received' or key == 'direct_hits_received' or key == 'draws' or key == 'dropped_capture_points' or key == 'explosion_hits' or key == 'explosion_hits_received' or key == 'frags' or key == 'hits' or key == 'hits_percents' or key == 'losses' or key == 'max_damage' or key == 'max_damage_tank_id' or key == 'max_frags' or key == 'max_frags_tank_id' or key == 'max_xp' or key == 'max_xp_tank_id' or key == 'no_damage_direct_hits_received' or key == 'piercings' or key == 'piercings_received' or key == 'shots' or key == 'spotted' or key == 'stun_assisted_damage' or key == 'stun_number' or key == 'survived_battles' or key == 'tanking_factor' or key == 'wins' or key == 'xp':
                    ranked_15x15_class = Ranked15X15Class(ranked_15x15_temp)
                    break
        elif isinstance(ranked_15x15_temp, list):
            ranked_15x15_class = [Ranked15X15Class(data) for data in ranked_15x15_temp]
        if not ranked_15x15_class:
            ranked_15x15_class: Ranked15X15Class = Ranked15X15Class(ranked_15x15_temp)
        self.ranked_15x15: Ranked15X15Class | list[Ranked15X15Class] | dict[str, Ranked15X15Class] = ranked_15x15_class
        del ranked_15x15_temp, ranked_15x15_class


        ranked_battles_temp: dict = self._statistics.get('ranked_battles')
        ranked_battles_class = None
        if isinstance(ranked_battles_temp, dict):
            for key in ranked_battles_temp:
                if str(key).isnumeric():
                    ranked_battles_class = {key: RankedBattlesClass(data) for key, data in ranked_battles_temp.items()}
                    break
                if key == 'avg_damage_assisted' or key == 'avg_damage_assisted_radio' or key == 'avg_damage_assisted_track' or key == 'avg_damage_blocked' or key == 'battle_avg_xp' or key == 'battles' or key == 'battles_on_stunning_vehicles' or key == 'capture_points' or key == 'damage_dealt' or key == 'damage_received' or key == 'direct_hits_received' or key == 'draws' or key == 'dropped_capture_points' or key == 'explosion_hits' or key == 'explosion_hits_received' or key == 'frags' or key == 'hits' or key == 'hits_percents' or key == 'losses' or key == 'max_damage' or key == 'max_damage_tank_id' or key == 'max_frags' or key == 'max_frags_tank_id' or key == 'max_xp' or key == 'max_xp_tank_id' or key == 'no_damage_direct_hits_received' or key == 'piercings' or key == 'piercings_received' or key == 'shots' or key == 'spotted' or key == 'stun_assisted_damage' or key == 'stun_number' or key == 'survived_battles' or key == 'tanking_factor' or key == 'wins' or key == 'xp':
                    ranked_battles_class = RankedBattlesClass(ranked_battles_temp)
                    break
        elif isinstance(ranked_battles_temp, list):
            ranked_battles_class = [RankedBattlesClass(data) for data in ranked_battles_temp]
        if not ranked_battles_class:
            ranked_battles_class: RankedBattlesClass = RankedBattlesClass(ranked_battles_temp)
        self.ranked_battles: RankedBattlesClass | list[RankedBattlesClass] | dict[str, RankedBattlesClass] = ranked_battles_class
        del ranked_battles_temp, ranked_battles_class


        ranked_battles_current_temp: dict = self._statistics.get('ranked_battles_current')
        ranked_battles_current_class = None
        if isinstance(ranked_battles_current_temp, dict):
            for key in ranked_battles_current_temp:
                if str(key).isnumeric():
                    ranked_battles_current_class = {key: RankedBattlesCurrentClass(data) for key, data in ranked_battles_current_temp.items()}
                    break
                if key == 'avg_damage_assisted' or key == 'avg_damage_assisted_radio' or key == 'avg_damage_assisted_track' or key == 'avg_damage_blocked' or key == 'battle_avg_xp' or key == 'battles' or key == 'battles_on_stunning_vehicles' or key == 'capture_points' or key == 'damage_dealt' or key == 'damage_received' or key == 'direct_hits_received' or key == 'draws' or key == 'dropped_capture_points' or key == 'explosion_hits' or key == 'explosion_hits_received' or key == 'frags' or key == 'hits' or key == 'hits_percents' or key == 'losses' or key == 'max_damage' or key == 'max_damage_tank_id' or key == 'max_frags' or key == 'max_frags_tank_id' or key == 'max_xp' or key == 'max_xp_tank_id' or key == 'no_damage_direct_hits_received' or key == 'piercings' or key == 'piercings_received' or key == 'shots' or key == 'spotted' or key == 'stun_assisted_damage' or key == 'stun_number' or key == 'survived_battles' or key == 'tanking_factor' or key == 'wins' or key == 'xp':
                    ranked_battles_current_class = RankedBattlesCurrentClass(ranked_battles_current_temp)
                    break
        elif isinstance(ranked_battles_current_temp, list):
            ranked_battles_current_class = [RankedBattlesCurrentClass(data) for data in ranked_battles_current_temp]
        if not ranked_battles_current_class:
            ranked_battles_current_class: RankedBattlesCurrentClass = RankedBattlesCurrentClass(ranked_battles_current_temp)
        self.ranked_battles_current: RankedBattlesCurrentClass | list[RankedBattlesCurrentClass] | dict[str, RankedBattlesCurrentClass] = ranked_battles_current_class
        del ranked_battles_current_temp, ranked_battles_current_class


        ranked_battles_previous_temp: dict = self._statistics.get('ranked_battles_previous')
        ranked_battles_previous_class = None
        if isinstance(ranked_battles_previous_temp, dict):
            for key in ranked_battles_previous_temp:
                if str(key).isnumeric():
                    ranked_battles_previous_class = {key: RankedBattlesPreviousClass(data) for key, data in ranked_battles_previous_temp.items()}
                    break
                if key == 'avg_damage_assisted' or key == 'avg_damage_assisted_radio' or key == 'avg_damage_assisted_track' or key == 'avg_damage_blocked' or key == 'battle_avg_xp' or key == 'battles' or key == 'battles_on_stunning_vehicles' or key == 'capture_points' or key == 'damage_dealt' or key == 'damage_received' or key == 'direct_hits_received' or key == 'draws' or key == 'dropped_capture_points' or key == 'explosion_hits' or key == 'explosion_hits_received' or key == 'frags' or key == 'hits' or key == 'hits_percents' or key == 'losses' or key == 'max_damage' or key == 'max_damage_tank_id' or key == 'max_frags' or key == 'max_frags_tank_id' or key == 'max_xp' or key == 'max_xp_tank_id' or key == 'no_damage_direct_hits_received' or key == 'piercings' or key == 'piercings_received' or key == 'shots' or key == 'spotted' or key == 'stun_assisted_damage' or key == 'stun_number' or key == 'survived_battles' or key == 'tanking_factor' or key == 'wins' or key == 'xp':
                    ranked_battles_previous_class = RankedBattlesPreviousClass(ranked_battles_previous_temp)
                    break
        elif isinstance(ranked_battles_previous_temp, list):
            ranked_battles_previous_class = [RankedBattlesPreviousClass(data) for data in ranked_battles_previous_temp]
        if not ranked_battles_previous_class:
            ranked_battles_previous_class: RankedBattlesPreviousClass = RankedBattlesPreviousClass(ranked_battles_previous_temp)
        self.ranked_battles_previous: RankedBattlesPreviousClass | list[RankedBattlesPreviousClass] | dict[str, RankedBattlesPreviousClass] = ranked_battles_previous_class
        del ranked_battles_previous_temp, ranked_battles_previous_class


        ranked_season_1_temp: dict = self._statistics.get('ranked_season_1')
        ranked_season_1_class = None
        if isinstance(ranked_season_1_temp, dict):
            for key in ranked_season_1_temp:
                if str(key).isnumeric():
                    ranked_season_1_class = {key: RankedSeason1Class(data) for key, data in ranked_season_1_temp.items()}
                    break
                if key == 'avg_damage_assisted' or key == 'avg_damage_assisted_radio' or key == 'avg_damage_assisted_track' or key == 'avg_damage_blocked' or key == 'battle_avg_xp' or key == 'battles' or key == 'battles_on_stunning_vehicles' or key == 'capture_points' or key == 'damage_dealt' or key == 'damage_received' or key == 'direct_hits_received' or key == 'draws' or key == 'dropped_capture_points' or key == 'explosion_hits' or key == 'explosion_hits_received' or key == 'frags' or key == 'hits' or key == 'hits_percents' or key == 'losses' or key == 'max_damage' or key == 'max_damage_tank_id' or key == 'max_frags' or key == 'max_frags_tank_id' or key == 'max_xp' or key == 'max_xp_tank_id' or key == 'no_damage_direct_hits_received' or key == 'piercings' or key == 'piercings_received' or key == 'shots' or key == 'spotted' or key == 'stun_assisted_damage' or key == 'stun_number' or key == 'survived_battles' or key == 'tanking_factor' or key == 'wins' or key == 'xp':
                    ranked_season_1_class = RankedSeason1Class(ranked_season_1_temp)
                    break
        elif isinstance(ranked_season_1_temp, list):
            ranked_season_1_class = [RankedSeason1Class(data) for data in ranked_season_1_temp]
        if not ranked_season_1_class:
            ranked_season_1_class: RankedSeason1Class = RankedSeason1Class(ranked_season_1_temp)
        self.ranked_season_1: RankedSeason1Class | list[RankedSeason1Class] | dict[str, RankedSeason1Class] = ranked_season_1_class
        del ranked_season_1_temp, ranked_season_1_class


        ranked_season_2_temp: dict = self._statistics.get('ranked_season_2')
        ranked_season_2_class = None
        if isinstance(ranked_season_2_temp, dict):
            for key in ranked_season_2_temp:
                if str(key).isnumeric():
                    ranked_season_2_class = {key: RankedSeason2Class(data) for key, data in ranked_season_2_temp.items()}
                    break
                if key == 'avg_damage_assisted' or key == 'avg_damage_assisted_radio' or key == 'avg_damage_assisted_track' or key == 'avg_damage_blocked' or key == 'battle_avg_xp' or key == 'battles' or key == 'battles_on_stunning_vehicles' or key == 'capture_points' or key == 'damage_dealt' or key == 'damage_received' or key == 'direct_hits_received' or key == 'draws' or key == 'dropped_capture_points' or key == 'explosion_hits' or key == 'explosion_hits_received' or key == 'frags' or key == 'hits' or key == 'hits_percents' or key == 'losses' or key == 'max_damage' or key == 'max_damage_tank_id' or key == 'max_frags' or key == 'max_frags_tank_id' or key == 'max_xp' or key == 'max_xp_tank_id' or key == 'no_damage_direct_hits_received' or key == 'piercings' or key == 'piercings_received' or key == 'shots' or key == 'spotted' or key == 'stun_assisted_damage' or key == 'stun_number' or key == 'survived_battles' or key == 'tanking_factor' or key == 'wins' or key == 'xp':
                    ranked_season_2_class = RankedSeason2Class(ranked_season_2_temp)
                    break
        elif isinstance(ranked_season_2_temp, list):
            ranked_season_2_class = [RankedSeason2Class(data) for data in ranked_season_2_temp]
        if not ranked_season_2_class:
            ranked_season_2_class: RankedSeason2Class = RankedSeason2Class(ranked_season_2_temp)
        self.ranked_season_2: RankedSeason2Class | list[RankedSeason2Class] | dict[str, RankedSeason2Class] = ranked_season_2_class
        del ranked_season_2_temp, ranked_season_2_class


        ranked_season_3_temp: dict = self._statistics.get('ranked_season_3')
        ranked_season_3_class = None
        if isinstance(ranked_season_3_temp, dict):
            for key in ranked_season_3_temp:
                if str(key).isnumeric():
                    ranked_season_3_class = {key: RankedSeason3Class(data) for key, data in ranked_season_3_temp.items()}
                    break
                if key == 'avg_damage_assisted' or key == 'avg_damage_assisted_radio' or key == 'avg_damage_assisted_track' or key == 'avg_damage_blocked' or key == 'battle_avg_xp' or key == 'battles' or key == 'battles_on_stunning_vehicles' or key == 'capture_points' or key == 'damage_dealt' or key == 'damage_received' or key == 'direct_hits_received' or key == 'draws' or key == 'dropped_capture_points' or key == 'explosion_hits' or key == 'explosion_hits_received' or key == 'frags' or key == 'hits' or key == 'hits_percents' or key == 'losses' or key == 'max_damage' or key == 'max_damage_tank_id' or key == 'max_frags' or key == 'max_frags_tank_id' or key == 'max_xp' or key == 'max_xp_tank_id' or key == 'no_damage_direct_hits_received' or key == 'piercings' or key == 'piercings_received' or key == 'shots' or key == 'spotted' or key == 'stun_assisted_damage' or key == 'stun_number' or key == 'survived_battles' or key == 'tanking_factor' or key == 'wins' or key == 'xp':
                    ranked_season_3_class = RankedSeason3Class(ranked_season_3_temp)
                    break
        elif isinstance(ranked_season_3_temp, list):
            ranked_season_3_class = [RankedSeason3Class(data) for data in ranked_season_3_temp]
        if not ranked_season_3_class:
            ranked_season_3_class: RankedSeason3Class = RankedSeason3Class(ranked_season_3_temp)
        self.ranked_season_3: RankedSeason3Class | list[RankedSeason3Class] | dict[str, RankedSeason3Class] = ranked_season_3_class
        del ranked_season_3_temp, ranked_season_3_class


        regular_team_temp: dict = self._statistics.get('regular_team')
        regular_team_class = None
        if isinstance(regular_team_temp, dict):
            for key in regular_team_temp:
                if str(key).isnumeric():
                    regular_team_class = {key: RegularTeamClass(data) for key, data in regular_team_temp.items()}
                    break
                if key == 'avg_damage_assisted' or key == 'avg_damage_assisted_radio' or key == 'avg_damage_assisted_track' or key == 'avg_damage_blocked' or key == 'battle_avg_xp' or key == 'battles' or key == 'battles_on_stunning_vehicles' or key == 'capture_points' or key == 'damage_dealt' or key == 'damage_received' or key == 'direct_hits_received' or key == 'draws' or key == 'dropped_capture_points' or key == 'explosion_hits' or key == 'explosion_hits_received' or key == 'frags' or key == 'hits' or key == 'hits_percents' or key == 'losses' or key == 'max_damage' or key == 'max_damage_tank_id' or key == 'max_frags' or key == 'max_frags_tank_id' or key == 'max_xp' or key == 'max_xp_tank_id' or key == 'no_damage_direct_hits_received' or key == 'piercings' or key == 'piercings_received' or key == 'shots' or key == 'spotted' or key == 'stun_assisted_damage' or key == 'stun_number' or key == 'survived_battles' or key == 'tanking_factor' or key == 'wins' or key == 'xp':
                    regular_team_class = RegularTeamClass(regular_team_temp)
                    break
        elif isinstance(regular_team_temp, list):
            regular_team_class = [RegularTeamClass(data) for data in regular_team_temp]
        if not regular_team_class:
            regular_team_class: RegularTeamClass = RegularTeamClass(regular_team_temp)
        self.regular_team: RegularTeamClass | list[RegularTeamClass] | dict[str, RegularTeamClass] = regular_team_class
        del regular_team_temp, regular_team_class


        stronghold_defense_temp: dict = self._statistics.get('stronghold_defense')
        stronghold_defense_class = None
        if isinstance(stronghold_defense_temp, dict):
            for key in stronghold_defense_temp:
                if str(key).isnumeric():
                    stronghold_defense_class = {key: StrongholdDefenseClass(data) for key, data in stronghold_defense_temp.items()}
                    break
                if key == 'battle_avg_xp' or key == 'battles' or key == 'battles_on_stunning_vehicles' or key == 'capture_points' or key == 'damage_dealt' or key == 'damage_received' or key == 'direct_hits_received' or key == 'draws' or key == 'dropped_capture_points' or key == 'explosion_hits' or key == 'explosion_hits_received' or key == 'frags' or key == 'hits' or key == 'hits_percents' or key == 'losses' or key == 'max_damage' or key == 'max_damage_tank_id' or key == 'max_frags' or key == 'max_frags_tank_id' or key == 'max_xp' or key == 'max_xp_tank_id' or key == 'no_damage_direct_hits_received' or key == 'piercings' or key == 'piercings_received' or key == 'shots' or key == 'spotted' or key == 'stun_assisted_damage' or key == 'stun_number' or key == 'survived_battles' or key == 'tanking_factor' or key == 'wins' or key == 'xp':
                    stronghold_defense_class = StrongholdDefenseClass(stronghold_defense_temp)
                    break
        elif isinstance(stronghold_defense_temp, list):
            stronghold_defense_class = [StrongholdDefenseClass(data) for data in stronghold_defense_temp]
        if not stronghold_defense_class:
            stronghold_defense_class: StrongholdDefenseClass = StrongholdDefenseClass(stronghold_defense_temp)
        self.stronghold_defense: StrongholdDefenseClass | list[StrongholdDefenseClass] | dict[str, StrongholdDefenseClass] = stronghold_defense_class
        del stronghold_defense_temp, stronghold_defense_class


        stronghold_skirmish_temp: dict = self._statistics.get('stronghold_skirmish')
        stronghold_skirmish_class = None
        if isinstance(stronghold_skirmish_temp, dict):
            for key in stronghold_skirmish_temp:
                if str(key).isnumeric():
                    stronghold_skirmish_class = {key: StrongholdSkirmishClass(data) for key, data in stronghold_skirmish_temp.items()}
                    break
                if key == 'battle_avg_xp' or key == 'battles' or key == 'battles_on_stunning_vehicles' or key == 'capture_points' or key == 'damage_dealt' or key == 'damage_received' or key == 'direct_hits_received' or key == 'draws' or key == 'dropped_capture_points' or key == 'explosion_hits' or key == 'explosion_hits_received' or key == 'frags' or key == 'hits' or key == 'hits_percents' or key == 'losses' or key == 'max_damage' or key == 'max_damage_tank_id' or key == 'max_frags' or key == 'max_frags_tank_id' or key == 'max_xp' or key == 'max_xp_tank_id' or key == 'no_damage_direct_hits_received' or key == 'piercings' or key == 'piercings_received' or key == 'shots' or key == 'spotted' or key == 'stun_assisted_damage' or key == 'stun_number' or key == 'survived_battles' or key == 'tanking_factor' or key == 'wins' or key == 'xp':
                    stronghold_skirmish_class = StrongholdSkirmishClass(stronghold_skirmish_temp)
                    break
        elif isinstance(stronghold_skirmish_temp, list):
            stronghold_skirmish_class = [StrongholdSkirmishClass(data) for data in stronghold_skirmish_temp]
        if not stronghold_skirmish_class:
            stronghold_skirmish_class: StrongholdSkirmishClass = StrongholdSkirmishClass(stronghold_skirmish_temp)
        self.stronghold_skirmish: StrongholdSkirmishClass | list[StrongholdSkirmishClass] | dict[str, StrongholdSkirmishClass] = stronghold_skirmish_class
        del stronghold_skirmish_temp, stronghold_skirmish_class


        team_temp: dict = self._statistics.get('team')
        team_class = None
        if isinstance(team_temp, dict):
            for key in team_temp:
                if str(key).isnumeric():
                    team_class = {key: TeamClass(data) for key, data in team_temp.items()}
                    break
                if key == 'avg_damage_assisted' or key == 'avg_damage_assisted_radio' or key == 'avg_damage_assisted_track' or key == 'avg_damage_blocked' or key == 'battle_avg_xp' or key == 'battles' or key == 'battles_on_stunning_vehicles' or key == 'capture_points' or key == 'damage_dealt' or key == 'damage_received' or key == 'direct_hits_received' or key == 'draws' or key == 'dropped_capture_points' or key == 'explosion_hits' or key == 'explosion_hits_received' or key == 'frags' or key == 'hits' or key == 'hits_percents' or key == 'losses' or key == 'max_damage' or key == 'max_damage_tank_id' or key == 'max_frags' or key == 'max_frags_tank_id' or key == 'max_xp' or key == 'max_xp_tank_id' or key == 'no_damage_direct_hits_received' or key == 'piercings' or key == 'piercings_received' or key == 'shots' or key == 'spotted' or key == 'stun_assisted_damage' or key == 'stun_number' or key == 'survived_battles' or key == 'tanking_factor' or key == 'wins' or key == 'xp':
                    team_class = TeamClass(team_temp)
                    break
        elif isinstance(team_temp, list):
            team_class = [TeamClass(data) for data in team_temp]
        if not team_class:
            team_class: TeamClass = TeamClass(team_temp)
        self.team: TeamClass | list[TeamClass] | dict[str, TeamClass] = team_class
        del team_temp, team_class


class AccountInfoClass:
    def __init__(self, account_info_data: dict):
        if not account_info_data: account_info_data = {}
        self._account_info: dict = account_info_data
        self.account_id: int = account_info_data.get('account_id', 0)
        self.clan_id: int = account_info_data.get('clan_id', 0)
        self.client_language: str = account_info_data.get('client_language', '')
        self.created_at: int = account_info_data.get('created_at', 0)
        self.global_rating: int = account_info_data.get('global_rating', 0)
        self.last_battle_time: int = account_info_data.get('last_battle_time', 0)
        self.logout_at: int = account_info_data.get('logout_at', 0)
        self.nickname: str = account_info_data.get('nickname', '')
        self.updated_at: int = account_info_data.get('updated_at', 0)

        private_temp: dict = self._account_info.get('private')
        private_class = None
        if isinstance(private_temp, dict):
            for key in private_temp:
                if str(key).isnumeric():
                    private_class = {key: PrivateClass(data) for key, data in private_temp.items()}
                    break
                if key == 'ban_info' or key == 'ban_time' or key == 'battle_life_time' or key == 'bonds' or key == 'credits' or key == 'free_xp' or key == 'garage' or key == 'gold' or key == 'is_bound_to_phone' or key == 'is_premium' or key == 'personal_missions' or key == 'premium_expires_at' or key == 'boosters' or key == 'grouped_contacts' or key == 'rented' or key == 'restrictions':
                    private_class = PrivateClass(private_temp)
                    break
        elif isinstance(private_temp, list):
            private_class = [PrivateClass(data) for data in private_temp]
        if not private_class:
            private_class: PrivateClass = PrivateClass(private_temp)
        self.private: PrivateClass | list[PrivateClass] | dict[str, PrivateClass] = private_class
        del private_temp, private_class


        statistics_temp: dict = self._account_info.get('statistics')
        statistics_class = None
        if isinstance(statistics_temp, dict):
            for key in statistics_temp:
                if str(key).isnumeric():
                    statistics_class = {key: StatisticsClass(data) for key, data in statistics_temp.items()}
                    break
                if key == 'frags' or key == 'trees_cut' or key == 'all' or key == 'clan' or key == 'company' or key == 'epic' or key == 'fallout' or key == 'globalmap_absolute' or key == 'globalmap_champion' or key == 'globalmap_middle' or key == 'historical' or key == 'random' or key == 'ranked_10x10' or key == 'ranked_15x15' or key == 'ranked_battles' or key == 'ranked_battles_current' or key == 'ranked_battles_previous' or key == 'ranked_season_1' or key == 'ranked_season_2' or key == 'ranked_season_3' or key == 'regular_team' or key == 'stronghold_defense' or key == 'stronghold_skirmish' or key == 'team':
                    statistics_class = StatisticsClass(statistics_temp)
                    break
        elif isinstance(statistics_temp, list):
            statistics_class = [StatisticsClass(data) for data in statistics_temp]
        if not statistics_class:
            statistics_class: StatisticsClass = StatisticsClass(statistics_temp)
        self.statistics: StatisticsClass | list[StatisticsClass] | dict[str, StatisticsClass] = statistics_class
        del statistics_temp, statistics_class


