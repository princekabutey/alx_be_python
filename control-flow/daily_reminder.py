def get_task_details():
    """
    Gets task description, priority, and time sensitivity from user.
    """
    
    # Task description
    task = input("Enter your task: ")
    
    # Priority
    while True:
        priority = input("Priority (high/medium/low): ").lower()
        if priority in ["high", "medium", "low"]:
            break
        print("Invalid priority. Please enter high, medium, or low.")
    
    # Time-bound
    while True:
        time_bound = input("Is it time-bound? (yes/no): ").lower()
        if time_bound in ["yes", "no"]:
            break
        print("Invalid input. Please enter yes or no.")
    
    return task, priority, time_bound

def provide_reminder(task, priority, time_bound):
    """
    Provides customized reminder based on task priority and time sensitivity.
    """
    
    match priority:
        case "high":
            base_message = f"'{task}' is a high priority task"
        case "medium":
            base_message = f"'{task}' is a medium priority task"
        case "low":
            base_message = f"'{task}' is a low priority task"
    
    if time_bound == "yes":
        reminder = f"{base_message} that requires immediate attention today!"
    else:
        reminder = f"{base_message}. Consider completing it when you have free time."
    
    print("Reminder:", reminder)


