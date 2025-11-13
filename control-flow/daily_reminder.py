task = input("enter your task: ")
priority = input("enter task priority (high, medium, low): ").lower()
time_bound = input("is this task time-bound? (yes/no): ").lower()

match priority:
    case "high":
        message = f"'{task}' is a high priority task. Make sure to complete it as soon as possible!"
    case "medium":
        message = f"'{task}' is a medium priority task. Try to get to it when you can."
    case "low":
        message = f"'{task}' is a low priority task. You can do it whenever you have time."