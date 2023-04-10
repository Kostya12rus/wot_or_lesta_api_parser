class TanksMasteryClass:
    def __init__(self, tanks_mastery_data: dict):
        if not tanks_mastery_data: tanks_mastery_data = {}
        self._tanks_mastery: dict = tanks_mastery_data
        self.distribution: dict = tanks_mastery_data.get('distribution', {})
        self.updated_at: int = tanks_mastery_data.get('updated_at', 0)

