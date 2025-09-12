class TransportService:
    def _init_(self, name, vehicle_type, route):
        self.name = name
        self.vehicle_type = vehicle_type
        self.route = route

transport1 = TransportService("Link Bus", "Bus", "Fort Portal - Kampala")
transport2 = TransportService("Y.Y Coaches", "Bus", "Fort Portal - Kampala")
transport3 = TransportService("Private Hire Taxi", "Car", "Fort Portal Town")
transport4 = TransportService("Boda Boda", "Motorbike", "All over town")
transport5 = TransportService("Self Drive Rentals", "Car", "Tourist Services")