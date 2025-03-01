import pyray as pr
from typing import List, Optional

class Window():
    def __init__(self, width: int, height: int, name: str) -> None:
        self.width: int = width
        self.height: int = height
        self.name: str = name
    
window = Window(1280, 720, "Snake Game")
pr.init_window(window.width, window.height, window.name)

while not pr.window_should_close():
    pr.begin_drawing()
    pr.end_drawing()
pr.close_window()
