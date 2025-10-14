class phone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
        
    def call(self, number):
        print(f'calling{number} from {self.brand}')
    def take_photo(self, photo):
        print(f'taking{photo}')
    def play_music(self, song):
        print(f'playing{song}')
  
phone = phone('iphone', '16 pro', '256GB')
phone.call('772469947')
phone.take_photo('selfie')
phone.play_music('faithfull')
      
    
    
        
        
        