class Square:

    def __init__(self, color):
        self.color = color
        self.occupied = False
        self.man = "  "

    def set_occupied(self, occupied):
        self.occupied = occupied

    def get_occupied(self):
        return self.occupied
    
    def set_man(self, man):
        self.man = man

    def get_man(self):
        return self.man
