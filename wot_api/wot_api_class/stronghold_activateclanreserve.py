class StrongholdActivateclanreserveClass:
    def __init__(self, stronghold_activateclanreserve_data: dict):
        if not stronghold_activateclanreserve_data: stronghold_activateclanreserve_data = {}
        self._stronghold_activateclanreserve: dict = stronghold_activateclanreserve_data
        self.activated_at: int = stronghold_activateclanreserve_data.get('activated_at', 0)

