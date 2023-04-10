class AllClass:
    def __init__(self, all_data: dict):
        if not all_data: all_data = {}
        self._all: dict = all_data
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
        self.battle_avg_xp: int = clan_data.get('battle_avg_xp', 0)
        self.battles: int = clan_data.get('battles', 0)
        self.battles_on_stunning_vehicles: int = clan_data.get('battles_on_stunning_vehicles', 0)
        self.capture_points: int = clan_data.get('capture_points', 0)
        self.damage_dealt: int = clan_data.get('damage_dealt', 0)
        self.damage_received: int = clan_data.get('damage_received', 0)
        self.draws: int = clan_data.get('draws', 0)
        self.dropped_capture_points: int = clan_data.get('dropped_capture_points', 0)
        self.frags: int = clan_data.get('frags', 0)
        self.hits: int = clan_data.get('hits', 0)
        self.hits_percents: int = clan_data.get('hits_percents', 0)
        self.losses: int = clan_data.get('losses', 0)
        self.max_damage: int = clan_data.get('max_damage', 0)
        self.max_frags: int = clan_data.get('max_frags', 0)
        self.max_xp: int = clan_data.get('max_xp', 0)
        self.shots: int = clan_data.get('shots', 0)
        self.spotted: int = clan_data.get('spotted', 0)
        self.stun_assisted_damage: int = clan_data.get('stun_assisted_damage', 0)
        self.stun_number: int = clan_data.get('stun_number', 0)
        self.survived_battles: int = clan_data.get('survived_battles', 0)
        self.wins: int = clan_data.get('wins', 0)
        self.xp: int = clan_data.get('xp', 0)

class CompanyClass:
    def __init__(self, company_data: dict):
        if not company_data: company_data = {}
        self._company: dict = company_data
        self.battle_avg_xp: int = company_data.get('battle_avg_xp', 0)
        self.battles: int = company_data.get('battles', 0)
        self.battles_on_stunning_vehicles: int = company_data.get('battles_on_stunning_vehicles', 0)
        self.capture_points: int = company_data.get('capture_points', 0)
        self.damage_dealt: int = company_data.get('damage_dealt', 0)
        self.damage_received: int = company_data.get('damage_received', 0)
        self.draws: int = company_data.get('draws', 0)
        self.dropped_capture_points: int = company_data.get('dropped_capture_points', 0)
        self.frags: int = company_data.get('frags', 0)
        self.hits: int = company_data.get('hits', 0)
        self.hits_percents: int = company_data.get('hits_percents', 0)
        self.losses: int = company_data.get('losses', 0)
        self.shots: int = company_data.get('shots', 0)
        self.spotted: int = company_data.get('spotted', 0)
        self.stun_assisted_damage: int = company_data.get('stun_assisted_damage', 0)
        self.stun_number: int = company_data.get('stun_number', 0)
        self.survived_battles: int = company_data.get('survived_battles', 0)
        self.wins: int = company_data.get('wins', 0)
        self.xp: int = company_data.get('xp', 0)

class EpicClass:
    def __init__(self, epic_data: dict):
        if not epic_data: epic_data = {}
        self._epic: dict = epic_data
        self.battle_avg_xp: int = epic_data.get('battle_avg_xp', 0)
        self.battles: int = epic_data.get('battles', 0)
        self.battles_on_stunning_vehicles: int = epic_data.get('battles_on_stunning_vehicles', 0)
        self.capture_points: int = epic_data.get('capture_points', 0)
        self.damage_dealt: int = epic_data.get('damage_dealt', 0)
        self.damage_received: int = epic_data.get('damage_received', 0)
        self.draws: int = epic_data.get('draws', 0)
        self.dropped_capture_points: int = epic_data.get('dropped_capture_points', 0)
        self.frags: int = epic_data.get('frags', 0)
        self.hits: int = epic_data.get('hits', 0)
        self.hits_percents: int = epic_data.get('hits_percents', 0)
        self.losses: int = epic_data.get('losses', 0)
        self.max_damage: int = epic_data.get('max_damage', 0)
        self.max_frags: int = epic_data.get('max_frags', 0)
        self.max_xp: int = epic_data.get('max_xp', 0)
        self.shots: int = epic_data.get('shots', 0)
        self.spotted: int = epic_data.get('spotted', 0)
        self.stun_assisted_damage: int = epic_data.get('stun_assisted_damage', 0)
        self.stun_number: int = epic_data.get('stun_number', 0)
        self.survived_battles: int = epic_data.get('survived_battles', 0)
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
        self.max_damage_with_avatar: int = fallout_data.get('max_damage_with_avatar', 0)
        self.max_frags: int = fallout_data.get('max_frags', 0)
        self.max_frags_with_avatar: int = fallout_data.get('max_frags_with_avatar', 0)
        self.max_win_points: int = fallout_data.get('max_win_points', 0)
        self.max_xp: int = fallout_data.get('max_xp', 0)
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

class GlobalmapClass:
    def __init__(self, globalmap_data: dict):
        if not globalmap_data: globalmap_data = {}
        self._globalmap: dict = globalmap_data
        self.avg_damage_assisted: float = globalmap_data.get('avg_damage_assisted', 0.0)
        self.avg_damage_assisted_radio: float = globalmap_data.get('avg_damage_assisted_radio', 0.0)
        self.avg_damage_assisted_track: float = globalmap_data.get('avg_damage_assisted_track', 0.0)
        self.avg_damage_blocked: float = globalmap_data.get('avg_damage_blocked', 0.0)
        self.battle_avg_xp: int = globalmap_data.get('battle_avg_xp', 0)
        self.battles: int = globalmap_data.get('battles', 0)
        self.battles_on_stunning_vehicles: int = globalmap_data.get('battles_on_stunning_vehicles', 0)
        self.capture_points: int = globalmap_data.get('capture_points', 0)
        self.damage_dealt: int = globalmap_data.get('damage_dealt', 0)
        self.damage_received: int = globalmap_data.get('damage_received', 0)
        self.direct_hits_received: int = globalmap_data.get('direct_hits_received', 0)
        self.draws: int = globalmap_data.get('draws', 0)
        self.dropped_capture_points: int = globalmap_data.get('dropped_capture_points', 0)
        self.explosion_hits: int = globalmap_data.get('explosion_hits', 0)
        self.explosion_hits_received: int = globalmap_data.get('explosion_hits_received', 0)
        self.frags: int = globalmap_data.get('frags', 0)
        self.hits: int = globalmap_data.get('hits', 0)
        self.hits_percents: int = globalmap_data.get('hits_percents', 0)
        self.losses: int = globalmap_data.get('losses', 0)
        self.no_damage_direct_hits_received: int = globalmap_data.get('no_damage_direct_hits_received', 0)
        self.piercings: int = globalmap_data.get('piercings', 0)
        self.piercings_received: int = globalmap_data.get('piercings_received', 0)
        self.shots: int = globalmap_data.get('shots', 0)
        self.spotted: int = globalmap_data.get('spotted', 0)
        self.stun_assisted_damage: int = globalmap_data.get('stun_assisted_damage', 0)
        self.stun_number: int = globalmap_data.get('stun_number', 0)
        self.survived_battles: int = globalmap_data.get('survived_battles', 0)
        self.tanking_factor: float = globalmap_data.get('tanking_factor', 0.0)
        self.wins: int = globalmap_data.get('wins', 0)
        self.xp: int = globalmap_data.get('xp', 0)

class RandomClass:
    def __init__(self, random_data: dict):
        if not random_data: random_data = {}
        self._random: dict = random_data
        self.battle_avg_xp: int = random_data.get('battle_avg_xp', 0)
        self.battles: int = random_data.get('battles', 0)
        self.battles_on_stunning_vehicles: int = random_data.get('battles_on_stunning_vehicles', 0)
        self.capture_points: int = random_data.get('capture_points', 0)
        self.damage_dealt: int = random_data.get('damage_dealt', 0)
        self.damage_received: int = random_data.get('damage_received', 0)
        self.draws: int = random_data.get('draws', 0)
        self.dropped_capture_points: int = random_data.get('dropped_capture_points', 0)
        self.frags: int = random_data.get('frags', 0)
        self.hits: int = random_data.get('hits', 0)
        self.hits_percents: int = random_data.get('hits_percents', 0)
        self.losses: int = random_data.get('losses', 0)
        self.max_damage: int = random_data.get('max_damage', 0)
        self.max_frags: int = random_data.get('max_frags', 0)
        self.max_xp: int = random_data.get('max_xp', 0)
        self.shots: int = random_data.get('shots', 0)
        self.spotted: int = random_data.get('spotted', 0)
        self.stun_assisted_damage: int = random_data.get('stun_assisted_damage', 0)
        self.stun_number: int = random_data.get('stun_number', 0)
        self.survived_battles: int = random_data.get('survived_battles', 0)
        self.wins: int = random_data.get('wins', 0)
        self.xp: int = random_data.get('xp', 0)

class Ranked10X10Class:
    def __init__(self, ranked_10x10_data: dict):
        if not ranked_10x10_data: ranked_10x10_data = {}
        self._ranked_10x10: dict = ranked_10x10_data
        self.battle_avg_xp: int = ranked_10x10_data.get('battle_avg_xp', 0)
        self.battles: int = ranked_10x10_data.get('battles', 0)
        self.battles_on_stunning_vehicles: int = ranked_10x10_data.get('battles_on_stunning_vehicles', 0)
        self.capture_points: int = ranked_10x10_data.get('capture_points', 0)
        self.damage_dealt: int = ranked_10x10_data.get('damage_dealt', 0)
        self.damage_received: int = ranked_10x10_data.get('damage_received', 0)
        self.draws: int = ranked_10x10_data.get('draws', 0)
        self.dropped_capture_points: int = ranked_10x10_data.get('dropped_capture_points', 0)
        self.frags: int = ranked_10x10_data.get('frags', 0)
        self.hits: int = ranked_10x10_data.get('hits', 0)
        self.hits_percents: int = ranked_10x10_data.get('hits_percents', 0)
        self.losses: int = ranked_10x10_data.get('losses', 0)
        self.max_damage: int = ranked_10x10_data.get('max_damage', 0)
        self.max_frags: int = ranked_10x10_data.get('max_frags', 0)
        self.max_xp: int = ranked_10x10_data.get('max_xp', 0)
        self.shots: int = ranked_10x10_data.get('shots', 0)
        self.spotted: int = ranked_10x10_data.get('spotted', 0)
        self.stun_assisted_damage: int = ranked_10x10_data.get('stun_assisted_damage', 0)
        self.stun_number: int = ranked_10x10_data.get('stun_number', 0)
        self.survived_battles: int = ranked_10x10_data.get('survived_battles', 0)
        self.wins: int = ranked_10x10_data.get('wins', 0)
        self.xp: int = ranked_10x10_data.get('xp', 0)

class RankedBattlesClass:
    def __init__(self, ranked_battles_data: dict):
        if not ranked_battles_data: ranked_battles_data = {}
        self._ranked_battles: dict = ranked_battles_data
        self.battle_avg_xp: int = ranked_battles_data.get('battle_avg_xp', 0)
        self.battles: int = ranked_battles_data.get('battles', 0)
        self.battles_on_stunning_vehicles: int = ranked_battles_data.get('battles_on_stunning_vehicles', 0)
        self.capture_points: int = ranked_battles_data.get('capture_points', 0)
        self.damage_dealt: int = ranked_battles_data.get('damage_dealt', 0)
        self.damage_received: int = ranked_battles_data.get('damage_received', 0)
        self.draws: int = ranked_battles_data.get('draws', 0)
        self.dropped_capture_points: int = ranked_battles_data.get('dropped_capture_points', 0)
        self.frags: int = ranked_battles_data.get('frags', 0)
        self.hits: int = ranked_battles_data.get('hits', 0)
        self.hits_percents: int = ranked_battles_data.get('hits_percents', 0)
        self.losses: int = ranked_battles_data.get('losses', 0)
        self.max_damage: int = ranked_battles_data.get('max_damage', 0)
        self.max_frags: int = ranked_battles_data.get('max_frags', 0)
        self.max_xp: int = ranked_battles_data.get('max_xp', 0)
        self.shots: int = ranked_battles_data.get('shots', 0)
        self.spotted: int = ranked_battles_data.get('spotted', 0)
        self.stun_assisted_damage: int = ranked_battles_data.get('stun_assisted_damage', 0)
        self.stun_number: int = ranked_battles_data.get('stun_number', 0)
        self.survived_battles: int = ranked_battles_data.get('survived_battles', 0)
        self.wins: int = ranked_battles_data.get('wins', 0)
        self.xp: int = ranked_battles_data.get('xp', 0)

class RegularTeamClass:
    def __init__(self, regular_team_data: dict):
        if not regular_team_data: regular_team_data = {}
        self._regular_team: dict = regular_team_data
        self.battle_avg_xp: int = regular_team_data.get('battle_avg_xp', 0)
        self.battles: int = regular_team_data.get('battles', 0)
        self.battles_on_stunning_vehicles: int = regular_team_data.get('battles_on_stunning_vehicles', 0)
        self.capture_points: int = regular_team_data.get('capture_points', 0)
        self.damage_dealt: int = regular_team_data.get('damage_dealt', 0)
        self.damage_received: int = regular_team_data.get('damage_received', 0)
        self.draws: int = regular_team_data.get('draws', 0)
        self.dropped_capture_points: int = regular_team_data.get('dropped_capture_points', 0)
        self.frags: int = regular_team_data.get('frags', 0)
        self.hits: int = regular_team_data.get('hits', 0)
        self.hits_percents: int = regular_team_data.get('hits_percents', 0)
        self.losses: int = regular_team_data.get('losses', 0)
        self.max_damage: int = regular_team_data.get('max_damage', 0)
        self.max_frags: int = regular_team_data.get('max_frags', 0)
        self.max_xp: int = regular_team_data.get('max_xp', 0)
        self.shots: int = regular_team_data.get('shots', 0)
        self.spotted: int = regular_team_data.get('spotted', 0)
        self.stun_assisted_damage: int = regular_team_data.get('stun_assisted_damage', 0)
        self.stun_number: int = regular_team_data.get('stun_number', 0)
        self.survived_battles: int = regular_team_data.get('survived_battles', 0)
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
        self.max_frags: int = stronghold_defense_data.get('max_frags', 0)
        self.max_xp: int = stronghold_defense_data.get('max_xp', 0)
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
        self.max_frags: int = stronghold_skirmish_data.get('max_frags', 0)
        self.max_xp: int = stronghold_skirmish_data.get('max_xp', 0)
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
        self.battle_avg_xp: int = team_data.get('battle_avg_xp', 0)
        self.battles: int = team_data.get('battles', 0)
        self.battles_on_stunning_vehicles: int = team_data.get('battles_on_stunning_vehicles', 0)
        self.capture_points: int = team_data.get('capture_points', 0)
        self.damage_dealt: int = team_data.get('damage_dealt', 0)
        self.damage_received: int = team_data.get('damage_received', 0)
        self.draws: int = team_data.get('draws', 0)
        self.dropped_capture_points: int = team_data.get('dropped_capture_points', 0)
        self.frags: int = team_data.get('frags', 0)
        self.hits: int = team_data.get('hits', 0)
        self.hits_percents: int = team_data.get('hits_percents', 0)
        self.losses: int = team_data.get('losses', 0)
        self.max_damage: int = team_data.get('max_damage', 0)
        self.max_frags: int = team_data.get('max_frags', 0)
        self.max_xp: int = team_data.get('max_xp', 0)
        self.shots: int = team_data.get('shots', 0)
        self.spotted: int = team_data.get('spotted', 0)
        self.stun_assisted_damage: int = team_data.get('stun_assisted_damage', 0)
        self.stun_number: int = team_data.get('stun_number', 0)
        self.survived_battles: int = team_data.get('survived_battles', 0)
        self.wins: int = team_data.get('wins', 0)
        self.xp: int = team_data.get('xp', 0)

class TanksStatsClass:
    def __init__(self, tanks_stats_data: dict):
        if not tanks_stats_data: tanks_stats_data = {}
        self._tanks_stats: dict = tanks_stats_data
        self.account_id: int = tanks_stats_data.get('account_id', 0)
        self.mark_of_mastery: int = tanks_stats_data.get('mark_of_mastery', 0)
        self.max_frags: int = tanks_stats_data.get('max_frags', 0)
        self.max_xp: int = tanks_stats_data.get('max_xp', 0)
        self.tank_id: int = tanks_stats_data.get('tank_id', 0)
        self.frags: dict = tanks_stats_data.get('frags', {})
        self.in_garage: bool = tanks_stats_data.get('in_garage', False)

        all_temp: dict = self._tanks_stats.get('all')
        all_class = None
        if isinstance(all_temp, dict):
            for key in all_temp:
                if str(key).isnumeric():
                    all_class = {key: AllClass(data) for key, data in all_temp.items()}
                    break
                if key == 'avg_damage_blocked' or key == 'battle_avg_xp' or key == 'battles' or key == 'battles_on_stunning_vehicles' or key == 'capture_points' or key == 'damage_dealt' or key == 'damage_received' or key == 'direct_hits_received' or key == 'draws' or key == 'dropped_capture_points' or key == 'explosion_hits' or key == 'explosion_hits_received' or key == 'frags' or key == 'hits' or key == 'hits_percents' or key == 'losses' or key == 'no_damage_direct_hits_received' or key == 'piercings' or key == 'piercings_received' or key == 'shots' or key == 'spotted' or key == 'stun_assisted_damage' or key == 'stun_number' or key == 'survived_battles' or key == 'tanking_factor' or key == 'wins' or key == 'xp':
                    all_class = AllClass(all_temp)
                    break
        elif isinstance(all_temp, list):
            all_class = [AllClass(data) for data in all_temp]
        if not all_class:
            all_class: AllClass = AllClass(all_temp)
        self.all: AllClass | list[AllClass] | dict[str, AllClass] = all_class
        del all_temp, all_class


        clan_temp: dict = self._tanks_stats.get('clan')
        clan_class = None
        if isinstance(clan_temp, dict):
            for key in clan_temp:
                if str(key).isnumeric():
                    clan_class = {key: ClanClass(data) for key, data in clan_temp.items()}
                    break
                if key == 'battle_avg_xp' or key == 'battles' or key == 'battles_on_stunning_vehicles' or key == 'capture_points' or key == 'damage_dealt' or key == 'damage_received' or key == 'draws' or key == 'dropped_capture_points' or key == 'frags' or key == 'hits' or key == 'hits_percents' or key == 'losses' or key == 'max_damage' or key == 'max_frags' or key == 'max_xp' or key == 'shots' or key == 'spotted' or key == 'stun_assisted_damage' or key == 'stun_number' or key == 'survived_battles' or key == 'wins' or key == 'xp':
                    clan_class = ClanClass(clan_temp)
                    break
        elif isinstance(clan_temp, list):
            clan_class = [ClanClass(data) for data in clan_temp]
        if not clan_class:
            clan_class: ClanClass = ClanClass(clan_temp)
        self.clan: ClanClass | list[ClanClass] | dict[str, ClanClass] = clan_class
        del clan_temp, clan_class


        company_temp: dict = self._tanks_stats.get('company')
        company_class = None
        if isinstance(company_temp, dict):
            for key in company_temp:
                if str(key).isnumeric():
                    company_class = {key: CompanyClass(data) for key, data in company_temp.items()}
                    break
                if key == 'battle_avg_xp' or key == 'battles' or key == 'battles_on_stunning_vehicles' or key == 'capture_points' or key == 'damage_dealt' or key == 'damage_received' or key == 'draws' or key == 'dropped_capture_points' or key == 'frags' or key == 'hits' or key == 'hits_percents' or key == 'losses' or key == 'shots' or key == 'spotted' or key == 'stun_assisted_damage' or key == 'stun_number' or key == 'survived_battles' or key == 'wins' or key == 'xp':
                    company_class = CompanyClass(company_temp)
                    break
        elif isinstance(company_temp, list):
            company_class = [CompanyClass(data) for data in company_temp]
        if not company_class:
            company_class: CompanyClass = CompanyClass(company_temp)
        self.company: CompanyClass | list[CompanyClass] | dict[str, CompanyClass] = company_class
        del company_temp, company_class


        epic_temp: dict = self._tanks_stats.get('epic')
        epic_class = None
        if isinstance(epic_temp, dict):
            for key in epic_temp:
                if str(key).isnumeric():
                    epic_class = {key: EpicClass(data) for key, data in epic_temp.items()}
                    break
                if key == 'battle_avg_xp' or key == 'battles' or key == 'battles_on_stunning_vehicles' or key == 'capture_points' or key == 'damage_dealt' or key == 'damage_received' or key == 'draws' or key == 'dropped_capture_points' or key == 'frags' or key == 'hits' or key == 'hits_percents' or key == 'losses' or key == 'max_damage' or key == 'max_frags' or key == 'max_xp' or key == 'shots' or key == 'spotted' or key == 'stun_assisted_damage' or key == 'stun_number' or key == 'survived_battles' or key == 'wins' or key == 'xp':
                    epic_class = EpicClass(epic_temp)
                    break
        elif isinstance(epic_temp, list):
            epic_class = [EpicClass(data) for data in epic_temp]
        if not epic_class:
            epic_class: EpicClass = EpicClass(epic_temp)
        self.epic: EpicClass | list[EpicClass] | dict[str, EpicClass] = epic_class
        del epic_temp, epic_class


        fallout_temp: dict = self._tanks_stats.get('fallout')
        fallout_class = None
        if isinstance(fallout_temp, dict):
            for key in fallout_temp:
                if str(key).isnumeric():
                    fallout_class = {key: FalloutClass(data) for key, data in fallout_temp.items()}
                    break
                if key == 'avatar_damage_dealt' or key == 'avatar_frags' or key == 'avg_damage_assisted' or key == 'avg_damage_assisted_radio' or key == 'avg_damage_assisted_track' or key == 'avg_damage_blocked' or key == 'battle_avg_xp' or key == 'battles' or key == 'battles_on_stunning_vehicles' or key == 'capture_points' or key == 'damage_dealt' or key == 'damage_received' or key == 'death_count' or key == 'direct_hits_received' or key == 'draws' or key == 'dropped_capture_points' or key == 'explosion_hits' or key == 'explosion_hits_received' or key == 'flag_capture' or key == 'flag_capture_solo' or key == 'frags' or key == 'hits' or key == 'hits_percents' or key == 'losses' or key == 'max_damage' or key == 'max_damage_with_avatar' or key == 'max_frags' or key == 'max_frags_with_avatar' or key == 'max_win_points' or key == 'max_xp' or key == 'no_damage_direct_hits_received' or key == 'piercings' or key == 'piercings_received' or key == 'resource_absorbed' or key == 'shots' or key == 'spotted' or key == 'stun_assisted_damage' or key == 'stun_number' or key == 'survived_battles' or key == 'tanking_factor' or key == 'win_points' or key == 'wins' or key == 'xp':
                    fallout_class = FalloutClass(fallout_temp)
                    break
        elif isinstance(fallout_temp, list):
            fallout_class = [FalloutClass(data) for data in fallout_temp]
        if not fallout_class:
            fallout_class: FalloutClass = FalloutClass(fallout_temp)
        self.fallout: FalloutClass | list[FalloutClass] | dict[str, FalloutClass] = fallout_class
        del fallout_temp, fallout_class


        globalmap_temp: dict = self._tanks_stats.get('globalmap')
        globalmap_class = None
        if isinstance(globalmap_temp, dict):
            for key in globalmap_temp:
                if str(key).isnumeric():
                    globalmap_class = {key: GlobalmapClass(data) for key, data in globalmap_temp.items()}
                    break
                if key == 'avg_damage_assisted' or key == 'avg_damage_assisted_radio' or key == 'avg_damage_assisted_track' or key == 'avg_damage_blocked' or key == 'battle_avg_xp' or key == 'battles' or key == 'battles_on_stunning_vehicles' or key == 'capture_points' or key == 'damage_dealt' or key == 'damage_received' or key == 'direct_hits_received' or key == 'draws' or key == 'dropped_capture_points' or key == 'explosion_hits' or key == 'explosion_hits_received' or key == 'frags' or key == 'hits' or key == 'hits_percents' or key == 'losses' or key == 'no_damage_direct_hits_received' or key == 'piercings' or key == 'piercings_received' or key == 'shots' or key == 'spotted' or key == 'stun_assisted_damage' or key == 'stun_number' or key == 'survived_battles' or key == 'tanking_factor' or key == 'wins' or key == 'xp':
                    globalmap_class = GlobalmapClass(globalmap_temp)
                    break
        elif isinstance(globalmap_temp, list):
            globalmap_class = [GlobalmapClass(data) for data in globalmap_temp]
        if not globalmap_class:
            globalmap_class: GlobalmapClass = GlobalmapClass(globalmap_temp)
        self.globalmap: GlobalmapClass | list[GlobalmapClass] | dict[str, GlobalmapClass] = globalmap_class
        del globalmap_temp, globalmap_class


        random_temp: dict = self._tanks_stats.get('random')
        random_class = None
        if isinstance(random_temp, dict):
            for key in random_temp:
                if str(key).isnumeric():
                    random_class = {key: RandomClass(data) for key, data in random_temp.items()}
                    break
                if key == 'battle_avg_xp' or key == 'battles' or key == 'battles_on_stunning_vehicles' or key == 'capture_points' or key == 'damage_dealt' or key == 'damage_received' or key == 'draws' or key == 'dropped_capture_points' or key == 'frags' or key == 'hits' or key == 'hits_percents' or key == 'losses' or key == 'max_damage' or key == 'max_frags' or key == 'max_xp' or key == 'shots' or key == 'spotted' or key == 'stun_assisted_damage' or key == 'stun_number' or key == 'survived_battles' or key == 'wins' or key == 'xp':
                    random_class = RandomClass(random_temp)
                    break
        elif isinstance(random_temp, list):
            random_class = [RandomClass(data) for data in random_temp]
        if not random_class:
            random_class: RandomClass = RandomClass(random_temp)
        self.random: RandomClass | list[RandomClass] | dict[str, RandomClass] = random_class
        del random_temp, random_class


        ranked_10x10_temp: dict = self._tanks_stats.get('ranked_10x10')
        ranked_10x10_class = None
        if isinstance(ranked_10x10_temp, dict):
            for key in ranked_10x10_temp:
                if str(key).isnumeric():
                    ranked_10x10_class = {key: Ranked10X10Class(data) for key, data in ranked_10x10_temp.items()}
                    break
                if key == 'battle_avg_xp' or key == 'battles' or key == 'battles_on_stunning_vehicles' or key == 'capture_points' or key == 'damage_dealt' or key == 'damage_received' or key == 'draws' or key == 'dropped_capture_points' or key == 'frags' or key == 'hits' or key == 'hits_percents' or key == 'losses' or key == 'max_damage' or key == 'max_frags' or key == 'max_xp' or key == 'shots' or key == 'spotted' or key == 'stun_assisted_damage' or key == 'stun_number' or key == 'survived_battles' or key == 'wins' or key == 'xp':
                    ranked_10x10_class = Ranked10X10Class(ranked_10x10_temp)
                    break
        elif isinstance(ranked_10x10_temp, list):
            ranked_10x10_class = [Ranked10X10Class(data) for data in ranked_10x10_temp]
        if not ranked_10x10_class:
            ranked_10x10_class: Ranked10X10Class = Ranked10X10Class(ranked_10x10_temp)
        self.ranked_10x10: Ranked10X10Class | list[Ranked10X10Class] | dict[str, Ranked10X10Class] = ranked_10x10_class
        del ranked_10x10_temp, ranked_10x10_class


        ranked_battles_temp: dict = self._tanks_stats.get('ranked_battles')
        ranked_battles_class = None
        if isinstance(ranked_battles_temp, dict):
            for key in ranked_battles_temp:
                if str(key).isnumeric():
                    ranked_battles_class = {key: RankedBattlesClass(data) for key, data in ranked_battles_temp.items()}
                    break
                if key == 'battle_avg_xp' or key == 'battles' or key == 'battles_on_stunning_vehicles' or key == 'capture_points' or key == 'damage_dealt' or key == 'damage_received' or key == 'draws' or key == 'dropped_capture_points' or key == 'frags' or key == 'hits' or key == 'hits_percents' or key == 'losses' or key == 'max_damage' or key == 'max_frags' or key == 'max_xp' or key == 'shots' or key == 'spotted' or key == 'stun_assisted_damage' or key == 'stun_number' or key == 'survived_battles' or key == 'wins' or key == 'xp':
                    ranked_battles_class = RankedBattlesClass(ranked_battles_temp)
                    break
        elif isinstance(ranked_battles_temp, list):
            ranked_battles_class = [RankedBattlesClass(data) for data in ranked_battles_temp]
        if not ranked_battles_class:
            ranked_battles_class: RankedBattlesClass = RankedBattlesClass(ranked_battles_temp)
        self.ranked_battles: RankedBattlesClass | list[RankedBattlesClass] | dict[str, RankedBattlesClass] = ranked_battles_class
        del ranked_battles_temp, ranked_battles_class


        regular_team_temp: dict = self._tanks_stats.get('regular_team')
        regular_team_class = None
        if isinstance(regular_team_temp, dict):
            for key in regular_team_temp:
                if str(key).isnumeric():
                    regular_team_class = {key: RegularTeamClass(data) for key, data in regular_team_temp.items()}
                    break
                if key == 'battle_avg_xp' or key == 'battles' or key == 'battles_on_stunning_vehicles' or key == 'capture_points' or key == 'damage_dealt' or key == 'damage_received' or key == 'draws' or key == 'dropped_capture_points' or key == 'frags' or key == 'hits' or key == 'hits_percents' or key == 'losses' or key == 'max_damage' or key == 'max_frags' or key == 'max_xp' or key == 'shots' or key == 'spotted' or key == 'stun_assisted_damage' or key == 'stun_number' or key == 'survived_battles' or key == 'wins' or key == 'xp':
                    regular_team_class = RegularTeamClass(regular_team_temp)
                    break
        elif isinstance(regular_team_temp, list):
            regular_team_class = [RegularTeamClass(data) for data in regular_team_temp]
        if not regular_team_class:
            regular_team_class: RegularTeamClass = RegularTeamClass(regular_team_temp)
        self.regular_team: RegularTeamClass | list[RegularTeamClass] | dict[str, RegularTeamClass] = regular_team_class
        del regular_team_temp, regular_team_class


        stronghold_defense_temp: dict = self._tanks_stats.get('stronghold_defense')
        stronghold_defense_class = None
        if isinstance(stronghold_defense_temp, dict):
            for key in stronghold_defense_temp:
                if str(key).isnumeric():
                    stronghold_defense_class = {key: StrongholdDefenseClass(data) for key, data in stronghold_defense_temp.items()}
                    break
                if key == 'battle_avg_xp' or key == 'battles' or key == 'battles_on_stunning_vehicles' or key == 'capture_points' or key == 'damage_dealt' or key == 'damage_received' or key == 'direct_hits_received' or key == 'draws' or key == 'dropped_capture_points' or key == 'explosion_hits' or key == 'explosion_hits_received' or key == 'frags' or key == 'hits' or key == 'hits_percents' or key == 'losses' or key == 'max_damage' or key == 'max_frags' or key == 'max_xp' or key == 'no_damage_direct_hits_received' or key == 'piercings' or key == 'piercings_received' or key == 'shots' or key == 'spotted' or key == 'stun_assisted_damage' or key == 'stun_number' or key == 'survived_battles' or key == 'tanking_factor' or key == 'wins' or key == 'xp':
                    stronghold_defense_class = StrongholdDefenseClass(stronghold_defense_temp)
                    break
        elif isinstance(stronghold_defense_temp, list):
            stronghold_defense_class = [StrongholdDefenseClass(data) for data in stronghold_defense_temp]
        if not stronghold_defense_class:
            stronghold_defense_class: StrongholdDefenseClass = StrongholdDefenseClass(stronghold_defense_temp)
        self.stronghold_defense: StrongholdDefenseClass | list[StrongholdDefenseClass] | dict[str, StrongholdDefenseClass] = stronghold_defense_class
        del stronghold_defense_temp, stronghold_defense_class


        stronghold_skirmish_temp: dict = self._tanks_stats.get('stronghold_skirmish')
        stronghold_skirmish_class = None
        if isinstance(stronghold_skirmish_temp, dict):
            for key in stronghold_skirmish_temp:
                if str(key).isnumeric():
                    stronghold_skirmish_class = {key: StrongholdSkirmishClass(data) for key, data in stronghold_skirmish_temp.items()}
                    break
                if key == 'battle_avg_xp' or key == 'battles' or key == 'battles_on_stunning_vehicles' or key == 'capture_points' or key == 'damage_dealt' or key == 'damage_received' or key == 'direct_hits_received' or key == 'draws' or key == 'dropped_capture_points' or key == 'explosion_hits' or key == 'explosion_hits_received' or key == 'frags' or key == 'hits' or key == 'hits_percents' or key == 'losses' or key == 'max_damage' or key == 'max_frags' or key == 'max_xp' or key == 'no_damage_direct_hits_received' or key == 'piercings' or key == 'piercings_received' or key == 'shots' or key == 'spotted' or key == 'stun_assisted_damage' or key == 'stun_number' or key == 'survived_battles' or key == 'tanking_factor' or key == 'wins' or key == 'xp':
                    stronghold_skirmish_class = StrongholdSkirmishClass(stronghold_skirmish_temp)
                    break
        elif isinstance(stronghold_skirmish_temp, list):
            stronghold_skirmish_class = [StrongholdSkirmishClass(data) for data in stronghold_skirmish_temp]
        if not stronghold_skirmish_class:
            stronghold_skirmish_class: StrongholdSkirmishClass = StrongholdSkirmishClass(stronghold_skirmish_temp)
        self.stronghold_skirmish: StrongholdSkirmishClass | list[StrongholdSkirmishClass] | dict[str, StrongholdSkirmishClass] = stronghold_skirmish_class
        del stronghold_skirmish_temp, stronghold_skirmish_class


        team_temp: dict = self._tanks_stats.get('team')
        team_class = None
        if isinstance(team_temp, dict):
            for key in team_temp:
                if str(key).isnumeric():
                    team_class = {key: TeamClass(data) for key, data in team_temp.items()}
                    break
                if key == 'battle_avg_xp' or key == 'battles' or key == 'battles_on_stunning_vehicles' or key == 'capture_points' or key == 'damage_dealt' or key == 'damage_received' or key == 'draws' or key == 'dropped_capture_points' or key == 'frags' or key == 'hits' or key == 'hits_percents' or key == 'losses' or key == 'max_damage' or key == 'max_frags' or key == 'max_xp' or key == 'shots' or key == 'spotted' or key == 'stun_assisted_damage' or key == 'stun_number' or key == 'survived_battles' or key == 'wins' or key == 'xp':
                    team_class = TeamClass(team_temp)
                    break
        elif isinstance(team_temp, list):
            team_class = [TeamClass(data) for data in team_temp]
        if not team_class:
            team_class: TeamClass = TeamClass(team_temp)
        self.team: TeamClass | list[TeamClass] | dict[str, TeamClass] = team_class
        del team_temp, team_class


