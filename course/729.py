class MyCalendar:
    def __init__(self):
        self.plan = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.plan:
            if s < end and start < e:
                return False
        self.plan.append((start, end))
        return True
