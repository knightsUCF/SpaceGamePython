#!/usr/bin/env python



import random
import sound
import pygame


pygame.init()
































class Interface():



    # mouse

    def get_mouse_coordinates(self):
        return pygame.mouse.get_pos()


    def get_mouse_pressed_state(self):
        return pygame.mouse.get_pressed()



    # useful for triggering a sound only once per mouse move

    def get_user_input_before_tick(self):
        mouse_press = self.get_mouse_pressed_state()
        keyboard_press = 1
        return mouse_press, keyboard_press # can return multiple values for keyboard presses



    def get_user_input_after_tick(self):
        mouse_press = self.get_mouse_pressed_state()
        keyboard_press = 1
        return mouse_press, keyboard_press # can return multiple values for keyboard presses



    # all 

    def get_input(self):
        self.get_mouse_coordinates()
        self.get_mouse_pressed_state()



interface = Interface()




















class Controller():



    def update(self, previous_user_input, current_user_input):
        # 0 - mouse click, # 1 - keyboard press 
        if current_user_input[0] == (1, 0, 0) and previous_user_input[0] != (1, 0, 0):
            sound.play_sound('select_short.wav')



controller = Controller()






# http://thepythongamebook.com/en:pygame:step017 PERFECT!!!



class Fragment(pygame.sprite.Sprite):
    gravity = True # fragments fall down ?
    def __init__(self, position):
            pygame.sprite.Sprite.__init__(self, self.groups)
            self.position = [0.0,0.0]
            self.position[0] = position[0]
            self.position[1] = position[1]
            #...
            self.dx = random.randint(-self.fragmentmaxspeed,self.fragmentmaxspeed)
            self.dy = random.randint(-self.fragmentmaxspeed,self.fragmentmaxspeed)
 
    def update(self, seconds):
            #...
            self.position[0] += self.dx * seconds
            self.position[1] += self.dy * seconds
            if Fragment.gravity:
                self.dy += FORCE_OF_GRAVITY # gravity suck fragments down
            self.rect.centerx = round(self.position[0],0)
            self.rect.centery = round(self.position[1],0)





class HealthBar(pygame.sprite.Sprite):


        def __init__(self, parent):
            self.parent = parent # the boss is the bird sprite






class Ship(pygame.sprite.Sprite):



    def __init(self, start_position):
        pygame.sprite.Sprite.__init__(self, self.groups)
        HealthBar(self)
        self.current_position = [0.0, 0.0]



    def update(self):
        pass





'''
class CollisionTest(): # from chapter 15 of the Python Game Book
    # needs this before mainloop, probably in state, othergroup =  []  #create empty list
    # test if a bird collides with another bird
    for bird in birdgroup:
        othergroup[:] = birdgroup.sprites() # This is the correct code, no garbage collection
        othergroup.remove(bird) # remove the actual bird, only all other birds remain
        if pygame.sprite.spritecollideany(bird, othergroup): 
            bird.crashing = True
            crashgroup = pygame.sprite.spritecollide(bird, othergroup, False )
            for crashbird in crashgroup:
                bird.dx -= crashbird.pos[0] - bird.pos[0]
                bird.dy -= crashbird.pos[1] - bird.pos[1]
'''



'''
class Ship(pygame.sprite.Sprite):
    image=[]  # list of all images
    # not necessary:
    birds = {} # a dictionary of all Birds, each Bird has its own number
    number = 0  
    def __init__(self, startpos=(50,50), area): # area=screen.get_rect()):
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.pos = [0.0,0.0]
        self.pos[0] = startpos[0]*1.0 # float
        self.pos[1] = startpos[1]*1.0 # float
        self.image = Bird.image[0]
        self.rect = self.image.get_rect()
        self.area = area # where the sprite is allowed to move
        self.newspeed()
        self.catched = False
        #--- not necessary:
        self.number = Bird.number # get my personal Birdnumber
        Bird.number+= 1           # increase the number for next Bird
        Bird.birds[self.number] = self # store myself into the Bird dictionary
        #print "my number %i Bird number %i " % (self.number, Bird.number)
    def newspeed(self):
        # new birdspeed, but not 0
        speedrandom = random.choice([-1,1]) # flip a coin
        self.dx = random.random() * BIRDSPEED * speedrandom + speedrandom 
        self.dy = random.random() * BIRDSPEED * speedrandom + speedrandom 
      
    def update(self, seconds):
        self.pos[0] += self.dx * seconds
        self.pos[1] += self.dy * seconds
        # -- check if out of screen
        if not self.area.contains(self.rect):
            self.image = Bird.image[1] # crash into wall
            # --- compare self.rect and area.rect
            if self.pos[0] + self.rect.width/2 > self.area.right:
                self.pos[0] = self.area.right - self.rect.width/2
            if self.pos[0] - self.rect.width/2 < self.area.left:
                self.pos[0] = self.area.left + self.rect.width/2
            if self.pos[1] + self.rect.height/2 > self.area.bottom:
                self.pos[1] = self.area.bottom - self.rect.height/2
            if self.pos[1] - self.rect.height/2 < self.area.top:
                self.pos[1] = self.area.top + self.rect.height/2
            self.newspeed() # calculate a new direction
        else:
            if self.catched:
                self.image = Bird.image[2] # blue rectangle
            else:
                self.image = Bird.image[0] # normal bird image
        #--- calculate new position on screen -----
            
        self.rect.centerx = round(self.pos[0],0)
        self.rect.centery = round(self.pos[1],0)
'''

'''
#before main loop assignment
allgroup = pygame.sprite.Group()
snakegroup = pygame.sprite.Group()
# each Snake sprite is automatically member of both groups:
Snake.groups = allgroup, snakegroup
# create a single Snake named "mypython"
mypython = Snake()

# during mainloop:
allsprites.clear(screen, background)
allsprites.update(seconds)
allsprites.draw(screen)
pygame.display.flip()
'''

'''
# LAYERS!!!
# LayeredUpdates instead of group to draw in correct order
allgroup = pygame.sprite.LayeredUpdates() # important
#assign default groups to each sprite class
Livebar.groups =  bargroup, allgroup 
Timebar.groups = bargroup, allgroup
Bird.groups =  birdgroup, allgroup
Fragment.groups = fragmentgroup, allgroup
BirdCatcher.groups = stuffgroup, allgroup
#assign default layer for each sprite (lower numer is background)
BirdCatcher._layer = 5 # top foreground
Fragment._layer = 4
Timebar._layer = 3
Bird._layer = 2
Livebar._layer = 1 #background
'''














class Graphics():



    def __init__(self):
        self.width = 1280
        self.height = 800
        pygame.display.set_caption('S T A R  C O M M A N D E R   X')
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # fullscreen
        self.background = pygame.Surface(self.screen.get_size()).convert()



    def draw_text(self, text):
        self.font = pygame.font.SysFont('mono', 20, bold=True)
        """Center text in window
        """
        fw, fh = self.font.size(text) # fw: font width,  fh: font height
        surface = self.font.render(text, True, (0, 255, 0))
        # // makes integer division in python3
        self.screen.blit(surface, ((self.width - fw) * 1 // 2, (self.height - fh) * 1 // 2))



    def draw_circle(self, position, radius):
        # create a rectangular surface for the ball
        ballsurface = pygame.Surface((2,2))
        ballsurface.set_colorkey((0,0,0)) # make black the transparent color
        ballsurface = ballsurface.convert_alpha() # faster drawing
        # draw blue filled circle on ball surface 
        pygame.draw.circle(ballsurface, (255, 255, 255), (1, 1), radius) # color, position, radius, width
        self.screen.blit(ballsurface, position)



    def draw_starfield(self):
        self.draw_circle((100, 100), 1)
        self.draw_circle((400, 150), 1)
        self.draw_circle((500, 70), 1)
        # self.draw_circle((700, 300), 1)
        # self.draw_circle((800, 300), 1)
        self.draw_circle((1000, 700), 1)
        self.draw_circle((300, 400), 1)



    def render(self, clock_data, playtime_data):
    
        self.screen.blit(self.background, (0, 0))
        self.draw_starfield()

        self.draw_text("FPS: {:6.3}{}PLAYTIME: {:6.3} SECONDS".format(clock_data.get_fps(), " "*5, playtime_data))

        pygame.display.flip() # batch update, last thing to call




graphics = Graphics()


















class Engine(object):


    def __init__(self, fps = 30):

        self.clock = pygame.time.Clock()
        self.fps = fps
        self.playtime = 0.0
        


    def start_up(self):
        sound.play_music('sounds/score.mp3')



    def run(self):
        self.start_up()
        running = True
        
        while running:
            previous_user_input = interface.get_user_input_before_tick() # useful for getting the mouse to only trigger one effect
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        # updated_ship_movement_instructions = controller.get_new_instruction(target = event.pos) # , exact_position = 1, speed = 400) # clean up
                        pass

            milliseconds = self.clock.tick(self.fps)
            self.playtime += milliseconds * (1 / 1000.0)

            current_user_input = interface.get_user_input_after_tick() # INPUT
            state_update = controller.update(previous_user_input, current_user_input) # CONTROLLER
            graphics.render(self.clock, self.playtime)

        pygame.quit()




    





if __name__ == '__main__':
    Engine().run()


