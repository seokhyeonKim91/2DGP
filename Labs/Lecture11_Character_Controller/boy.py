from pico2d import *

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP = range(4)
key_event_table = {
(SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
(SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
(SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
(SDL_KEYUP, SDLK_LEFT): LEFT_UP
}


# Boy States

class IdleState:
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        boy.timer = 1000
    def exit(boy, event):
        pass

def do(boy):
    boy.frame = (boy.frame + 1) % 8
    boy.timer -= 1

def draw(boy):
    if boy.dir == 1:
        boy.image.clip_draw(boy.frame * 100, 300, 100, 100, boy.x, boy.y)
    else:
        boy.image.clip_draw(boy.frame * 100, 200, 100, 100, boy.x, boy.y)


class RunState:
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        boy.dir = boy.velocity

def exit(boy, event):
    pass

def do(boy):
    boy.frame = (boy.frame + 1) % 8
    boy.timer -= 1
    boy.x += boy.velocity
    boy.x = clamp(25, boy.x, 800 - 25)

def draw(boy):
    if boy.velocity == 1:
        boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
    else:
        boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)

next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState}
}



class Boy:

    def __init__(self):
        self.x, self.y = 800 // 2, 90
        self.image = load_image('animation_sheet.png')
        self.dir = 1
        self.velocity = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        pass


    def change_state(self,  state):
        # fill here
        pass


    def add_event(self, event):
        self.event_que.insert(0, event)
        pass


    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
        self.cur_state.exit(self, event)
        self.cur_state = next_state_table[self.cur_state][event]
        self.cur_state.enter(self, event)
        pass


    def draw(self):
        self.cur_state.draw(self)
        pass


    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
        self.add_event(key_event)

        pass

