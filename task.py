todo_list = []

def add_task(task):
  todo_list.append(task)
  print(f"Task '{task}' added to the list.")

def view_tasks():
  if not todo_list:
    print("Your to-do list is empty.")
  else:
    print("To-do list:")
    for index, task in enumerate(todo_list, start=1):
      print(f"{index}. {task}")

def complete_task(task_index):
  if 1 <= task_index <= len(todo_list):
    completed_task = todo_list.pop(task_index - 1)
    print(f"Task '{completed_task}' marked as complete.")
  else:
    print("Invalid task index.")

def main():
  while True:
    print("\nTo-do List App")
    print("1. Add task")
    print("2. View tasks")
    print("3. Complete task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
      task = input("Enter task: ")
      add_task(task)
    elif choice == "2":
      view_tasks()
    elif choice == "3":
      task_index = int(input("Enter task index to complete: "))
      complete_task(task_index)
    elif choice == "4":
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()