import pyray as pr
from typing import List, Optional

class Window():
    def __init__(self, width: int, height: int, name: str) -> None:
        self.width: int = width
        self.height: int = height
        self.name: str = name
        
class Snake():
    def __init__(self) -> None:
        self.pos: List[int] = [0, 0]
        self.vel: List[int] = [1, 3]
        self.width: int = 30
        self.height: int = 30
        self.color: tuple[int] = (75, 100, 225, 250)
            
window = Window(720, 720, "Snake Game")
pr.init_window(window.width, window.height, window.name)
pr.set_target_fps(160)

snake = Snake()

while not pr.window_should_close():
    snake.pos[0] += snake.vel[0]

    
    if snake.pos[0] > window.width - snake.width:
            snake.pos[0] = -snake.width -1
           
    pr.begin_drawing()
    pr.clear_background(pr.BLACK)
    pr.draw_rectangle(snake.pos[0], snake.pos[1],
                      snake.width, snake.height, snake.color)

    pr.end_drawing()
pr.close_window()
