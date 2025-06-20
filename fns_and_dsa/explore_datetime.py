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
        from datetime import datetime, timedelta
def calculate_future_date():
    if future_date:
        days = int(input("Enter the number of days to add to the current date: "))
        future_date = datetime.now() + timedelta(days=days)
        print("Future date:", future_date.strftime("%Y-%m-%d"))
        # calculate the date after adding specified number of days to the current date
        from datetime import datetime, timedelta
        current_date =datetime.now
        current_time = datetime.now().strtime("%Y-%m-%d %H:%M:%S")
        print(current_time)
        days_to_add = int(input("Enter number of days to add: "))
        new_date = current_date + timedelta(days=days_to_add)
        print("Current Date:", current_dat
        