class BattlesForStrongholdsStatisticsClass:
    def __init__(self, battles_for_strongholds_statistics_data: dict):
        if not battles_for_strongholds_statistics_data: battles_for_strongholds_statistics_data = {}
        self._battles_for_strongholds_statistics: dict = battles_for_strongholds_statistics_data
        self.last_time_10: int = battles_for_strongholds_statistics_data.get('last_time_10', 0)
        self.lose_10: int = battles_for_strongholds_statistics_data.get('lose_10', 0)
        self.total_10: int = battles_for_strongholds_statistics_data.get('total_10', 0)
        self.total_10_in_28d: int = battles_for_strongholds_statistics_data.get('total_10_in_28d', 0)
        self.win_10: int = battles_for_strongholds_statistics_data.get('win_10', 0)
        self.win_10_in_28d: int = battles_for_strongholds_statistics_data.get('win_10_in_28d', 0)

class BattlesSeriesForStrongholdsStatisticsClass:
    def __init__(self, battles_series_for_strongholds_statistics_data: dict):
        if not battles_series_for_strongholds_statistics_data: battles_series_for_strongholds_statistics_data = {}
        self._battles_series_for_strongholds_statistics: dict = battles_series_for_strongholds_statistics_data
        self.lose_10: int = battles_series_for_strongholds_statistics_data.get('lose_10', 0)
        self.total_10: int = battles_series_for_strongholds_statistics_data.get('total_10', 0)
        self.total_10_in_28d: int = battles_series_for_strongholds_statistics_data.get('total_10_in_28d', 0)
        self.win_10: int = battles_series_for_strongholds_statistics_data.get('win_10', 0)
        self.win_10_in_28d: int = battles_series_for_strongholds_statistics_data.get('win_10_in_28d', 0)

class BuildingSlotsClass:
    def __init__(self, building_slots_data: dict):
        if not building_slots_data: building_slots_data = {}
        self._building_slots: dict = building_slots_data
        self.arena_id: str = building_slots_data.get('arena_id', '')
        self.building_level: int = building_slots_data.get('building_level', 0)
        self.building_title: str = building_slots_data.get('building_title', '')
        self.direction: str = building_slots_data.get('direction', '')
        self.position: str = building_slots_data.get('position', '')
        self.reserve_title: str = building_slots_data.get('reserve_title', '')

class SkirmishStatisticsClass:
    def __init__(self, skirmish_statistics_data: dict):
        if not skirmish_statistics_data: skirmish_statistics_data = {}
        self._skirmish_statistics: dict = skirmish_statistics_data
        self.last_time_10: int = skirmish_statistics_data.get('last_time_10', 0)
        self.last_time_6: int = skirmish_statistics_data.get('last_time_6', 0)
        self.last_time_8: int = skirmish_statistics_data.get('last_time_8', 0)
        self.lose_10: int = skirmish_statistics_data.get('lose_10', 0)
        self.lose_6: int = skirmish_statistics_data.get('lose_6', 0)
        self.lose_8: int = skirmish_statistics_data.get('lose_8', 0)
        self.total_10: int = skirmish_statistics_data.get('total_10', 0)
        self.total_10_in_28d: int = skirmish_statistics_data.get('total_10_in_28d', 0)
        self.total_6: int = skirmish_statistics_data.get('total_6', 0)
        self.total_6_in_28d: int = skirmish_statistics_data.get('total_6_in_28d', 0)
        self.total_8: int = skirmish_statistics_data.get('total_8', 0)
        self.total_8_in_28d: int = skirmish_statistics_data.get('total_8_in_28d', 0)
        self.win_10: int = skirmish_statistics_data.get('win_10', 0)
        self.win_10_in_28d: int = skirmish_statistics_data.get('win_10_in_28d', 0)
        self.win_6: int = skirmish_statistics_data.get('win_6', 0)
        self.win_6_in_28d: int = skirmish_statistics_data.get('win_6_in_28d', 0)
        self.win_8: int = skirmish_statistics_data.get('win_8', 0)
        self.win_8_in_28d: int = skirmish_statistics_data.get('win_8_in_28d', 0)

class StrongholdClaninfoClass:
    def __init__(self, stronghold_claninfo_data: dict):
        if not stronghold_claninfo_data: stronghold_claninfo_data = {}
        self._stronghold_claninfo: dict = stronghold_claninfo_data
        self.clan_id: int = stronghold_claninfo_data.get('clan_id', 0)
        self.clan_name: str = stronghold_claninfo_data.get('clan_name', '')
        self.clan_tag: str = stronghold_claninfo_data.get('clan_tag', '')
        self.command_center_arena_id: str = stronghold_claninfo_data.get('command_center_arena_id', '')
        self.stronghold_buildings_level: int = stronghold_claninfo_data.get('stronghold_buildings_level', 0)
        self.stronghold_level: int = stronghold_claninfo_data.get('stronghold_level', 0)

        battles_for_strongholds_statistics_temp: dict = self._stronghold_claninfo.get('battles_for_strongholds_statistics')
        battles_for_strongholds_statistics_class = None
        if isinstance(battles_for_strongholds_statistics_temp, dict):
            for key in battles_for_strongholds_statistics_temp:
                if str(key).isnumeric():
                    battles_for_strongholds_statistics_class = {key: BattlesForStrongholdsStatisticsClass(data) for key, data in battles_for_strongholds_statistics_temp.items()}
                    break
                if key == 'last_time_10' or key == 'lose_10' or key == 'total_10' or key == 'total_10_in_28d' or key == 'win_10' or key == 'win_10_in_28d':
                    battles_for_strongholds_statistics_class = BattlesForStrongholdsStatisticsClass(battles_for_strongholds_statistics_temp)
                    break
        elif isinstance(battles_for_strongholds_statistics_temp, list):
            battles_for_strongholds_statistics_class = [BattlesForStrongholdsStatisticsClass(data) for data in battles_for_strongholds_statistics_temp]
        if not battles_for_strongholds_statistics_class:
            battles_for_strongholds_statistics_class: BattlesForStrongholdsStatisticsClass = BattlesForStrongholdsStatisticsClass(battles_for_strongholds_statistics_temp)
        self.battles_for_strongholds_statistics: BattlesForStrongholdsStatisticsClass | list[BattlesForStrongholdsStatisticsClass] | dict[str, BattlesForStrongholdsStatisticsClass] = battles_for_strongholds_statistics_class
        del battles_for_strongholds_statistics_temp, battles_for_strongholds_statistics_class


        battles_series_for_strongholds_statistics_temp: dict = self._stronghold_claninfo.get('battles_series_for_strongholds_statistics')
        battles_series_for_strongholds_statistics_class = None
        if isinstance(battles_series_for_strongholds_statistics_temp, dict):
            for key in battles_series_for_strongholds_statistics_temp:
                if str(key).isnumeric():
                    battles_series_for_strongholds_statistics_class = {key: BattlesSeriesForStrongholdsStatisticsClass(data) for key, data in battles_series_for_strongholds_statistics_temp.items()}
                    break
                if key == 'lose_10' or key == 'total_10' or key == 'total_10_in_28d' or key == 'win_10' or key == 'win_10_in_28d':
                    battles_series_for_strongholds_statistics_class = BattlesSeriesForStrongholdsStatisticsClass(battles_series_for_strongholds_statistics_temp)
                    break
        elif isinstance(battles_series_for_strongholds_statistics_temp, list):
            battles_series_for_strongholds_statistics_class = [BattlesSeriesForStrongholdsStatisticsClass(data) for data in battles_series_for_strongholds_statistics_temp]
        if not battles_series_for_strongholds_statistics_class:
            battles_series_for_strongholds_statistics_class: BattlesSeriesForStrongholdsStatisticsClass = BattlesSeriesForStrongholdsStatisticsClass(battles_series_for_strongholds_statistics_temp)
        self.battles_series_for_strongholds_statistics: BattlesSeriesForStrongholdsStatisticsClass | list[BattlesSeriesForStrongholdsStatisticsClass] | dict[str, BattlesSeriesForStrongholdsStatisticsClass] = battles_series_for_strongholds_statistics_class
        del battles_series_for_strongholds_statistics_temp, battles_series_for_strongholds_statistics_class


        building_slots_temp: dict = self._stronghold_claninfo.get('building_slots')
        building_slots_class = None
        if isinstance(building_slots_temp, dict):
            for key in building_slots_temp:
                if str(key).isnumeric():
                    building_slots_class = {key: BuildingSlotsClass(data) for key, data in building_slots_temp.items()}
                    break
                if key == 'arena_id' or key == 'building_level' or key == 'building_title' or key == 'direction' or key == 'position' or key == 'reserve_title':
                    building_slots_class = BuildingSlotsClass(building_slots_temp)
                    break
        elif isinstance(building_slots_temp, list):
            building_slots_class = [BuildingSlotsClass(data) for data in building_slots_temp]
        if not building_slots_class:
            building_slots_class: BuildingSlotsClass = BuildingSlotsClass(building_slots_temp)
        self.building_slots: BuildingSlotsClass | list[BuildingSlotsClass] | dict[str, BuildingSlotsClass] = building_slots_class
        del building_slots_temp, building_slots_class


        skirmish_statistics_temp: dict = self._stronghold_claninfo.get('skirmish_statistics')
        skirmish_statistics_class = None
        if isinstance(skirmish_statistics_temp, dict):
            for key in skirmish_statistics_temp:
                if str(key).isnumeric():
                    skirmish_statistics_class = {key: SkirmishStatisticsClass(data) for key, data in skirmish_statistics_temp.items()}
                    break
                if key == 'last_time_10' or key == 'last_time_6' or key == 'last_time_8' or key == 'lose_10' or key == 'lose_6' or key == 'lose_8' or key == 'total_10' or key == 'total_10_in_28d' or key == 'total_6' or key == 'total_6_in_28d' or key == 'total_8' or key == 'total_8_in_28d' or key == 'win_10' or key == 'win_10_in_28d' or key == 'win_6' or key == 'win_6_in_28d' or key == 'win_8' or key == 'win_8_in_28d':
                    skirmish_statistics_class = SkirmishStatisticsClass(skirmish_statistics_temp)
                    break
        elif isinstance(skirmish_statistics_temp, list):
            skirmish_statistics_class = [SkirmishStatisticsClass(data) for data in skirmish_statistics_temp]
        if not skirmish_statistics_class:
            skirmish_statistics_class: SkirmishStatisticsClass = SkirmishStatisticsClass(skirmish_statistics_temp)
        self.skirmish_statistics: SkirmishStatisticsClass | list[SkirmishStatisticsClass] | dict[str, SkirmishStatisticsClass] = skirmish_statistics_class
        del skirmish_statistics_temp, skirmish_statistics_class


