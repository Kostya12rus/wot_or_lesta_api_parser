class EncyclopediaArenasClass:
    def __init__(self, encyclopedia_arenas_data: dict):
        if not encyclopedia_arenas_data: encyclopedia_arenas_data = {}
        self._encyclopedia_arenas: dict = encyclopedia_arenas_data
        self.arena_id: str = encyclopedia_arenas_data.get('arena_id', '')
        self.camouflage_type: str = encyclopedia_arenas_data.get('camouflage_type', '')
        self.description: str = encyclopedia_arenas_data.get('description', '')
        self.name_i18n: str = encyclopedia_arenas_data.get('name_i18n', '')

