# assignment.py
from datetime import date

class Assignment:
    def __init__(self, title: str, due_date: date):
        self._title = title
        self._due_date = due_date
        self._completed = False
        
    @property
    def title(self):
        return self._title
    
    @property
    def due_date(self):
        return self._due_date

    @property
    def completed(self):
        return self._completed

    def mark_complete(self):
        self._completed = True

    def __str__(self):
        tick = "[x]" if self._completed else "[ ]"
        return f"{tick} {self._title} - {self._due_date.isoformat()}"
        
