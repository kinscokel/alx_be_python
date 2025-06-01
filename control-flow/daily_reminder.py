# daily_reminder.py

def main():
    # Prompt for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Match case to handle priority
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"
        case _:
            print("Invalid priority level entered. Please use high, medium, or low.")
            return

    # Add note if the task is time-bound
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"

    # Final output
    print("\nReminder:", reminder)


# Run the program
if __name__ == "__main__":
    main()