import json
from datetime import datetime
import os

# File to save tasks
file_name = "tasks.json"

# Load existing tasks if file exists
if os.path.exists(file_name):
    with open(file_name, 'r') as file:
        tasks = json.load(file)
else:
    tasks = []

# Show menu to user
while True:
    print("\n--- Daily Task Logger ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        task = input("Enter your task: ")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        tasks.append({"task": task, "time": timestamp})
        with open(file_name, 'w') as file:
            json.dump(tasks, file, indent=4)
        print("✅ Task added successfully!")

    elif choice == "2":
        print("\n--- Your Tasks ---")
        for entry in tasks:
            print(f"[{entry['time']}] - {entry['task']}")

    elif choice == "3":
        print("👋 Exiting the Task Logger. Bye!")
        break

    else:
        print("❌ Invalid choice. Please enter 1, 2, or 3.")
