class EncyclopediaProvisionsClass:
    def __init__(self, encyclopedia_provisions_data: dict):
        if not encyclopedia_provisions_data: encyclopedia_provisions_data = {}
        self._encyclopedia_provisions: dict = encyclopedia_provisions_data
        self.description: str = encyclopedia_provisions_data.get('description', '')
        self.image: str = encyclopedia_provisions_data.get('image', '')
        self.name: str = encyclopedia_provisions_data.get('name', '')
        self.price_credit: int = encyclopedia_provisions_data.get('price_credit', 0)
        self.price_gold: int = encyclopedia_provisions_data.get('price_gold', 0)
        self.provision_id: int = encyclopedia_provisions_data.get('provision_id', 0)
        self.tag: str = encyclopedia_provisions_data.get('tag', '')
        self.type: str = encyclopedia_provisions_data.get('type', '')
        self.weight: int = encyclopedia_provisions_data.get('weight', 0)

