from repository import TaskRepository
from view import MenuView

# Init

repo = TaskRepository()

view = MenuView()
view.menu(repo)