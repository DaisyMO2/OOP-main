class car:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        
        
    def drive (self):
        return f"{self.name}"
    def get_info(self):
         return(f"the{self.name} of color {self.color} made in {self.year}")
     
    