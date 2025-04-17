class Pet:

    def __init__(self, name):

        self.name = name

        self.hunger = 5 #range for hunger

        self.energy = 5 #range for energy

        self.happiness = 5 #range for happiness

        self.trick = [] #list storing tricks


    def eat(self):

        '''feed the pet to reduce hunger and increase happiness'''

        self.hunger = max(0, self.hunger - 3)

        self.happiness = min(10, self.happiness + 1)

        return f"{self.name} has been fed and is happier now"

    
    def sleep(self):

        '''Pet sleeps to gain energy'''

        self.energy = min(10, self.energy + 5)

        return f"{self.name} has slept and is now energized"

    
    def play(self):

        '''play with the pet to increase happiness but consume energy and increase hunger'''

        if self.energy <2:

            return f"{self.name} is too tired to play right now"

        self.energy = max(0, self.energy - 2)

        self.happiness = min(10, self.happiness + 2)

        self.hunger = min(10, self.hunger + 1)

        return f"It was fun playing with {self.name}"
    

    def get_status(self):

        '''display the current status'''

        hunger_status = "full" if self.hunger <= 2 else "hungry" if self.hunger >= 8 else "ok"

        energy_status = "tired" if self.energy <= 2 else "energetic" if self.energy >= 8 else "ok"

        happiness_status = "sad" if self.happiness <= 2 else "happy" if self.happiness >= 8 else "ok"


        status = f"{self.name}'s status: \n"

        status += f"hunger:{self.hunger}/10 ({hunger_status}) \n"

        status += f"energy:{self.energy}/10 ({energy_status}) \n"

        status += f"happiness:{self.happiness}/10 ({happiness_status})"

        return status
    

    def train(self, trick):
        
        self.trick.append(trick)
    
        return f"{self.name} learned a new trick: {trick}!"
    
    
    def show_tricks(self):

        if self.trick:
            return f"{self.name}'s tricks: {','.join(self.trick)}"
        else:
            return f"{self.name} hasn't learned any tricks yet."
