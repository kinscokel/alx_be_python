# daily_reminder.py

def main():
    print("Welcome to your Daily Reminder!\n")

    # Prompt for task information
    task = input("Please enter your task: ")
    priority = input("What is the priority? (high, medium, low): ").lower()
    time_bound = input("Is this task time-sensitive? (yes or no): ").lower()

    # Process priority using match-case (Python 3.10+)
    match priority:
        case "high":
            reminder = f"🔴 HIGH PRIORITY: Don't delay! Complete the task: {task}."
        case "medium":
            reminder = f"🟠 Medium priority: Make sure to get to this task: {task}."
        case "low":
            reminder = f"🟢 Low priority: You can do this task later: {task}."
        case _:
            reminder = f"⚪ Unknown priority level. Here's your task: {task}."

    # Modify reminder based on time sensitivity
    if time_bound == "yes":
        reminder += " ⏰ This task is time-sensitive, act quickly!"

    # Display final customized reminder
    print("\nYour Daily Reminder:")
    print(reminder)

if __name__ == "__main__":
    main()