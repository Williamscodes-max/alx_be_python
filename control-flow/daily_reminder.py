# daily_reminder.py

# Prompt for user inputs
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
        reminder = f"'{task}' has an unknown priority level"

# If statement for time sensitivity
if time_bound == "yes":
    print(f"Reminder: {reminder} that requires immediate attention today!")
else:
    print(f"Note: {reminder}. Consider completing it when you have free time.")


def my_func(name):
    "you are welcmome"
print(f"hello, {Alayode}")


def calculate_area(length, width):
    """Calculates the area of a rectangle."""
    area = length * width
    return area


# Passing argument
calculate_area(10, 5)  # rectangle_area will be 50





# Function definition with default value
def greet(name="World"):
     """Prints a greeting message."""
     print(f"Hello, {name}!")
greet()  # Output: Hello, World!
greet("Alice")  # Output: Hello, Alice! 

def greet(name= "Tinubu"):
    print(f"Hello", {name})


    
def square(number):
 """Returns the square of a number."""
 return number * number
squared_value = square(4)  # squared_value will be 16



count = 0  # Global variable
def increment():
     count += 1  # This refers to the local count within the function
     increment()
print(count)  # Output: 0 (Global count remains unchanged)


# def my_func(name= 'Alayode'):
#     "Welcome to our website"
# print(f"Hello, {name}")

def user_name(name):
    message = f"Hello, welcome {name}"
    print(message)



def calculate_area(length, width):
    """Calculates the area of a rectangle."""
    area = length * width
    return area