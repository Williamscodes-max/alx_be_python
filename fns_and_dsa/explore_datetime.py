from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()  # save current date/time
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted}")


def calculate_future_date():
    days = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.now() + timedelta(days=days)
    formatted = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted}")


def main():
    display_current_datetime()
    calculate_future_date()


if __name__ == "__main__":
    main()
