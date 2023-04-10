class ClansGlossaryClass:
    def __init__(self, clans_glossary_data: dict):
        if not clans_glossary_data: clans_glossary_data = {}
        self._clans_glossary: dict = clans_glossary_data
        self.clans_roles: dict = clans_glossary_data.get('clans_roles', {})

