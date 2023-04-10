class BonusValuesClass:
    def __init__(self, bonus_values_data: dict):
        if not bonus_values_data: bonus_values_data = {}
        self._bonus_values: dict = bonus_values_data
        self.battle_type: str = bonus_values_data.get('battle_type', '')
        self.value: float = bonus_values_data.get('value', 0.0)

class InStockClass:
    def __init__(self, in_stock_data: dict):
        if not in_stock_data: in_stock_data = {}
        self._in_stock: dict = in_stock_data
        self.action_time: int = in_stock_data.get('action_time', 0)
        self.activated_at: int = in_stock_data.get('activated_at', 0)
        self.active_till: int = in_stock_data.get('active_till', 0)
        self.amount: int = in_stock_data.get('amount', 0)
        self.level: int = in_stock_data.get('level', 0)
        self.status: str = in_stock_data.get('status', '')
        self.x_level_only: bool = in_stock_data.get('x_level_only', False)

        bonus_values_temp: dict = self._in_stock.get('bonus_values')
        bonus_values_class = None
        if isinstance(bonus_values_temp, dict):
            for key in bonus_values_temp:
                if str(key).isnumeric():
                    bonus_values_class = {key: BonusValuesClass(data) for key, data in bonus_values_temp.items()}
                    break
                if key == 'battle_type' or key == 'value':
                    bonus_values_class = BonusValuesClass(bonus_values_temp)
                    break
        elif isinstance(bonus_values_temp, list):
            bonus_values_class = [BonusValuesClass(data) for data in bonus_values_temp]
        if not bonus_values_class:
            bonus_values_class: BonusValuesClass = BonusValuesClass(bonus_values_temp)
        self.bonus_values: BonusValuesClass | list[BonusValuesClass] | dict[str, BonusValuesClass] = bonus_values_class
        del bonus_values_temp, bonus_values_class


class StrongholdClanreservesClass:
    def __init__(self, stronghold_clanreserves_data: dict):
        if not stronghold_clanreserves_data: stronghold_clanreserves_data = {}
        self._stronghold_clanreserves: dict = stronghold_clanreserves_data
        self.bonus_type: str = stronghold_clanreserves_data.get('bonus_type', '')
        self.disposable: bool = stronghold_clanreserves_data.get('disposable', False)
        self.icon: str = stronghold_clanreserves_data.get('icon', '')
        self.name: str = stronghold_clanreserves_data.get('name', '')
        self.type: str = stronghold_clanreserves_data.get('type', '')

        in_stock_temp: dict = self._stronghold_clanreserves.get('in_stock')
        in_stock_class = None
        if isinstance(in_stock_temp, dict):
            for key in in_stock_temp:
                if str(key).isnumeric():
                    in_stock_class = {key: InStockClass(data) for key, data in in_stock_temp.items()}
                    break
                if key == 'action_time' or key == 'activated_at' or key == 'active_till' or key == 'amount' or key == 'level' or key == 'status' or key == 'x_level_only' or key == 'bonus_values':
                    in_stock_class = InStockClass(in_stock_temp)
                    break
        elif isinstance(in_stock_temp, list):
            in_stock_class = [InStockClass(data) for data in in_stock_temp]
        if not in_stock_class:
            in_stock_class: InStockClass = InStockClass(in_stock_temp)
        self.in_stock: InStockClass | list[InStockClass] | dict[str, InStockClass] = in_stock_class
        del in_stock_temp, in_stock_class


