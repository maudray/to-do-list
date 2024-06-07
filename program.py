task = []
#menu function
def display_menu():
    print("1.Enter 1 to add task")
    print("2.Enter 2 to view task")
    print("3.Enter 3 to update task")
    print("4.Enter 4 t+o delete")
    print("5.Enter 5 to exit")
    

#add task function
def add_task():
    user_task = input("Enter your task")
    task.append(user_task)
    print("Task added successfully")

#view task fuction
def view_task():
    # if len(task) > 0:
    #     print(task)
    # else:
    #     print("No task to view")
      if not tasks:
           print("todo list is empty")
      else:
        #    print(task)
           for i, task in enumerate(task,1):
                print(f"{i}.{task}")
def update_task(): 
        print("these are your available task") 
        view_task()
        task_number = int(input("Enter task number you want to update\n")) 
        if 1 <= task_number <= len(tasks):
              updated_task = input("Enter update") 
              tasks[task_number -1]=update_task

def  delete_task():
        view_task()
        delete_task
   
    #exits 
def exit():
       exit()
    

