# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority and time sensitivity
if time_bound == "yes":
    urgency = "that requires immediate attention today!"
else:
    urgency = "Consider completing it when you have free time."

match priority:
    case "high":
        print(f"Reminder: '{task}' is a high priority task {urgency}")
    case "medium":
        print(f"Reminder: '{task}' is a medium priority task {urgency}")
    case "low":
        print(f"Reminder: '{task}' is a low priority task {urgency}")
    case _:
        print(f"Reminder: '{task}' has an unknown priority level {urgency}")

