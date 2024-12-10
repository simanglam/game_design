from .Scene import Scene

from math import sin, radians, sqrt
from pygame import draw, SRCALPHA
from pygame.color import Color
from pygame.event import Event
from pygame.surface import Surface
from pygame.transform import rotozoom, rotate

from ..ui.compoment.wheel import Wheel


class RotateScene(Scene):
    def __init__(self, game):
        self.game = game
        self.rotationAngle: float = 0
        self.accumelator: int = 0
        self.wheel: Wheel = Wheel(1920 / 2, 1080 / 2)
    
    def update(self, deltaT: int, event: list[Event]) -> None:
        self.wheel.update(deltaT)
    
    def render(self, screen: Surface) -> None:
        self.wheel.draw(screen)