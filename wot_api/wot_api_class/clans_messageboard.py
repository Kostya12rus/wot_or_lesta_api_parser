class ClansMessageboardClass:
    def __init__(self, clans_messageboard_data: dict):
        if not clans_messageboard_data: clans_messageboard_data = {}
        self._clans_messageboard: dict = clans_messageboard_data
        self.author_id: int = clans_messageboard_data.get('author_id', 0)
        self.created_at: int = clans_messageboard_data.get('created_at', 0)
        self.editor_id: int = clans_messageboard_data.get('editor_id', 0)
        self.is_read: bool = clans_messageboard_data.get('is_read', False)
        self.message: str = clans_messageboard_data.get('message', '')
        self.updated_at: int = clans_messageboard_data.get('updated_at', 0)

