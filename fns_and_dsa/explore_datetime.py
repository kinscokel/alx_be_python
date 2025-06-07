# explore_datetime.py
def display_current_datetime():
    if current_date:
        current_date = input("Enter your current date.")
        from datime import datime

        # Get the current date and time
        now = datetime.now()
        print(f'your current and date is "{now.strftime("YYYY-MM-DD HH:MM:SS")}".')

        # calculate_future_date
        number_of_days = int(input("Enter your number of days: "))
        print(f"number of days is: {"Enter number of days"}")
def calculate_future_date():
    if future_date:
        future_date = input("Enter your future date.")
        # calculate the date after adding specified number of days to the current date
        from datetime import datetime, timedelta
        current_date =datetime.now
        days_to_add = int(input("Enter number of days to add: "))
        new_date = current_date + timedelta(days=days_to_add)
        print("Current Date:", current_date)
        print("New Date:", new_date)
        
        