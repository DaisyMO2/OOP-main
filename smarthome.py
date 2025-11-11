class Device:
    def __init__(self, device_name, status, location):
        self.device_name = device_name
        self.status = status
        self.location = location

class SmartHomeController:
    total_devices = 0

    def __init__(self):
        self.devices = []

    def add_device(self, device_name, location):
        device = Device(device_name, "OFF", location)
        self.devices.append(device)
        SmartHomeController.total_devices += 1

    def turn_on_device(self, device_name):
        for d in self.devices:
            if d.device_name == device_name:
                d.status = "ON"
                print(f"{d.device_name} is ON")
                return
        print("Device not found")

    def turn_off_device(self, device_name):
        for d in self.devices:
            if d.device_name == device_name:
                d.status = "OFF"
                print(f"{d.device_name} is OFF")
                return
        print("Device not found")

    def display_all_devices(self):
        for d in self.devices:
            print(f"{d.device_name}, Status: {d.status}, Location: {d.location}")
        print(f"Total devices: {SmartHomeController.total_devices}")


# Demonstration
home = SmartHomeController()
home.add_device("Light", "Living Room")
home.add_device("Fan", "Bedroom")
home.add_device("TV", "Sitting Room")

home.turn_on_device("Light")
home.turn_off_device("Fan")

home.display_all_devices()
