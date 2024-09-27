def get_task_details():
    """
    Gets task description, priority, and time sensitivity from user.
    """
    task = input("Enter task description: ")
    priority = input("Enter task priority (high,medium,low): ").lower()
    time_bound = input("Is task time-bound?(yes or no): ").lower()
    
    return task, priority, time_bound

def provide_reminder(task, priority, time_bound):
    """
    Provides customized reminder based on task priority and time sensitivity.
    """
    match priority:
        case "high":
            base_message = f"High-priority task: {task}"
        case "medium":
            base_message = f"Medium-priority task: {task}"
        case "low":
            base_message = f"Low-priority task: {task}"
        case _:
            base_message = f"Task: {task}"
    
    if time_bound == "yes":
        reminder = f"{base_message} that requires immediate attention today!"
    else:
        reminder = f"{base_message}. Consider tackling it today."
    
    print(reminder)
def main():
    task, priority, time_bound = get_task_details()
    provide_reminder(task, priority, time_bound)

