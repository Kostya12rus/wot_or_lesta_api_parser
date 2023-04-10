class AchievementSectionsClass:
    def __init__(self, achievement_sections_data: dict):
        if not achievement_sections_data: achievement_sections_data = {}
        self._achievement_sections: dict = achievement_sections_data
        self.name: str = achievement_sections_data.get('name', '')
        self.order: int = achievement_sections_data.get('order', 0)

class EncyclopediaInfoClass:
    def __init__(self, encyclopedia_info_data: dict):
        if not encyclopedia_info_data: encyclopedia_info_data = {}
        self._encyclopedia_info: dict = encyclopedia_info_data
        self.game_version: str = encyclopedia_info_data.get('game_version', '')
        self.languages: dict = encyclopedia_info_data.get('languages', {})
        self.tanks_updated_at: int = encyclopedia_info_data.get('tanks_updated_at', 0)
        self.vehicle_crew_roles: dict = encyclopedia_info_data.get('vehicle_crew_roles', {})
        self.vehicle_nations: dict = encyclopedia_info_data.get('vehicle_nations', {})
        self.vehicle_types: dict = encyclopedia_info_data.get('vehicle_types', {})

        achievement_sections_temp: dict = self._encyclopedia_info.get('achievement_sections')
        achievement_sections_class = None
        if isinstance(achievement_sections_temp, dict):
            for key in achievement_sections_temp:
                if str(key).isnumeric():
                    achievement_sections_class = {key: AchievementSectionsClass(data) for key, data in achievement_sections_temp.items()}
                    break
                if key == 'name' or key == 'order':
                    achievement_sections_class = AchievementSectionsClass(achievement_sections_temp)
                    break
        elif isinstance(achievement_sections_temp, list):
            achievement_sections_class = [AchievementSectionsClass(data) for data in achievement_sections_temp]
        if not achievement_sections_class:
            achievement_sections_class: AchievementSectionsClass = AchievementSectionsClass(achievement_sections_temp)
        self.achievement_sections: AchievementSectionsClass | list[AchievementSectionsClass] | dict[str, AchievementSectionsClass] = achievement_sections_class
        del achievement_sections_temp, achievement_sections_class


