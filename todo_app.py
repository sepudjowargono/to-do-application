def show_welcome():
    print("\n======================== ") 
    print("Welcome to the To-Do App!")
    print("======================== ")

def show_menu(): # Displays the main menu options
    print("\nMAIN MENU:")
    print("1) Add A Task")
    print("2) View Tasks")
    print("3) Delete A Task")
    print("4) Quit Application\n")

def add_task(tasks):
    task = input("\nEnter a task to add: ").strip() #Removes spaces from beginning to end and prevents users from entering spaces only. 
    
    if not task:
        print("\n⚠️ Task is empty. No new task has been added. Please try again.")
        return
  
    tasks.append(task)
    print(f"\n✅ The following task has been successfully added: {task}")
        
def view_tasks(tasks):
    
    if not tasks:
        print("\n📋 Your list is empty. There are no tasks to complete!")
        return
    
    print("\nYOUR TASKS:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
        
def delete_task(tasks): #Deletes a task by its {i} number. 
    if not tasks:
        print("\n📋 No tasks to delete. Your list is currently empty.")
        return
    
    view_tasks(tasks)
    
    try:
        choice = input("\nEnter the task number to delete: ").strip()
        task_num = int(choice)
        
        if task_num < 1 or task_num > len(tasks):
            print("\n⚠️ That task number doesn't exist. Please choose a valid task number.")
            return
        
    except ValueError:
        print("\n❗ Invalid input. Please choose a valid task number.")
        return
        
    else:
        removed = tasks.pop(task_num -1)
        print(f"\n🗑️ The follow task has been deleted: {removed}")
        
    finally:
        print("\n🔁 Returning to the main menu...")
        
def get_menu_choice():
    try:
        choice = int(input("Choose an option (1-4): ").strip())
        if choice not in (1, 2, 3, 4):
            raise ValueError()
        
    except ValueError:
        print("\n❗Invalid choice. Please enter 1, 2, 3, or 4.")
        return None
    
    else:
        return choice
    
def main(): #Main program loop that runs the app
    tasks = []
        
    show_welcome()
    
    while True:
        show_menu()
        choice = get_menu_choice()
        
        if choice is None:
            continue
        
        elif choice == 1:
            add_task(tasks)
            
        elif choice == 2:
            view_tasks(tasks)
            
        elif choice == 3:
            delete_task(tasks)
            
        elif choice == 4:
            print("\n👋 Goodbye! Thanks for using the To-Do App!\n")
            break

# Prevents the app from auto-starting if imported
if __name__ == "__main__":
    main()
        
    
         
        
        
        
    





        

    
    