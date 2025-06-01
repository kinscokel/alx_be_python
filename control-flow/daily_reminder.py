# daily_reminder.py

def main():
    # Prompt for task details
    task_description = input("Enter your description: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Determine reminder message based on priority and time sensitivity
    match priority:
        case "high":
            reminder = f"'{task_description}' is a high priority task"
        case "medium":
            reminder = f"'{task_description}' is a medium priority task"
        case "low":
            reminder = f"'{task_description}' is a low priority task"
        case _:
            reminder = f"'{task_description}' has an unknown priority"

    # Add urgency if time-bound
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"

    # Print the final reminder
    print("\nReminder:", reminder)

if __name__ == "__main__":
    main()