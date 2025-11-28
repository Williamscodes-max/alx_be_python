# Ask the user for their current age
current_age = int(input("How old are you? "))

# Calculate their age in 2050
future_age = current_age + 27

# Print the result
print(f"In 2050, you will be {future_age} years old.")



day = input("Enter a day of the week (Monday-Sunday): ").lower()

match day:
    case "monday":
        print("Ugh, Mondays...")
    case "tuesday":
        print("Just another workday...")
    case "wednesday":
        print("Hump day!")
    case "thursday":
        print("Almost there...")
    case "friday":
        print("TGIF!")
    case "saturday" | "sunday":  # Match multiple values with pipe (|)
        print("Weekend vibes!")
    case _:
        print("Invalid day entered.")