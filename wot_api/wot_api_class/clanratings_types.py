class ClanratingsTypesClass:
    def __init__(self, clanratings_types_data: dict):
        if not clanratings_types_data: clanratings_types_data = {}
        self._clanratings_types: dict = clanratings_types_data
        self.rank_fields: list = clanratings_types_data.get('rank_fields', [])
        self.type: str = clanratings_types_data.get('type', '')

