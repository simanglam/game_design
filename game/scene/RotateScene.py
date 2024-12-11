from .Scene import Scene

from math import sin, radians, sqrt
from pygame import draw, SRCALPHA
from pygame.color import Color
from pygame.event import Event
from pygame.mouse import get_pos, get_pressed
from pygame.surface import Surface
from pygame.transform import rotozoom, rotate

from ..ui.compoment.wheel import Wheel
from ..ui.compoment.button import Button


class RotateScene(Scene):
    def __init__(self, game):
        self.game = game
        self.rotationAngle: float = 0
        self.accumelator: int = 0
        self.wheel: Wheel = Wheel(1920 / 2, 1080 / 2)
        self.rotateButton: Button = Button("GO!", self.wheel.rect.centerx, self.wheel.rect.bottom + 100).setCallBack(self.wheel.startRotating)
    
    def update(self, deltaT: int) -> None:
        self.wheel.update(deltaT)
        self.rotateButton.update(deltaT)
        
        if self.rotateButton.rect.collidepoint(get_pos()) and get_pressed()[0]:
            self.rotateButton.press()
    
    def render(self, screen: Surface) -> None:
        self.rotateButton.draw(screen)
        self.wheel.draw(screen)