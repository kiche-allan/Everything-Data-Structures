# You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

# A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

# The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

# Implement the MyCalendar class:
 
# MyCalendar() Initializes the calendar object.
# boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

class MyCalendar:
    def __init__(self):
        self.events = []

    def book(self, start, end):
        for event in self.events:
            if max(event[0], start) < min(event[1], end):
                # Check for intersection between existing events and the new event
                return False
        self.events.append((start, end))
        # Add the new event to the list of events
        return True


# solution 2

# class MyCalendar:
#     def __init__(self):
#         self.calendar = []
#     def book(self, start:int, end:int) -> bool:
#         l = 0
#         r = len(self.calendar)
        
#         while l < r:
#             mid = ( l + r )//2
#             if self.calendar[mid][0] <= start:
#                 l = mid+ 1
#             else:
#                 r = mid
            
#         if self.intersect(l, start, end):
#             return False
#         else:
#             self.calendar.insert(l, [start, end])
#         return True
#     def intersect(self, index, start, end):
#         return (
#             (self.calendar[index-1][1] > start if index >= 1 else False) or
#             (self.calendar[index][0] > end if l < len(self.calendar) else False)
#         )