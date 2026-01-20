task = input("Enter your task for today: ")
priority = input("Enter the priority (high, medium, low): ")
time_bound = input("Is this task time-bound? (yes/no): ")

match priority.lower():
    case "high":
        reminder = f"High priority task: {task}"
    case "medium":
        reminder = f"Medium priority task: {task}"
    case "low":
        reminder = f"Low priority task: {task}"
    case _:
        reminder = f"Task: {task}"

if time_bound == "yes":
    reminder += " that requires immediate attention today!"

print(reminder)
