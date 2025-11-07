print("Welcome to your Study Planner!")
print("You will enter study tasks, then plan how many to do today.\n")

tasks = []

print("Enter your study tasks (one per line).")
print("Press ENTER with nothing typed to stop.\n")

while True:
    task = input("Task: ")
    
    if task == "":
        break
    
    if task in tasks:
        print("You already have this task")
        continue
    
    tasks.append(task)
    
print(f"You have {len(tasks)} tasks")

for i, task in enumerate(tasks, 1):
    print(f" {i}. {task}")
    
if tasks == "":
    print("You have no tasks today")
    exit()
    
while True:
    answer = input(f"How many tasks will you do today (1 - {len(tasks)}) ")
    if answer.isdigit():
        num = int(answer)
        if 1 <= num <= len(tasks):
            break
        else:
            print("You don't have that many tasks")
    else:
        print("Please enter valid number")

today_tasks = tasks[:num]

for i, task in enumerate(today_tasks, 1):
    print(f"  {i}. {task}")

total_minutes = 0
print("\nNow estimate time for each task:")

for task in today_tasks:
    while True:
        mins_str = input(f"Minutes for {task} ")
        
        if mins_str.isdigit():
            mins = int(mins_str)
            if mins >= 0:
                total_minutes += mins
                break
            else:
                print("  → No negative numbers!")
        else:
            print("  → Enter a number!")
            
if num > 0:
    average = total_minutes / num
else:
    average = 0
    
print(f"\n=== STUDY PLAN SUMMARY ===")
print(f"Total study time: {total_minutes} minutes")
print(f"Average per task: {average:.1f} minutes")

if total_minutes < 60:
    level = "light"
elif total_minutes < 150:
    level = "moderate"
else:
    level = "intensive"

print(f"Your plan is {level}.")