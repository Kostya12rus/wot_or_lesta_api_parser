class ImagesClass:
    def __init__(self, images_data: dict):
        if not images_data: images_data = {}
        self._images: dict = images_data
        self.large: str = images_data.get('large', '')
        self.small: str = images_data.get('small', '')

class EncyclopediaBoostersClass:
    def __init__(self, encyclopedia_boosters_data: dict):
        if not encyclopedia_boosters_data: encyclopedia_boosters_data = {}
        self._encyclopedia_boosters: dict = encyclopedia_boosters_data
        self.booster_id: int = encyclopedia_boosters_data.get('booster_id', 0)
        self.description: str = encyclopedia_boosters_data.get('description', '')
        self.expires_at: int = encyclopedia_boosters_data.get('expires_at', 0)
        self.is_auto: bool = encyclopedia_boosters_data.get('is_auto', False)
        self.lifetime: int = encyclopedia_boosters_data.get('lifetime', 0)
        self.name: str = encyclopedia_boosters_data.get('name', '')
        self.price_credit: int = encyclopedia_boosters_data.get('price_credit', 0)
        self.price_gold: int = encyclopedia_boosters_data.get('price_gold', 0)
        self.resource: str = encyclopedia_boosters_data.get('resource', '')

        images_temp: dict = self._encyclopedia_boosters.get('images')
        images_class = None
        if isinstance(images_temp, dict):
            for key in images_temp:
                if str(key).isnumeric():
                    images_class = {key: ImagesClass(data) for key, data in images_temp.items()}
                    break
                if key == 'large' or key == 'small':
                    images_class = ImagesClass(images_temp)
                    break
        elif isinstance(images_temp, list):
            images_class = [ImagesClass(data) for data in images_temp]
        if not images_class:
            images_class: ImagesClass = ImagesClass(images_temp)
        self.images: ImagesClass | list[ImagesClass] | dict[str, ImagesClass] = images_class
        del images_temp, images_class


