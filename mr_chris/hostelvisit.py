# Class for Visitor
class Visitor:
    def __init__(self, name, visitor_id):
        self.name = name
        self.visitor_id = visitor_id


# Class for Resident
class Resident:
    def __init__(self, name, room):
        self.name = name
        self.room = room


# Class for Hostel
class Hostel:
    def __init__(self, name):
        self.name = name
        self.visits = []

    def record_visit(self, visitor, resident):
        self.visits.append((visitor, resident))

    def show_visits(self):
        print(f"Visit records for {self.name}:")
        if not self.visits:
            print("No visits recorded yet.")
        else:
            for v, r in self.visits:
                print(
                    f"{v.name} (ID: {v.visitor_id}) visited {r.name} in room {r.room}"
                )


visitor1 = Visitor("Komoire Ashiraf ", "R016")
resident1 = Resident("Marunga Diasy", "R220")
hostel1 = Hostel("Sky courts Hostel")

visitor2 = Visitor("Tumusiime Marvin", "R004")
resident2 = Resident("Komoire Ashiraf", "R033")
hostel2 = Hostel("Hill View Hostel")

visitor3 = Visitor("Mukasa Mathew", "R019")
resident3 = Resident("Lukyamuzi Gabby Angel", "R202")
hostel3 = Hostel("David's Ark Hostel")

hostel1.record_visit(visitor1, resident1)
hostel1.show_visits()

hostel2.record_visit(visitor2, resident2)
hostel2.show_visits()

hostel3.record_visit(visitor3, resident3)
hostel3.show_visits()
