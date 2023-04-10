class RewardsClass:
    def __init__(self, rewards_data: dict):
        if not rewards_data: rewards_data = {}
        self._rewards: dict = rewards_data
        self.berths: int = rewards_data.get('berths', 0)
        self.conditions: str = rewards_data.get('conditions', '')
        self.credits: int = rewards_data.get('credits', 0)
        self.free_xp: int = rewards_data.get('free_xp', 0)
        self.items: dict = rewards_data.get('items', {})
        self.premium: int = rewards_data.get('premium', 0)
        self.slots: int = rewards_data.get('slots', 0)
        self.tokens: int = rewards_data.get('tokens', 0)

class MissionsClass:
    def __init__(self, missions_data: dict):
        if not missions_data: missions_data = {}
        self._missions: dict = missions_data
        self.description: str = missions_data.get('description', '')
        self.hint: str = missions_data.get('hint', '')
        self.max_level: int = missions_data.get('max_level', 0)
        self.min_level: int = missions_data.get('min_level', 0)
        self.mission_id: int = missions_data.get('mission_id', 0)
        self.name: str = missions_data.get('name', '')
        self.set_id: int = missions_data.get('set_id', 0)
        self.tags: list = missions_data.get('tags', [])

        rewards_temp: dict = self._missions.get('rewards')
        rewards_class = None
        if isinstance(rewards_temp, dict):
            for key in rewards_temp:
                if str(key).isnumeric():
                    rewards_class = {key: RewardsClass(data) for key, data in rewards_temp.items()}
                    break
                if key == 'berths' or key == 'conditions' or key == 'credits' or key == 'free_xp' or key == 'items' or key == 'premium' or key == 'slots' or key == 'tokens':
                    rewards_class = RewardsClass(rewards_temp)
                    break
        elif isinstance(rewards_temp, list):
            rewards_class = [RewardsClass(data) for data in rewards_temp]
        if not rewards_class:
            rewards_class: RewardsClass = RewardsClass(rewards_temp)
        self.rewards: RewardsClass | list[RewardsClass] | dict[str, RewardsClass] = rewards_class
        del rewards_temp, rewards_class


class RewardClass:
    def __init__(self, reward_data: dict):
        if not reward_data: reward_data = {}
        self._reward: dict = reward_data
        self.slots: int = reward_data.get('slots', 0)
        self.tanks: list = reward_data.get('tanks', [])

class OperationsClass:
    def __init__(self, operations_data: dict):
        if not operations_data: operations_data = {}
        self._operations: dict = operations_data
        self.description: str = operations_data.get('description', '')
        self.image: str = operations_data.get('image', '')
        self.missions_in_set: int = operations_data.get('missions_in_set', 0)
        self.name: str = operations_data.get('name', '')
        self.next_id: int = operations_data.get('next_id', 0)
        self.operation_id: int = operations_data.get('operation_id', 0)
        self.sets_count: int = operations_data.get('sets_count', 0)
        self.sets_to_next: int = operations_data.get('sets_to_next', 0)

        missions_temp: dict = self._operations.get('missions')
        missions_class = None
        if isinstance(missions_temp, dict):
            for key in missions_temp:
                if str(key).isnumeric():
                    missions_class = {key: MissionsClass(data) for key, data in missions_temp.items()}
                    break
                if key == 'description' or key == 'hint' or key == 'max_level' or key == 'min_level' or key == 'mission_id' or key == 'name' or key == 'set_id' or key == 'tags' or key == 'rewards':
                    missions_class = MissionsClass(missions_temp)
                    break
        elif isinstance(missions_temp, list):
            missions_class = [MissionsClass(data) for data in missions_temp]
        if not missions_class:
            missions_class: MissionsClass = MissionsClass(missions_temp)
        self.missions: MissionsClass | list[MissionsClass] | dict[str, MissionsClass] = missions_class
        del missions_temp, missions_class


        reward_temp: dict = self._operations.get('reward')
        reward_class = None
        if isinstance(reward_temp, dict):
            for key in reward_temp:
                if str(key).isnumeric():
                    reward_class = {key: RewardClass(data) for key, data in reward_temp.items()}
                    break
                if key == 'slots' or key == 'tanks':
                    reward_class = RewardClass(reward_temp)
                    break
        elif isinstance(reward_temp, list):
            reward_class = [RewardClass(data) for data in reward_temp]
        if not reward_class:
            reward_class: RewardClass = RewardClass(reward_temp)
        self.reward: RewardClass | list[RewardClass] | dict[str, RewardClass] = reward_class
        del reward_temp, reward_class


class EncyclopediaPersonalmissionsClass:
    def __init__(self, encyclopedia_personalmissions_data: dict):
        if not encyclopedia_personalmissions_data: encyclopedia_personalmissions_data = {}
        self._encyclopedia_personalmissions: dict = encyclopedia_personalmissions_data
        self.campaign_id: int = encyclopedia_personalmissions_data.get('campaign_id', 0)
        self.description: str = encyclopedia_personalmissions_data.get('description', '')
        self.name: str = encyclopedia_personalmissions_data.get('name', '')

        operations_temp: dict = self._encyclopedia_personalmissions.get('operations')
        operations_class = None
        if isinstance(operations_temp, dict):
            for key in operations_temp:
                if str(key).isnumeric():
                    operations_class = {key: OperationsClass(data) for key, data in operations_temp.items()}
                    break
                if key == 'description' or key == 'image' or key == 'missions_in_set' or key == 'name' or key == 'next_id' or key == 'operation_id' or key == 'sets_count' or key == 'sets_to_next' or key == 'missions' or key == 'reward':
                    operations_class = OperationsClass(operations_temp)
                    break
        elif isinstance(operations_temp, list):
            operations_class = [OperationsClass(data) for data in operations_temp]
        if not operations_class:
            operations_class: OperationsClass = OperationsClass(operations_temp)
        self.operations: OperationsClass | list[OperationsClass] | dict[str, OperationsClass] = operations_class
        del operations_temp, operations_class


