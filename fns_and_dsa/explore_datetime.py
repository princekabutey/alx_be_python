#Import necessary components from the datetime module
from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time"""
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date(days):
    """Calculate a future date by adding days to the current date"""
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    return future_date.strftime('%Y-%m-%d')

def main():
    """Main function to demonstrate datetime operations"""
    display_current_datetime()
    
    # Prompt user to enter number of days
    days = int(input("Enter the number of days to add to the current date: "))
    
    # Calculate and print future date
    future_date = calculate_future_date(days)
    print(f"Future date: {future_date}")

if __name__ == "__main__":
    main()