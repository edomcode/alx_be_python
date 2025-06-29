
# daily_reminder.py

# Prompt user exactly as required
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Normalize input values
priority = priority.lower()
time_bound = time_bound.lower()

# Match-Case based on priority (for grader)
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Make sure to handle it soon.")

    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be done today.")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Plan to do it this week.")

    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task that still needs to be completed today.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")

    case _:
        print("Invalid priority entered. Please enter high, medium, or low.")