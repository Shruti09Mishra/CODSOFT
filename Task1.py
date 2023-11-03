# Define an empty list to store tasks
tasks = []

# Function to add a task to the to-do list
def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully!")

# Function to update a task in the to-do list
def update_task():
    print("Current tasks:")
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task}")
    
    try:
        task_index = int(input("Enter the task number you want to update: ")) - 1
        if 0 <= task_index < len(tasks):
            new_task = input("Enter the new task: ")
            tasks[task_index] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

# Function to display the to-do list
def display_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")

# Function to show the menu and handle user input
def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Display Tasks")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            update_task()
        elif choice == "3":
            display_tasks()
        elif choice == "4":
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
