from model import Task

class TaskRepository:
    def __init__(self) -> None:
        self.tasks = []

    # CRUD operations
    # Create
    def create(self, task: Task) -> None:
        self.tasks.append(task)

    # Read
    def getByIndex(self, index: int) -> Task|None:
        if(self.isNumberAValidIndex(index)): 
            return self.tasks[index]
        return
    
    def getAllTasks(self) -> list[Task]:
        return self.tasks
    
    # Update
    def update(self, index: int, task: Task) -> None:
        if(self.isNumberAValidIndex(index)): 
            self.tasks[index] = task

    # Delete
    def delete(self, index: int) -> None:
        if(self.isNumberAValidIndex(index)): 
            del self.tasks[index]
    
    # Toggle completed
    def toggleCompleted(self, index: int) -> None:
        if(self.isNumberAValidIndex(index)): 
            task = self.getByIndex(index)
            if task.completed == True:
                task.completed = False
            else:
                task.completed = True
            self.tasks[index] = task

    # Repository utils
    def isNumberAValidIndex(self, index: int) -> bool:
        return index >= 0 and index < len(self.tasks)
    
    def saveToFile(self, filename: str) -> None:
        file = open(filename, "w")
        for task in self.getAllTasks():
            file.write(task.title + "\n")
            file.write(task.description + "\n")
            if(task.completed):
                file.write("1\n")
            file.write("0\n")

    def loadFromFile(self, filename: str) -> None:
        file = open(filename, "r")
        lines = file.readlines()
        for i in range(0, len(lines), 3):
                title = lines[i].strip()
                description = lines[i+1].strip()
                completed = bool(int(lines[i+2].strip()))
                self.create(Task(title, description, completed))