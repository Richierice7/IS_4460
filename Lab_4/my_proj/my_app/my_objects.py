
class vehicle():
    def __init__(self):
        self.type = 'generic vehicle'

class car():
    def __init__(self,color,sound):
        self.color = color
        self.sound = sound
        self.wheels = 4

    def honk(self):
        return self.sound
    
    def wheels(self):
        return self.wheels
    
class motorcycle():
    def __init__(self,color,sound):
        self.color = color
        self.sound = sound
        self.wheels = 2

    def honk(self):
        return self.sound
    
    def wheels(self):
        return self.wheels