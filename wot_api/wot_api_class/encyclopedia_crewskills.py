class ImageUrlClass:
    def __init__(self, image_url_data: dict):
        if not image_url_data: image_url_data = {}
        self._image_url: dict = image_url_data
        self.big_icon: str = image_url_data.get('big_icon', '')
        self.small_icon: str = image_url_data.get('small_icon', '')

class EncyclopediaCrewskillsClass:
    def __init__(self, encyclopedia_crewskills_data: dict):
        if not encyclopedia_crewskills_data: encyclopedia_crewskills_data = {}
        self._encyclopedia_crewskills: dict = encyclopedia_crewskills_data
        self.description: str = encyclopedia_crewskills_data.get('description', '')
        self.is_perk: bool = encyclopedia_crewskills_data.get('is_perk', False)
        self.name: str = encyclopedia_crewskills_data.get('name', '')
        self.skill: str = encyclopedia_crewskills_data.get('skill', '')

        image_url_temp: dict = self._encyclopedia_crewskills.get('image_url')
        image_url_class = None
        if isinstance(image_url_temp, dict):
            for key in image_url_temp:
                if str(key).isnumeric():
                    image_url_class = {key: ImageUrlClass(data) for key, data in image_url_temp.items()}
                    break
                if key == 'big_icon' or key == 'small_icon':
                    image_url_class = ImageUrlClass(image_url_temp)
                    break
        elif isinstance(image_url_temp, list):
            image_url_class = [ImageUrlClass(data) for data in image_url_temp]
        if not image_url_class:
            image_url_class: ImageUrlClass = ImageUrlClass(image_url_temp)
        self.image_url: ImageUrlClass | list[ImageUrlClass] | dict[str, ImageUrlClass] = image_url_class
        del image_url_temp, image_url_class


