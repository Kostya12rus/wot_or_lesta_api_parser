class NationImagesClass:
    def __init__(self, nation_images_data: dict):
        if not nation_images_data: nation_images_data = {}
        self._nation_images: dict = nation_images_data
        self.x180: dict = nation_images_data.get('x180', {})
        self.x71: dict = nation_images_data.get('x71', {})
        self.x85: dict = nation_images_data.get('x85', {})

class OptionsClass:
    def __init__(self, options_data: dict):
        if not options_data: options_data = {}
        self._options: dict = options_data
        self.description: str = options_data.get('description', '')
        self.image: str = options_data.get('image', '')
        self.image_big: str = options_data.get('image_big', '')
        self.name_i18n: str = options_data.get('name_i18n', '')

        nation_images_temp: dict = self._options.get('nation_images')
        nation_images_class = None
        if isinstance(nation_images_temp, dict):
            for key in nation_images_temp:
                if str(key).isnumeric():
                    nation_images_class = {key: NationImagesClass(data) for key, data in nation_images_temp.items()}
                    break
                if key == 'x180' or key == 'x71' or key == 'x85':
                    nation_images_class = NationImagesClass(nation_images_temp)
                    break
        elif isinstance(nation_images_temp, list):
            nation_images_class = [NationImagesClass(data) for data in nation_images_temp]
        if not nation_images_class:
            nation_images_class: NationImagesClass = NationImagesClass(nation_images_temp)
        self.nation_images: NationImagesClass | list[NationImagesClass] | dict[str, NationImagesClass] = nation_images_class
        del nation_images_temp, nation_images_class


class EncyclopediaAchievementsClass:
    def __init__(self, encyclopedia_achievements_data: dict):
        if not encyclopedia_achievements_data: encyclopedia_achievements_data = {}
        self._encyclopedia_achievements: dict = encyclopedia_achievements_data
        self.condition: str = encyclopedia_achievements_data.get('condition', '')
        self.description: str = encyclopedia_achievements_data.get('description', '')
        self.hero_info: str = encyclopedia_achievements_data.get('hero_info', '')
        self.image: str = encyclopedia_achievements_data.get('image', '')
        self.image_big: str = encyclopedia_achievements_data.get('image_big', '')
        self.name: str = encyclopedia_achievements_data.get('name', '')
        self.name_i18n: str = encyclopedia_achievements_data.get('name_i18n', '')
        self.order: int = encyclopedia_achievements_data.get('order', 0)
        self.outdated: bool = encyclopedia_achievements_data.get('outdated', False)
        self.section: str = encyclopedia_achievements_data.get('section', '')
        self.section_order: int = encyclopedia_achievements_data.get('section_order', 0)
        self.type: str = encyclopedia_achievements_data.get('type', '')

        options_temp: dict = self._encyclopedia_achievements.get('options')
        options_class = None
        if isinstance(options_temp, dict):
            for key in options_temp:
                if str(key).isnumeric():
                    options_class = {key: OptionsClass(data) for key, data in options_temp.items()}
                    break
                if key == 'description' or key == 'image' or key == 'image_big' or key == 'name_i18n' or key == 'nation_images':
                    options_class = OptionsClass(options_temp)
                    break
        elif isinstance(options_temp, list):
            options_class = [OptionsClass(data) for data in options_temp]
        if not options_class:
            options_class: OptionsClass = OptionsClass(options_temp)
        self.options: OptionsClass | list[OptionsClass] | dict[str, OptionsClass] = options_class
        del options_temp, options_class


