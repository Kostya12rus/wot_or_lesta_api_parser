class EncyclopediaVehicleprofilesClass:
    def __init__(self, encyclopedia_vehicleprofiles_data: dict):
        if not encyclopedia_vehicleprofiles_data: encyclopedia_vehicleprofiles_data = {}
        self._encyclopedia_vehicleprofiles: dict = encyclopedia_vehicleprofiles_data
        self.is_default: bool = encyclopedia_vehicleprofiles_data.get('is_default', False)
        self.price_credit: int = encyclopedia_vehicleprofiles_data.get('price_credit', 0)
        self.profile_id: str = encyclopedia_vehicleprofiles_data.get('profile_id', '')
        self.tank_id: int = encyclopedia_vehicleprofiles_data.get('tank_id', 0)

