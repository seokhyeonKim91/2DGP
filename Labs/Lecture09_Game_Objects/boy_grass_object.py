import random
from pico2d import *

# Game object class here

class Grass:
    def __init__(self): # 생성자
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)
    pass

class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x, self.y = random.randint(100, 700), 90
        self.frame = 0

    def update(self): # 소년의 행위 구현.
        self.x += 5 # 속성 값을 바꿈으로 써, 행위(오른쪽으로 이동)를 구현
        self.frame = (self.frame + 1 ) % 8
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Small_Ball:
    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(100, 700), 500
        self.frame = 0
    def update(self):
        ball_v =  random.randint(1, 10)
        self.y -= ball_v
        if self.y <= 30:
            self.y = 30
    def draw(self):
        self.image.draw()
class Big_Ball:
    def __init__(self):
        self.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(100, 700), 500
        self.frame = 0
    def update(self):
        ball_v =  random.randint(1, 10)
        self.y -= ball_v
        if self.y <= 30:
            self.y = 30

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code

open_canvas()

grass =Grass() #Grass 라는 클래스로부터, grass 객체를 생성한다.
team = [ Boy() for i in range(11)]
small_balls = [ Small_Ball() for i in range(5) ]
big_balls = [ Big_Ball() for i in range(5) ]
ball_v = 0

running = True

# game main loop code

while running:

    handle_events() # 키 입력을 받아들이는 처리

    #Game logic
    for boy in team:
        boy.update() # 소년의 상호작용
    for Sballs in small_balls:
        Sballs.update()
    for Bballs in big_balls:
        Bballs.update
    #Game drawing
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    update_canvas()
    for Sballs in small_balls:
        Sballs.draw()
    for Bballs in team:
        Bballs.draw()
    delay(0.05)
# finalization code