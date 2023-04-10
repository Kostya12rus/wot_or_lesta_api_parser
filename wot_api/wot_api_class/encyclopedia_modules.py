class EngineClass:
    def __init__(self, engine_data: dict):
        if not engine_data: engine_data = {}
        self._engine: dict = engine_data
        self.fire_chance: float = engine_data.get('fire_chance', 0.0)
        self.power: int = engine_data.get('power', 0)

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


class GunClass:
    def __init__(self, gun_data: dict):
        if not gun_data: gun_data = {}
        self._gun: dict = gun_data
        self.aim_time: float = gun_data.get('aim_time', 0.0)
        self.dispersion: float = gun_data.get('dispersion', 0.0)
        self.fire_rate: float = gun_data.get('fire_rate', 0.0)
        self.max_ammo: int = gun_data.get('max_ammo', 0)
        self.move_down_arc: int = gun_data.get('move_down_arc', 0)
        self.move_up_arc: int = gun_data.get('move_up_arc', 0)
        self.reload_time: float = gun_data.get('reload_time', 0.0)
        self.traverse_speed: int = gun_data.get('traverse_speed', 0)

        ammo_temp: dict = self._gun.get('ammo')
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


class RadioClass:
    def __init__(self, radio_data: dict):
        if not radio_data: radio_data = {}
        self._radio: dict = radio_data
        self.signal_range: int = radio_data.get('signal_range', 0)

class SuspensionClass:
    def __init__(self, suspension_data: dict):
        if not suspension_data: suspension_data = {}
        self._suspension: dict = suspension_data
        self.load_limit: int = suspension_data.get('load_limit', 0)
        self.traverse_speed: int = suspension_data.get('traverse_speed', 0)

class TurretClass:
    def __init__(self, turret_data: dict):
        if not turret_data: turret_data = {}
        self._turret: dict = turret_data
        self.armor_front: int = turret_data.get('armor_front', 0)
        self.armor_rear: int = turret_data.get('armor_rear', 0)
        self.armor_sides: int = turret_data.get('armor_sides', 0)
        self.hp: int = turret_data.get('hp', 0)
        self.traverse_speed: int = turret_data.get('traverse_speed', 0)
        self.view_range: int = turret_data.get('view_range', 0)

class DefaultProfileClass:
    def __init__(self, default_profile_data: dict):
        if not default_profile_data: default_profile_data = {}
        self._default_profile: dict = default_profile_data

        engine_temp: dict = self._default_profile.get('engine')
        engine_class = None
        if isinstance(engine_temp, dict):
            for key in engine_temp:
                if str(key).isnumeric():
                    engine_class = {key: EngineClass(data) for key, data in engine_temp.items()}
                    break
                if key == 'fire_chance' or key == 'power':
                    engine_class = EngineClass(engine_temp)
                    break
        elif isinstance(engine_temp, list):
            engine_class = [EngineClass(data) for data in engine_temp]
        if not engine_class:
            engine_class: EngineClass = EngineClass(engine_temp)
        self.engine: EngineClass | list[EngineClass] | dict[str, EngineClass] = engine_class
        del engine_temp, engine_class


        gun_temp: dict = self._default_profile.get('gun')
        gun_class = None
        if isinstance(gun_temp, dict):
            for key in gun_temp:
                if str(key).isnumeric():
                    gun_class = {key: GunClass(data) for key, data in gun_temp.items()}
                    break
                if key == 'aim_time' or key == 'dispersion' or key == 'fire_rate' or key == 'max_ammo' or key == 'move_down_arc' or key == 'move_up_arc' or key == 'reload_time' or key == 'traverse_speed' or key == 'ammo':
                    gun_class = GunClass(gun_temp)
                    break
        elif isinstance(gun_temp, list):
            gun_class = [GunClass(data) for data in gun_temp]
        if not gun_class:
            gun_class: GunClass = GunClass(gun_temp)
        self.gun: GunClass | list[GunClass] | dict[str, GunClass] = gun_class
        del gun_temp, gun_class


        radio_temp: dict = self._default_profile.get('radio')
        radio_class = None
        if isinstance(radio_temp, dict):
            for key in radio_temp:
                if str(key).isnumeric():
                    radio_class = {key: RadioClass(data) for key, data in radio_temp.items()}
                    break
                if key == 'signal_range':
                    radio_class = RadioClass(radio_temp)
                    break
        elif isinstance(radio_temp, list):
            radio_class = [RadioClass(data) for data in radio_temp]
        if not radio_class:
            radio_class: RadioClass = RadioClass(radio_temp)
        self.radio: RadioClass | list[RadioClass] | dict[str, RadioClass] = radio_class
        del radio_temp, radio_class


        suspension_temp: dict = self._default_profile.get('suspension')
        suspension_class = None
        if isinstance(suspension_temp, dict):
            for key in suspension_temp:
                if str(key).isnumeric():
                    suspension_class = {key: SuspensionClass(data) for key, data in suspension_temp.items()}
                    break
                if key == 'load_limit' or key == 'traverse_speed':
                    suspension_class = SuspensionClass(suspension_temp)
                    break
        elif isinstance(suspension_temp, list):
            suspension_class = [SuspensionClass(data) for data in suspension_temp]
        if not suspension_class:
            suspension_class: SuspensionClass = SuspensionClass(suspension_temp)
        self.suspension: SuspensionClass | list[SuspensionClass] | dict[str, SuspensionClass] = suspension_class
        del suspension_temp, suspension_class


        turret_temp: dict = self._default_profile.get('turret')
        turret_class = None
        if isinstance(turret_temp, dict):
            for key in turret_temp:
                if str(key).isnumeric():
                    turret_class = {key: TurretClass(data) for key, data in turret_temp.items()}
                    break
                if key == 'armor_front' or key == 'armor_rear' or key == 'armor_sides' or key == 'hp' or key == 'traverse_speed' or key == 'view_range':
                    turret_class = TurretClass(turret_temp)
                    break
        elif isinstance(turret_temp, list):
            turret_class = [TurretClass(data) for data in turret_temp]
        if not turret_class:
            turret_class: TurretClass = TurretClass(turret_temp)
        self.turret: TurretClass | list[TurretClass] | dict[str, TurretClass] = turret_class
        del turret_temp, turret_class


class EncyclopediaModulesClass:
    def __init__(self, encyclopedia_modules_data: dict):
        if not encyclopedia_modules_data: encyclopedia_modules_data = {}
        self._encyclopedia_modules: dict = encyclopedia_modules_data
        self.image: str = encyclopedia_modules_data.get('image', '')
        self.module_id: int = encyclopedia_modules_data.get('module_id', 0)
        self.name: str = encyclopedia_modules_data.get('name', '')
        self.nation: str = encyclopedia_modules_data.get('nation', '')
        self.price_credit: int = encyclopedia_modules_data.get('price_credit', 0)
        self.tanks: list = encyclopedia_modules_data.get('tanks', [])
        self.tier: int = encyclopedia_modules_data.get('tier', 0)
        self.type: str = encyclopedia_modules_data.get('type', '')
        self.weight: int = encyclopedia_modules_data.get('weight', 0)

        default_profile_temp: dict = self._encyclopedia_modules.get('default_profile')
        default_profile_class = None
        if isinstance(default_profile_temp, dict):
            for key in default_profile_temp:
                if str(key).isnumeric():
                    default_profile_class = {key: DefaultProfileClass(data) for key, data in default_profile_temp.items()}
                    break
                if key == 'engine' or key == 'gun' or key == 'radio' or key == 'suspension' or key == 'turret':
                    default_profile_class = DefaultProfileClass(default_profile_temp)
                    break
        elif isinstance(default_profile_temp, list):
            default_profile_class = [DefaultProfileClass(data) for data in default_profile_temp]
        if not default_profile_class:
            default_profile_class: DefaultProfileClass = DefaultProfileClass(default_profile_temp)
        self.default_profile: DefaultProfileClass | list[DefaultProfileClass] | dict[str, DefaultProfileClass] = default_profile_class
        del default_profile_temp, default_profile_class


