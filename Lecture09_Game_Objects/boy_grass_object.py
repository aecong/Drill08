import random
from pico2d import *


# Game object class here
class Grass:
    def __init__(self):  # self : 생성된 객체를 가리키는 변수
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self): pass


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class MinBall:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.speed = random.randint(1, 10)
        self.image = load_image('ball21x21.png')

    def update(self):
        if self.y > 83:
            self.y -= 3 * self.speed
        else:
            self.y = 65
    def draw(self):
        self.image.draw(self.x, self.y)

class MaxBall:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.speed = random.randint(1, 10)
        self.image = load_image('ball41x41.png')

    def update(self):
        if self.y > 103:
            self.y -= 3 * self.speed
        else:
            self.y = 75

    def draw(self):
        self.image.draw(self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running
    global grass
    global team
    global small
    global big
    global world

    running = True
    world = []

    grass = Grass()
    world.append(grass)

    team = [Boy() for i in range(11)]
    world += team

    small = [MinBall() for i in range(10)]
    world += small

    big = [MaxBall() for i in range(10)]
    world += big

def update_world():
    # grass.update()
    # for boy in team:
    #     boy.update()
    for o in world:
        o.update()

def render_world():
    clear_canvas()
    # grass.draw()
    # for boy in team:
    #     boy.draw()
    for o in world:
        o.draw()
    update_canvas()


open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    handle_events()
    update_world()  # game logic
    render_world()  # draw game world
    delay(0.05)

# finalization code

close_canvas()
