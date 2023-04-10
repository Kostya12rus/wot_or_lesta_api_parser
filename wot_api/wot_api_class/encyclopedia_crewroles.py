class EncyclopediaCrewrolesClass:
    def __init__(self, encyclopedia_crewroles_data: dict):
        if not encyclopedia_crewroles_data: encyclopedia_crewroles_data = {}
        self._encyclopedia_crewroles: dict = encyclopedia_crewroles_data
        self.name: str = encyclopedia_crewroles_data.get('name', '')
        self.role: str = encyclopedia_crewroles_data.get('role', '')
        self.skills: list = encyclopedia_crewroles_data.get('skills', [])

