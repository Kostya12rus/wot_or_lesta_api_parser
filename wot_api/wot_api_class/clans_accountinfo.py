class EmblemsClass:
    def __init__(self, emblems_data: dict):
        if not emblems_data: emblems_data = {}
        self._emblems: dict = emblems_data
        self.x195: dict = emblems_data.get('x195', {})
        self.x24: dict = emblems_data.get('x24', {})
        self.x256: dict = emblems_data.get('x256', {})
        self.x32: dict = emblems_data.get('x32', {})
        self.x64: dict = emblems_data.get('x64', {})

class ClanClass:
    def __init__(self, clan_data: dict):
        if not clan_data: clan_data = {}
        self._clan: dict = clan_data
        self.clan_id: int = clan_data.get('clan_id', 0)
        self.color: str = clan_data.get('color', '')
        self.created_at: int = clan_data.get('created_at', 0)
        self.members_count: int = clan_data.get('members_count', 0)
        self.name: str = clan_data.get('name', '')
        self.tag: str = clan_data.get('tag', '')

        emblems_temp: dict = self._clan.get('emblems')
        emblems_class = None
        if isinstance(emblems_temp, dict):
            for key in emblems_temp:
                if str(key).isnumeric():
                    emblems_class = {key: EmblemsClass(data) for key, data in emblems_temp.items()}
                    break
                if key == 'x195' or key == 'x24' or key == 'x256' or key == 'x32' or key == 'x64':
                    emblems_class = EmblemsClass(emblems_temp)
                    break
        elif isinstance(emblems_temp, list):
            emblems_class = [EmblemsClass(data) for data in emblems_temp]
        if not emblems_class:
            emblems_class: EmblemsClass = EmblemsClass(emblems_temp)
        self.emblems: EmblemsClass | list[EmblemsClass] | dict[str, EmblemsClass] = emblems_class
        del emblems_temp, emblems_class


class ClansAccountinfoClass:
    def __init__(self, clans_accountinfo_data: dict):
        if not clans_accountinfo_data: clans_accountinfo_data = {}
        self._clans_accountinfo: dict = clans_accountinfo_data
        self.account_id: int = clans_accountinfo_data.get('account_id', 0)
        self.account_name: str = clans_accountinfo_data.get('account_name', '')
        self.joined_at: int = clans_accountinfo_data.get('joined_at', 0)
        self.role: str = clans_accountinfo_data.get('role', '')
        self.role_i18n: str = clans_accountinfo_data.get('role_i18n', '')

        clan_temp: dict = self._clans_accountinfo.get('clan')
        clan_class = None
        if isinstance(clan_temp, dict):
            for key in clan_temp:
                if str(key).isnumeric():
                    clan_class = {key: ClanClass(data) for key, data in clan_temp.items()}
                    break
                if key == 'clan_id' or key == 'color' or key == 'created_at' or key == 'members_count' or key == 'name' or key == 'tag' or key == 'emblems':
                    clan_class = ClanClass(clan_temp)
                    break
        elif isinstance(clan_temp, list):
            clan_class = [ClanClass(data) for data in clan_temp]
        if not clan_class:
            clan_class: ClanClass = ClanClass(clan_temp)
        self.clan: ClanClass | list[ClanClass] | dict[str, ClanClass] = clan_class
        del clan_temp, clan_class


