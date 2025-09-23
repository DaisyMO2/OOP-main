class resident:
    def __init__(self, name, room_no):
        self.name = name
        self.room_no = room_no

class visitor:
    def __init__(self, name, national_id):
        self. name = name
        self.national_id = national_id 
        
class hostel:
    def __init__(self, name):
        self.name = name
        self.visits = []
        
    def record_visit(self, visitor: visitor, resident:resident):
        entry = visitor.name, + "is visiting" + resident.name + "in room" + resident.room_no
        self.visits.append(entry)
        
    def show_visits(self):
        print(f"visit log for {}")
        
    