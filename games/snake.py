from sense_hat import SenseHat # errorignor
from random import randint
from time import sleep


# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

COLOR_CHANGE_RED = 8
COLOR_CHANGE_GREEN = 50
COLOR_CHANGE_BLUE = 20

# KEYS
NOTHING = BLACK
SNAKE = GREEN
APPLE = RED



class Playgrond():
    def __init__(self,size=8) -> None:
        self.size = size
        self.snake = None
        self.apples = []
        self.sense = None

        self.map = []
        self.clear_map()
    
    def clear_map(self):
        self.map = []
        for _ in range(self.size**2):
            self.map.append(NOTHING)
        pass

    def __str__(self) -> str:
        string_map = ''
        for i in range(len(self.map)-1):
            if i % self.size == 0:
                string_map += '\n'
            string_map += str(self.map[i])
        return string_map
    
    def get(self, x : int, y : int):
        return self.map[y * self.size + x]
    
    def set(self, x : int, y : int, value) -> None:
        self.map[y * self.size + x] = value
    
    def get_colormap(self) -> list:
        color_map = []
        for filed in self.map:
            if filed == 0:
                color_map.append(BLACK)
            else:
                try:
                    color_map.append(filed.color())
                except:
                    color_map.append(filed)
        self.sense.set_pixels(color_map)
        return color_map

    def draw_to_map(self):
        self.clear_map()
        self.snake.draw()
        for apple in self.apples:
            apple.draw()

    def view_game(self, terminal_mode=True):
        if terminal_mode:
            return str(self)
        else:
            return self.get_colormap()


class Snake():
    def __init__(self, ground : Playgrond, head_position=(1, 3), size=4,
                    color=GREEN, colorful=True) -> None:
        self.ground = ground
        self.map = ground.map
        self.ground.snake = self


        self.head_position = head_position
        self.x, self.y = self.head_position
        self.size = size
        self.color = color
        self.colorful = colorful

        self.alive = True
        self.bigger_at_move = False
        self.direction = 0
        # 0, 1, 2, 3 = up, right, down, left
        
        self.body : list[list[tuple[int, int], tuple[int, int, int]]]
        # body = [head, body1, body2, end] | head = [position, color]
        self.setup_body()

    
    def setup_body(self) -> None:
        self.body = []
        r, g, b = self.color
        for i in range(self.size):
            self.body.append([(self.x, self.y+i), ((r+i*COLOR_CHANGE_RED)%256, (g+i*COLOR_CHANGE_GREEN)%256, (b+i*COLOR_CHANGE_BLUE)%256)])
    
    def move(self) -> None:
        if not self.alive:
            return
        

        # Head
        position, color = self.body[0]
        x, y = position
        if self.direction == 0: y-=1
        elif self.direction == 1: x+=1
        elif self.direction == 2: y+=1
        elif self.direction == 3: x-=1
        
        if str(self.ground.get(x, y)) == str(APPLE):
            self.bigger_at_move = True
            for apple in self.ground.apples:
                if apple.position == (x, y):
                    self.ground.apples.remove(apple)
            self.ground.set(x, y, NOTHING)
        elif self.ground.get(x, y) != NOTHING:
            self.alive = False
            # # print(str(self.ground.get(x, y)), self.ground.get(x, y))
            # # print(str(APPLE))
            return


        new_body = []
        new_body.append([(x, y), color])

        for index in range(1, len(self.body), 1):
            new_body.append([self.body[index-1][0], self.body[index][1]])
        
        if self.bigger_at_move:
            position, color = self.body[-1]
            r, g, b = color
            new_body.append([position, ((r+COLOR_CHANGE_RED)%256, (g+COLOR_CHANGE_GREEN)%256, (b+COLOR_CHANGE_BLUE)%256)])
            self.bigger_at_move = False

        self.body = new_body
        self.ground.draw_to_map()
    
    def bigger(self):
        self.bigger_at_move = True
    
    def check_the_position(self) -> None:
        for part in self.body:
            x, y = part[0]
            if not (0 <= x < self.size and 0 <= y < self.size):
                self.alive = False
    
    def draw(self) -> None:
        for part in self.body:
            position, color = part
            self.ground.set(position[0], position[1], color)


class Apple():
    def __init__(self, ground : Playgrond, position : tuple[int, int]) -> None:
        self.ground = ground

        if position == None:
            position = (randint(0, self.ground.size-1), randint(0, self.ground.size-1))
        self.position = position
        self.x, self.y = self.position

        self.ground.apples.append(self)
    
    def __str__(self) -> str:
        return str(APPLE)

    def color(self):
        return APPLE

    
    def draw(self):
        self.ground.set(self.x, self.y, self)


class Game():
    def __init__(self, sense = SenseHat(),ground=None, snake=None, apples=[], apples_num = 3) -> None:
        self.sense = sense
        
        if ground == None:
            ground = Playgrond()
        if snake == None:
            snake = Snake(ground)
        self.ground = ground
        self.snake = snake

        self.ground.sense = self.sense

        self.ground.apples = apples
        self.apples_num = apples_num
        self.ground.draw_to_map()
        self.get_apples()
        self.ground.draw_to_map()

        

    def get_apples(self):
        colormap = self.ground.view_game(False)
        # print('ALMA ELEJE\n', colormap)
        for _ in range(self.apples_num - len(self.ground.apples)):
            self.ground.draw_to_map()
            colormap = self.ground.view_game(False)
            place = randint(1, colormap.count(NOTHING))-1
            wrong_fields = 0
            i = 0
            while i < (place + wrong_fields) or colormap[i] != NOTHING:
                if colormap[i] != NOTHING:
                    wrong_fields += 1
                i += 1
            place += wrong_fields

            # print('Nothing:', colormap.count(NOTHING))
            # print(f'Random: {place-wrong_fields}\nWrong: {wrong_fields}\nNew: {place}\n\n')
            
            Apple(self.ground, (place % self.ground.size, place // self.ground.size))
            self.ground.draw_to_map()
            # print('ALMA VÉGE\n', colormap)    
        return colormap

    def check_moving(self):
        for event in self.sense.stick.get_events():
            # Check if the joystick was pressed
            if event.action == "pressed":
                # Check which direction
                if event.direction == "up":
                    self.ground.snake.direction = 0
                elif event.direction == "down":
                    self.ground.snake.direction = 2
                elif event.direction == "left": 
                    self.ground.snake.direction = 3
                elif event.direction == "right":
                    self.ground.snake.direction = 1
                elif event.direction == "middle":
                    pass


    def start(self, terminal_mode = False, speed=1):
        self.ground.draw_to_map()
        self.sense.clear()
        while self.ground.snake.alive:
            self.check_moving()
            self.ground.snake.move()
            self.ground.draw_to_map()

            cm = self.get_apples()
            self.ground.draw_to_map()

            self.sense.set_pixels(self.ground.view_game(terminal_mode))
            # print('EGYENLŐ-E', cm == self.ground.view_game(terminal_mode))
            # print('KAPOTT:\n', cm, '\n\n\n')
            # print('CIKLUS VÉGE\n', self.ground.view_game(terminal_mode), '\n-----------------------------')
            sleep(speed)
            


def main():
    game = Game(apples=[])
    game.start(terminal_mode=False, speed=1)

def main_loop():
    while True:
        try:
            main()
        except:
            pass
        sleep(1)
        input('TRY A NEW? ')

if __name__ == '__main__':
    main_loop()
