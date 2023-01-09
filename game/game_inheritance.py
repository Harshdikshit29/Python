from random import randint as ri
import pgzrun

WIDTH = 800
HEIGHT = 500

# all the class logic
class Player(Actor):
    # override the default constructor
    def __init__(self, image, speed=5):
        pos = ri(0,WIDTH), ri(0,HEIGHT) # generate a random x,y coordinate
        super().__init__(image,pos) # call the parent class constructor and pass image and pos
        self.speed = speed # add a new instance variable
    
    def move(self):
        if keyboard.W:
            self.y -= self.speed
        elif keyboard.S:
            self.y += self.speed
        elif keyboard.A:
            self.x -= self.speed
            self.angle = +10
        elif keyboard.D:
            self.x += self.speed 
            self.angle = -10  
        # elif keyboard.E:
        #     self.x += self.speed    (diaognal movement)
        #     self.y -= self.speed
        else:
            self.angle = 0
        
    def check_boundry(self):
        if self.x < 0:
            self.x = WIDTH
        if self.x > WIDTH:
            self.x = 0
        if self.y < 0:
            self.y = HEIGHT
        if self.y > HEIGHT:
            self.y = 0        

# main game code
p = Player('ironman')
  
def draw():
    screen.fill('black')
    screen.blit('bg', (0,0)) # add background image
    p.draw()
    
def update():
    p.move()
    p.check_boundry()

pgzrun.go()