# main.py
from assignment_manager import AssignmentManager
from assignment import Assignment
from datetime import date

manager = AssignmentManager()

while True:
    print("########--STUDYBUDDY--######## \n")
    print("1. Add")
    print("2. List")
    print("3. Complete")
    print("4. Sort")
    print("5. Quit")
    print("########--------------######## \n")
    ch = input("Choose: ")

    if ch == "1":
        name = input("Enter title: ")
        try:
            due = input("Enter due date (YYYY-MM-DD): ")
            manager.add(Assignment(name, date.fromisoformat(due)))
        except ValueError:
            print("Please enter in the correct format.")

    elif ch == "2":
        manager.list_all()

    elif ch == "3":
        try:
            num = int(input("Which assignment?: "))
            if (num >= 1):  
                manager.complete(num)
            else:
                print("Invalid number")
        except(ValueError, IndexError):
            print("Invalid Number.")


    elif ch == "4":
        manager.sort_by_due_date()
        manager.list_all()

    elif ch == "5":
        break

    else:
        print("INVALID CHOICE")
        
