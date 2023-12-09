from repository import TaskRepository
from model import Task
import os

class TaskView:
    def create(self, taskRepository: TaskRepository):
        os.system("cls")
        task_title = ""
        task_description = ""
        task_completed = False
        
        task_title = input("Task title: ")
        task_description = input("Task description: ")

        taskRepository.create(Task(task_title, task_description, task_completed))


    def displayAllTasks(self, taskRepository: TaskRepository):
        os.system("cls")
        tasks = taskRepository.getAllTasks()
        index = 0
        print("===")
        for task in tasks:
            print(f"{index}. \"{task.title} - {task.completed}\"\n\n\n{task.description}\n\n")
            index += 1
        print("===")
        input()

    def displayTask(self, taskRepository: TaskRepository):
        os.system("cls")
        index = int(input("Task index: "))
        if(taskRepository.isNumberAValidIndex(index)):
            task = taskRepository.getByIndex(index)

            if type(task) is Task:
                print("===")
                print(f"{index}. \"{task.title} - {task.completed}\"\n\n\n{task.description}\n\n")
                print("===")
                input()
            else:
                print("Cannot read task details")
                input()
        
    def updateTask(self, taskRepository: TaskRepository):
        os.system("cls")
        index = int(input("Task index: "))

        if(taskRepository.isNumberAValidIndex(index)):
            task: Task = taskRepository.getByIndex(index)
            task.title = input("Task title: ")
            task.description = input("Task description: ")
            taskRepository.update(index, task)

    def deleteTask(self, taskRepository: TaskRepository):
        os.system("cls")
        index = int(input("Task index: "))

        if(taskRepository.isNumberAValidIndex(index)):
            choice = input("Delete?(type 'no' to cancel): ")
            if(choice != "no"):
                taskRepository.delete(index)

    def toggleCompleted(self, taskRepository: TaskRepository):
        os.system("cls")
        index = int(input("Task index: "))

        if(taskRepository.isNumberAValidIndex(index)):
            taskRepository.toggleCompleted(index)

    def save(self, taskRepository: TaskRepository):
        filename = input("Filename: ")
        taskRepository.saveToFile(filename)

    def load(self, taskRepository: TaskRepository):
        filename = input("Filename: ")
        taskRepository.loadFromFile(filename)


class MenuView:

    def menu(self, taskRepository: TaskRepository):
        taskView = TaskView()
        while True:
            os.system("cls")
            print("\t1. List of tasks")
            print("\t2. Create a new task")
            print("\t3. Show task by index")
            print("\t4. Edit task by index")
            print("\t5. Delete task by index")
            print("\t6. Toggle completed")
            print("\t7. Save to file")
            print("\t8. Load from file")

            choice = int(input("\t>>"))


            if choice == 1:
                taskView.displayAllTasks(taskRepository)
            elif choice == 2:
                taskView.create(taskRepository)
            elif choice == 3:
                taskView.displayTask(taskRepository)
            elif choice == 4:
                taskView.updateTask(taskRepository)
            elif choice == 5:
                taskView.deleteTask(taskRepository)
            elif choice == 6:
                taskView.toggleCompleted(taskRepository)
            elif choice == 7:
                taskView.save(taskRepository)
            elif choice == 8:
                taskView.load(taskRepository)
            

