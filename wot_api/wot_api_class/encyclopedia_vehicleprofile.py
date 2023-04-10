class StunClass:
    def __init__(self, stun_data: dict):
        if not stun_data: stun_data = {}
        self._stun: dict = stun_data
        self.duration: list = stun_data.get('duration', [])

class AmmoClass:
    def __init__(self, ammo_data: dict):
        if not ammo_data: ammo_data = {}
        self._ammo: dict = ammo_data
        self.damage: list = ammo_data.get('damage', [])
        self.penetration: list = ammo_data.get('penetration', [])
        self.type: str = ammo_data.get('type', '')

        stun_temp: dict = self._ammo.get('stun')
        stun_class = None
        if isinstance(stun_temp, dict):
            for key in stun_temp:
                if str(key).isnumeric():
                    stun_class = {key: StunClass(data) for key, data in stun_temp.items()}
                    break
                if key == 'duration':
                    stun_class = StunClass(stun_temp)
                    break
        elif isinstance(stun_temp, list):
            stun_class = [StunClass(data) for data in stun_temp]
        if not stun_class:
            stun_class: StunClass = StunClass(stun_temp)
        self.stun: StunClass | list[StunClass] | dict[str, StunClass] = stun_class
        del stun_temp, stun_class


class HullClass:
    def __init__(self, hull_data: dict):
        if not hull_data: hull_data = {}
        self._hull: dict = hull_data
        self.front: int = hull_data.get('front', 0)
        self.rear: int = hull_data.get('rear', 0)
        self.sides: int = hull_data.get('sides', 0)

class TurretClass:
    def __init__(self, turret_data: dict):
        if not turret_data: turret_data = {}
        self._turret: dict = turret_data
        self.front: int = turret_data.get('front', 0)
        self.rear: int = turret_data.get('rear', 0)
        self.sides: int = turret_data.get('sides', 0)

class ArmorClass:
    def __init__(self, armor_data: dict):
        if not armor_data: armor_data = {}
        self._armor: dict = armor_data

        hull_temp: dict = self._armor.get('hull')
        hull_class = None
        if isinstance(hull_temp, dict):
            for key in hull_temp:
                if str(key).isnumeric():
                    hull_class = {key: HullClass(data) for key, data in hull_temp.items()}
                    break
                if key == 'front' or key == 'rear' or key == 'sides':
                    hull_class = HullClass(hull_temp)
                    break
        elif isinstance(hull_temp, list):
            hull_class = [HullClass(data) for data in hull_temp]
        if not hull_class:
            hull_class: HullClass = HullClass(hull_temp)
        self.hull: HullClass | list[HullClass] | dict[str, HullClass] = hull_class
        del hull_temp, hull_class


        turret_temp: dict = self._armor.get('turret')
        turret_class = None
        if isinstance(turret_temp, dict):
            for key in turret_temp:
                if str(key).isnumeric():
                    turret_class = {key: TurretClass(data) for key, data in turret_temp.items()}
                    break
                if key == 'front' or key == 'rear' or key == 'sides':
                    turret_class = TurretClass(turret_temp)
                    break
        elif isinstance(turret_temp, list):
            turret_class = [TurretClass(data) for data in turret_temp]
        if not turret_class:
            turret_class: TurretClass = TurretClass(turret_temp)
        self.turret: TurretClass | list[TurretClass] | dict[str, TurretClass] = turret_class
        del turret_temp, turret_class


class EngineClass:
    def __init__(self, engine_data: dict):
        if not engine_data: engine_data = {}
        self._engine: dict = engine_data
        self.fire_chance: float = engine_data.get('fire_chance', 0.0)
        self.name: str = engine_data.get('name', '')
        self.power: int = engine_data.get('power', 0)
        self.tag: str = engine_data.get('tag', '')
        self.tier: int = engine_data.get('tier', 0)
        self.weight: int = engine_data.get('weight', 0)

class GunClass:
    def __init__(self, gun_data: dict):
        if not gun_data: gun_data = {}
        self._gun: dict = gun_data
        self.aim_time: float = gun_data.get('aim_time', 0.0)
        self.caliber: int = gun_data.get('caliber', 0)
        self.dispersion: float = gun_data.get('dispersion', 0.0)
        self.fire_rate: float = gun_data.get('fire_rate', 0.0)
        self.move_down_arc: int = gun_data.get('move_down_arc', 0)
        self.move_up_arc: int = gun_data.get('move_up_arc', 0)
        self.name: str = gun_data.get('name', '')
        self.reload_time: float = gun_data.get('reload_time', 0.0)
        self.tag: str = gun_data.get('tag', '')
        self.tier: int = gun_data.get('tier', 0)
        self.traverse_speed: int = gun_data.get('traverse_speed', 0)
        self.weight: int = gun_data.get('weight', 0)

class ModulesClass:
    def __init__(self, modules_data: dict):
        if not modules_data: modules_data = {}
        self._modules: dict = modules_data
        self.engine_id: int = modules_data.get('engine_id', 0)
        self.gun_id: int = modules_data.get('gun_id', 0)
        self.radio_id: int = modules_data.get('radio_id', 0)
        self.suspension_id: int = modules_data.get('suspension_id', 0)
        self.turret_id: int = modules_data.get('turret_id', 0)

class RadioClass:
    def __init__(self, radio_data: dict):
        if not radio_data: radio_data = {}
        self._radio: dict = radio_data
        self.name: str = radio_data.get('name', '')
        self.signal_range: int = radio_data.get('signal_range', 0)
        self.tag: str = radio_data.get('tag', '')
        self.tier: int = radio_data.get('tier', 0)
        self.weight: int = radio_data.get('weight', 0)

class RapidClass:
    def __init__(self, rapid_data: dict):
        if not rapid_data: rapid_data = {}
        self._rapid: dict = rapid_data
        self.speed_backward: int = rapid_data.get('speed_backward', 0)
        self.speed_forward: int = rapid_data.get('speed_forward', 0)
        self.suspension_steering_lock_angle: int = rapid_data.get('suspension_steering_lock_angle', 0)
        self.switch_off_time: float = rapid_data.get('switch_off_time', 0.0)
        self.switch_on_time: float = rapid_data.get('switch_on_time', 0.0)

class SiegeClass:
    def __init__(self, siege_data: dict):
        if not siege_data: siege_data = {}
        self._siege: dict = siege_data
        self.aim_time: float = siege_data.get('aim_time', 0.0)
        self.dispersion: float = siege_data.get('dispersion', 0.0)
        self.move_down_arc: int = siege_data.get('move_down_arc', 0)
        self.move_up_arc: int = siege_data.get('move_up_arc', 0)
        self.reload_time: float = siege_data.get('reload_time', 0.0)
        self.speed_backward: int = siege_data.get('speed_backward', 0)
        self.suspension_traverse_speed: int = siege_data.get('suspension_traverse_speed', 0)
        self.switch_off_time: float = siege_data.get('switch_off_time', 0.0)
        self.switch_on_time: float = siege_data.get('switch_on_time', 0.0)

class SuspensionClass:
    def __init__(self, suspension_data: dict):
        if not suspension_data: suspension_data = {}
        self._suspension: dict = suspension_data
        self.load_limit: int = suspension_data.get('load_limit', 0)
        self.name: str = suspension_data.get('name', '')
        self.steering_lock_angle: int = suspension_data.get('steering_lock_angle', 0)
        self.tag: str = suspension_data.get('tag', '')
        self.tier: int = suspension_data.get('tier', 0)
        self.traverse_speed: int = suspension_data.get('traverse_speed', 0)
        self.weight: int = suspension_data.get('weight', 0)

class TurretClass:
    def __init__(self, turret_data: dict):
        if not turret_data: turret_data = {}
        self._turret: dict = turret_data
        self.hp: int = turret_data.get('hp', 0)
        self.name: str = turret_data.get('name', '')
        self.tag: str = turret_data.get('tag', '')
        self.tier: int = turret_data.get('tier', 0)
        self.traverse_left_arc: int = turret_data.get('traverse_left_arc', 0)
        self.traverse_right_arc: int = turret_data.get('traverse_right_arc', 0)
        self.traverse_speed: int = turret_data.get('traverse_speed', 0)
        self.view_range: int = turret_data.get('view_range', 0)
        self.weight: int = turret_data.get('weight', 0)

class EncyclopediaVehicleprofileClass:
    def __init__(self, encyclopedia_vehicleprofile_data: dict):
        if not encyclopedia_vehicleprofile_data: encyclopedia_vehicleprofile_data = {}
        self._encyclopedia_vehicleprofile: dict = encyclopedia_vehicleprofile_data
        self.hp: int = encyclopedia_vehicleprofile_data.get('hp', 0)
        self.hull_hp: int = encyclopedia_vehicleprofile_data.get('hull_hp', 0)
        self.hull_weight: int = encyclopedia_vehicleprofile_data.get('hull_weight', 0)
        self.is_default: bool = encyclopedia_vehicleprofile_data.get('is_default', False)
        self.max_ammo: int = encyclopedia_vehicleprofile_data.get('max_ammo', 0)
        self.max_weight: int = encyclopedia_vehicleprofile_data.get('max_weight', 0)
        self.profile_id: str = encyclopedia_vehicleprofile_data.get('profile_id', '')
        self.speed_backward: int = encyclopedia_vehicleprofile_data.get('speed_backward', 0)
        self.speed_forward: int = encyclopedia_vehicleprofile_data.get('speed_forward', 0)
        self.tank_id: int = encyclopedia_vehicleprofile_data.get('tank_id', 0)
        self.weight: int = encyclopedia_vehicleprofile_data.get('weight', 0)

        ammo_temp: dict = self._encyclopedia_vehicleprofile.get('ammo')
        ammo_class = None
        if isinstance(ammo_temp, dict):
            for key in ammo_temp:
                if str(key).isnumeric():
                    ammo_class = {key: AmmoClass(data) for key, data in ammo_temp.items()}
                    break
                if key == 'damage' or key == 'penetration' or key == 'type' or key == 'stun':
                    ammo_class = AmmoClass(ammo_temp)
                    break
        elif isinstance(ammo_temp, list):
            ammo_class = [AmmoClass(data) for data in ammo_temp]
        if not ammo_class:
            ammo_class: AmmoClass = AmmoClass(ammo_temp)
        self.ammo: AmmoClass | list[AmmoClass] | dict[str, AmmoClass] = ammo_class
        del ammo_temp, ammo_class


        armor_temp: dict = self._encyclopedia_vehicleprofile.get('armor')
        armor_class = None
        if isinstance(armor_temp, dict):
            for key in armor_temp:
                if str(key).isnumeric():
                    armor_class = {key: ArmorClass(data) for key, data in armor_temp.items()}
                    break
                if key == 'hull' or key == 'turret':
                    armor_class = ArmorClass(armor_temp)
                    break
        elif isinstance(armor_temp, list):
            armor_class = [ArmorClass(data) for data in armor_temp]
        if not armor_class:
            armor_class: ArmorClass = ArmorClass(armor_temp)
        self.armor: ArmorClass | list[ArmorClass] | dict[str, ArmorClass] = armor_class
        del armor_temp, armor_class


        engine_temp: dict = self._encyclopedia_vehicleprofile.get('engine')
        engine_class = None
        if isinstance(engine_temp, dict):
            for key in engine_temp:
                if str(key).isnumeric():
                    engine_class = {key: EngineClass(data) for key, data in engine_temp.items()}
                    break
                if key == 'fire_chance' or key == 'name' or key == 'power' or key == 'tag' or key == 'tier' or key == 'weight':
                    engine_class = EngineClass(engine_temp)
                    break
        elif isinstance(engine_temp, list):
            engine_class = [EngineClass(data) for data in engine_temp]
        if not engine_class:
            engine_class: EngineClass = EngineClass(engine_temp)
        self.engine: EngineClass | list[EngineClass] | dict[str, EngineClass] = engine_class
        del engine_temp, engine_class


        gun_temp: dict = self._encyclopedia_vehicleprofile.get('gun')
        gun_class = None
        if isinstance(gun_temp, dict):
            for key in gun_temp:
                if str(key).isnumeric():
                    gun_class = {key: GunClass(data) for key, data in gun_temp.items()}
                    break
                if key == 'aim_time' or key == 'caliber' or key == 'dispersion' or key == 'fire_rate' or key == 'move_down_arc' or key == 'move_up_arc' or key == 'name' or key == 'reload_time' or key == 'tag' or key == 'tier' or key == 'traverse_speed' or key == 'weight':
                    gun_class = GunClass(gun_temp)
                    break
        elif isinstance(gun_temp, list):
            gun_class = [GunClass(data) for data in gun_temp]
        if not gun_class:
            gun_class: GunClass = GunClass(gun_temp)
        self.gun: GunClass | list[GunClass] | dict[str, GunClass] = gun_class
        del gun_temp, gun_class


        modules_temp: dict = self._encyclopedia_vehicleprofile.get('modules')
        modules_class = None
        if isinstance(modules_temp, dict):
            for key in modules_temp:
                if str(key).isnumeric():
                    modules_class = {key: ModulesClass(data) for key, data in modules_temp.items()}
                    break
                if key == 'engine_id' or key == 'gun_id' or key == 'radio_id' or key == 'suspension_id' or key == 'turret_id':
                    modules_class = ModulesClass(modules_temp)
                    break
        elif isinstance(modules_temp, list):
            modules_class = [ModulesClass(data) for data in modules_temp]
        if not modules_class:
            modules_class: ModulesClass = ModulesClass(modules_temp)
        self.modules: ModulesClass | list[ModulesClass] | dict[str, ModulesClass] = modules_class
        del modules_temp, modules_class


        radio_temp: dict = self._encyclopedia_vehicleprofile.get('radio')
        radio_class = None
        if isinstance(radio_temp, dict):
            for key in radio_temp:
                if str(key).isnumeric():
                    radio_class = {key: RadioClass(data) for key, data in radio_temp.items()}
                    break
                if key == 'name' or key == 'signal_range' or key == 'tag' or key == 'tier' or key == 'weight':
                    radio_class = RadioClass(radio_temp)
                    break
        elif isinstance(radio_temp, list):
            radio_class = [RadioClass(data) for data in radio_temp]
        if not radio_class:
            radio_class: RadioClass = RadioClass(radio_temp)
        self.radio: RadioClass | list[RadioClass] | dict[str, RadioClass] = radio_class
        del radio_temp, radio_class


        rapid_temp: dict = self._encyclopedia_vehicleprofile.get('rapid')
        rapid_class = None
        if isinstance(rapid_temp, dict):
            for key in rapid_temp:
                if str(key).isnumeric():
                    rapid_class = {key: RapidClass(data) for key, data in rapid_temp.items()}
                    break
                if key == 'speed_backward' or key == 'speed_forward' or key == 'suspension_steering_lock_angle' or key == 'switch_off_time' or key == 'switch_on_time':
                    rapid_class = RapidClass(rapid_temp)
                    break
        elif isinstance(rapid_temp, list):
            rapid_class = [RapidClass(data) for data in rapid_temp]
        if not rapid_class:
            rapid_class: RapidClass = RapidClass(rapid_temp)
        self.rapid: RapidClass | list[RapidClass] | dict[str, RapidClass] = rapid_class
        del rapid_temp, rapid_class


        siege_temp: dict = self._encyclopedia_vehicleprofile.get('siege')
        siege_class = None
        if isinstance(siege_temp, dict):
            for key in siege_temp:
                if str(key).isnumeric():
                    siege_class = {key: SiegeClass(data) for key, data in siege_temp.items()}
                    break
                if key == 'aim_time' or key == 'dispersion' or key == 'move_down_arc' or key == 'move_up_arc' or key == 'reload_time' or key == 'speed_backward' or key == 'suspension_traverse_speed' or key == 'switch_off_time' or key == 'switch_on_time':
                    siege_class = SiegeClass(siege_temp)
                    break
        elif isinstance(siege_temp, list):
            siege_class = [SiegeClass(data) for data in siege_temp]
        if not siege_class:
            siege_class: SiegeClass = SiegeClass(siege_temp)
        self.siege: SiegeClass | list[SiegeClass] | dict[str, SiegeClass] = siege_class
        del siege_temp, siege_class


        suspension_temp: dict = self._encyclopedia_vehicleprofile.get('suspension')
        suspension_class = None
        if isinstance(suspension_temp, dict):
            for key in suspension_temp:
                if str(key).isnumeric():
                    suspension_class = {key: SuspensionClass(data) for key, data in suspension_temp.items()}
                    break
                if key == 'load_limit' or key == 'name' or key == 'steering_lock_angle' or key == 'tag' or key == 'tier' or key == 'traverse_speed' or key == 'weight':
                    suspension_class = SuspensionClass(suspension_temp)
                    break
        elif isinstance(suspension_temp, list):
            suspension_class = [SuspensionClass(data) for data in suspension_temp]
        if not suspension_class:
            suspension_class: SuspensionClass = SuspensionClass(suspension_temp)
        self.suspension: SuspensionClass | list[SuspensionClass] | dict[str, SuspensionClass] = suspension_class
        del suspension_temp, suspension_class


        turret_temp: dict = self._encyclopedia_vehicleprofile.get('turret')
        turret_class = None
        if isinstance(turret_temp, dict):
            for key in turret_temp:
                if str(key).isnumeric():
                    turret_class = {key: TurretClass(data) for key, data in turret_temp.items()}
                    break
                if key == 'hp' or key == 'name' or key == 'tag' or key == 'tier' or key == 'traverse_left_arc' or key == 'traverse_right_arc' or key == 'traverse_speed' or key == 'view_range' or key == 'weight':
                    turret_class = TurretClass(turret_temp)
                    break
        elif isinstance(turret_temp, list):
            turret_class = [TurretClass(data) for data in turret_temp]
        if not turret_class:
            turret_class: TurretClass = TurretClass(turret_temp)
        self.turret: TurretClass | list[TurretClass] | dict[str, TurretClass] = turret_class
        del turret_temp, turret_class


