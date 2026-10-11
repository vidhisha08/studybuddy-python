# assignment_manager.py
from assignment import Assignment
from datetime import date

    
class AssignmentManager:
    def __init__(self):
        self._assignments = []

    def add(self, assignment):
        self._assignments.append(assignment)

    def list_all(self):
        if len(self._assignments) == 0:
            print("No assignments yet!!")
            return
        
        for i, assignment in enumerate(self._assignments, start=1):
            print(f"{i}. {assignment}")

    def complete(self, index):
        self._assignments[index - 1].mark_complete()

    def sort_by_due_date(self):
        self._assignments.sort(key=lambda a: a.due_date)

