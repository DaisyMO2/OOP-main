class Gadget:
    def start(self):
        print("Gadget has started")
        
        
class Phone(Gadget):
    def start(self):
        print("Phone is starting")
        
class Laptop(Gadget):
    def start(self):
        print("Laptop is starting")
        
 
gadgets = [Phone(), Laptop()]
  
for gadget in gadgets:
    gadget.start()  
    
    
class Camera:
    def __init__(self):
        print("taking photo")   
        
class Wifi_enabled:
    def __init__(self):
        print("connect to wifi")
        
class Phone(Gadget, Camera, Wifi_enabled):
    def __init__(self):
        print("phone is ready")
   
class Phone(gadget, Wifi_enabled):
    def __init__(self):
        print("phone is ready")
        
devices = [Phone(), Phone()]

for device in devices:
    device.__init__()
    if isinstance(device, Camera):
        print("This device has a camera.")
    if isinstance(device, Wifi_enabled):
        print("This device has WiFi capability.")    
    
