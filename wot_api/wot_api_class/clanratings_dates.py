class ClanratingsDatesClass:
    def __init__(self, clanratings_dates_data: dict):
        if not clanratings_dates_data: clanratings_dates_data = {}
        self._clanratings_dates: dict = clanratings_dates_data
        self.dates: list = clanratings_dates_data.get('dates', [])

