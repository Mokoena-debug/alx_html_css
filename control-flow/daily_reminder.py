# daily_reminder.py

# Prompt user for task details
task = input("Enter your task:")  # Exact prompt formatting for ALX
priority = input("Priority (high/medium/low):").strip().lower()
time_bound = input("Is it time-bound? (yes/no):").strip().lower()

# Process task based on priority
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"Note: '{task}' has an unspecified priority"

# Modify message if task is time-bound
if time_bound == "yes" and priority in ["high", "medium"]:
    message += " that requires immediate attention today!"
elif time_bound == "no" and priority in ["high", "medium"]:
    message += ". Consider scheduling it soon."
elif time_bound == "yes" and priority == "low":
    message += " that you may want to complete soon."
else:
    message += ". Consider completing it when you have free time."

# Print the customized reminder
print(message)
