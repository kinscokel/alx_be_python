def get_task_details():
    task = input("Enter your task: ")
    priority = input("Enter task priority (high, medium, low): ").lower()
    while priority not in ["high", "medium", "low"]:
        priority = input("Invalid priority. Please enter high, medium, or low: ").lower()

    time_bound = input("Is the task time-bound? (yes/no): ").lower()
    while time_bound not in ["yes", "no"]:
        time_bound = input("Invalid input. Please enter yes or no: ").lower()

    return task, priority, time_bound


def provide_reminder(task, priority, time_bound):
    match priority:
        case "high":
            reminder = f"High priority task: {task}"
            if time_bound == "yes":
                reminder += " that requires immediate attention today!"
            else:
                reminder += " that needs to be completed as soon as possible."
        case "medium":
            reminder = f"Medium priority task: {task}"
            if time_bound == "yes":
                reminder += " that should be addressed today."
            else:
                reminder += " that should be completed within a reasonable timeframe."
        case "low":
            reminder = f"Low priority task: {task}"
            if time_bound == "yes":
                reminder += " that needs attention today, but has some flexibility."
            else:
                reminder += " that can be completed at your convenience."

    print("Reminder:", reminder)


def main():
    task, priority, time_bound = get_task_details()
    provide_reminder(task, priority, time_bound)


if __name__ == "__main__":
    main()