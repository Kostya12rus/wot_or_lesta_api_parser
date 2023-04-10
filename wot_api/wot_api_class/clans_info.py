class EmblemsClass:
    def __init__(self, emblems_data: dict):
        if not emblems_data: emblems_data = {}
        self._emblems: dict = emblems_data
        self.x195: dict = emblems_data.get('x195', {})
        self.x24: dict = emblems_data.get('x24', {})
        self.x256: dict = emblems_data.get('x256', {})
        self.x32: dict = emblems_data.get('x32', {})
        self.x64: dict = emblems_data.get('x64', {})

class MembersClass:
    def __init__(self, members_data: dict):
        if not members_data: members_data = {}
        self._members: dict = members_data
        self.account_id: int = members_data.get('account_id', 0)
        self.account_name: str = members_data.get('account_name', '')
        self.joined_at: int = members_data.get('joined_at', 0)
        self.role: str = members_data.get('role', '')
        self.role_i18n: str = members_data.get('role_i18n', '')

class ClanTreasuryClass:
    def __init__(self, clan_treasury_data: dict):
        if not clan_treasury_data: clan_treasury_data = {}
        self._clan_treasury: dict = clan_treasury_data
        self.credits: int = clan_treasury_data.get('credits', 0)
        self.crystal: int = clan_treasury_data.get('crystal', 0)
        self.gold: int = clan_treasury_data.get('gold', 0)

class PrivateClass:
    def __init__(self, private_data: dict):
        if not private_data: private_data = {}
        self._private: dict = private_data
        self.online_members: list = private_data.get('online_members', [])
        self.treasury: int = private_data.get('treasury', 0)

        clan_treasury_temp: dict = self._private.get('clan_treasury')
        clan_treasury_class = None
        if isinstance(clan_treasury_temp, dict):
            for key in clan_treasury_temp:
                if str(key).isnumeric():
                    clan_treasury_class = {key: ClanTreasuryClass(data) for key, data in clan_treasury_temp.items()}
                    break
                if key == 'credits' or key == 'crystal' or key == 'gold':
                    clan_treasury_class = ClanTreasuryClass(clan_treasury_temp)
                    break
        elif isinstance(clan_treasury_temp, list):
            clan_treasury_class = [ClanTreasuryClass(data) for data in clan_treasury_temp]
        if not clan_treasury_class:
            clan_treasury_class: ClanTreasuryClass = ClanTreasuryClass(clan_treasury_temp)
        self.clan_treasury: ClanTreasuryClass | list[ClanTreasuryClass] | dict[str, ClanTreasuryClass] = clan_treasury_class
        del clan_treasury_temp, clan_treasury_class


class ClansInfoClass:
    def __init__(self, clans_info_data: dict):
        if not clans_info_data: clans_info_data = {}
        self._clans_info: dict = clans_info_data
        self.accepts_join_requests: bool = clans_info_data.get('accepts_join_requests', False)
        self.clan_id: int = clans_info_data.get('clan_id', 0)
        self.color: str = clans_info_data.get('color', '')
        self.created_at: int = clans_info_data.get('created_at', 0)
        self.creator_id: int = clans_info_data.get('creator_id', 0)
        self.creator_name: str = clans_info_data.get('creator_name', '')
        self.description: str = clans_info_data.get('description', '')
        self.description_html: str = clans_info_data.get('description_html', '')
        self.is_clan_disbanded: bool = clans_info_data.get('is_clan_disbanded', False)
        self.leader_id: int = clans_info_data.get('leader_id', 0)
        self.leader_name: str = clans_info_data.get('leader_name', '')
        self.members_count: int = clans_info_data.get('members_count', 0)
        self.motto: str = clans_info_data.get('motto', '')
        self.name: str = clans_info_data.get('name', '')
        self.old_name: str = clans_info_data.get('old_name', '')
        self.old_tag: str = clans_info_data.get('old_tag', '')
        self.renamed_at: int = clans_info_data.get('renamed_at', 0)
        self.tag: str = clans_info_data.get('tag', '')
        self.updated_at: int = clans_info_data.get('updated_at', 0)

        emblems_temp: dict = self._clans_info.get('emblems')
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


        members_temp: dict = self._clans_info.get('members')
        members_class = None
        if isinstance(members_temp, dict):
            for key in members_temp:
                if str(key).isnumeric():
                    members_class = {key: MembersClass(data) for key, data in members_temp.items()}
                    break
                if key == 'account_id' or key == 'account_name' or key == 'joined_at' or key == 'role' or key == 'role_i18n':
                    members_class = MembersClass(members_temp)
                    break
        elif isinstance(members_temp, list):
            members_class = [MembersClass(data) for data in members_temp]
        if not members_class:
            members_class: MembersClass = MembersClass(members_temp)
        self.members: MembersClass | list[MembersClass] | dict[str, MembersClass] = members_class
        del members_temp, members_class


        private_temp: dict = self._clans_info.get('private')
        private_class = None
        if isinstance(private_temp, dict):
            for key in private_temp:
                if str(key).isnumeric():
                    private_class = {key: PrivateClass(data) for key, data in private_temp.items()}
                    break
                if key == 'online_members' or key == 'treasury' or key == 'clan_treasury':
                    private_class = PrivateClass(private_temp)
                    break
        elif isinstance(private_temp, list):
            private_class = [PrivateClass(data) for data in private_temp]
        if not private_class:
            private_class: PrivateClass = PrivateClass(private_temp)
        self.private: PrivateClass | list[PrivateClass] | dict[str, PrivateClass] = private_class
        del private_temp, private_class


