class ImagesClass:
    def __init__(self, images_data: dict):
        if not images_data: images_data = {}
        self._images: dict = images_data
        self.big_icon: str = images_data.get('big_icon', '')
        self.medium_icon: str = images_data.get('medium_icon', '')
        self.small_icon: str = images_data.get('small_icon', '')

class EncyclopediaBadgesClass:
    def __init__(self, encyclopedia_badges_data: dict):
        if not encyclopedia_badges_data: encyclopedia_badges_data = {}
        self._encyclopedia_badges: dict = encyclopedia_badges_data
        self.badge_id: int = encyclopedia_badges_data.get('badge_id', 0)
        self.description: str = encyclopedia_badges_data.get('description', '')
        self.name: str = encyclopedia_badges_data.get('name', '')

        images_temp: dict = self._encyclopedia_badges.get('images')
        images_class = None
        if isinstance(images_temp, dict):
            for key in images_temp:
                if str(key).isnumeric():
                    images_class = {key: ImagesClass(data) for key, data in images_temp.items()}
                    break
                if key == 'big_icon' or key == 'medium_icon' or key == 'small_icon':
                    images_class = ImagesClass(images_temp)
                    break
        elif isinstance(images_temp, list):
            images_class = [ImagesClass(data) for data in images_temp]
        if not images_class:
            images_class: ImagesClass = ImagesClass(images_temp)
        self.images: ImagesClass | list[ImagesClass] | dict[str, ImagesClass] = images_class
        del images_temp, images_class


