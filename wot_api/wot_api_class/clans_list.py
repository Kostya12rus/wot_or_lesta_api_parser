class EmblemsClass:
    def __init__(self, emblems_data: dict):
        if not emblems_data: emblems_data = {}
        self._emblems: dict = emblems_data
        self.x195: dict = emblems_data.get('x195', {})
        self.x24: dict = emblems_data.get('x24', {})
        self.x256: dict = emblems_data.get('x256', {})
        self.x32: dict = emblems_data.get('x32', {})
        self.x64: dict = emblems_data.get('x64', {})

class ClansListClass:
    def __init__(self, clans_list_data: dict):
        if not clans_list_data: clans_list_data = {}
        self._clans_list: dict = clans_list_data
        self.clan_id: int = clans_list_data.get('clan_id', 0)
        self.color: str = clans_list_data.get('color', '')
        self.created_at: int = clans_list_data.get('created_at', 0)
        self.members_count: int = clans_list_data.get('members_count', 0)
        self.name: str = clans_list_data.get('name', '')
        self.tag: str = clans_list_data.get('tag', '')

        emblems_temp: dict = self._clans_list.get('emblems')
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


