class Task:
    def __init__(self, title:str, description: str, completed: bool) -> None:
        self.title = title
        self.description = description
        self.completed = completed