# daily_reminder.py

# Prompt user for task details (exact prompts)
task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

# Use match-case to decide message
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Reminder: '{task}' is a low priority task"
    case _:
        message = f"Reminder: '{task}' has an unspecified priority"

# Append time-bound info in the same f-string format
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message += ". Consider completing it when you have free time."

# Print the final message exactly using a single f-string
print(f"{message}")
