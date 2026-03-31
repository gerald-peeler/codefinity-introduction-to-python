# list of products on prromotion for each weekday
daily_promotions = ["Milk", "Eggs", "Bread", "Apples", "Oranges"]

# List of weekdays corresponding to each task
weekdays = [
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"
]

# Loop through each day using the range function
for day in range(len(daily_promotions)):
    task = daily_promotions[day]  # Access the task corresponding to the current day
    weekday = weekdays[day]   # Access the corresponding weekday
    
    print(f"{weekday}: Promotion on {task}")