from random import randint
from typing import Self
from collections.abc import Callable

from pygame.rect import Rect
from pygame.surface import Surface
from pygame.font import Font, SysFont, get_fonts

from ...util import smooth, ease_in_out_back, ease_out_back

class Button:
    def __init__(self, label: str, x: float = 0, y: float = 0):
        self.font: Font = Font("assets/wt004.ttf", 128)
        self.label = self.font.render(label, True, (0, 0, 0, 255))
            
        self.rect: Rect = self.label.get_rect()
        self.rect.center = (x, y)
        
        self.isDisable: bool = False
        self.accumulator: int = 0
        
        self.callBackFunc: Callable[[], None] = None
        
        
    def update(self, deltaT: int):
        if not self.isDisable:
            return
        
        self.accumulator += deltaT
        if self.accumulator > 5000:
            self.isDisable = False
            self.accumulator = 0
        
    def setCallBack(self, callBackFunc: Callable[[], None]) -> Self:
        self.callBackFunc = callBackFunc
        return self
        
    def press(self):
        if self.callBackFunc and not self.isDisable:
            self.callBackFunc()
            self.isDisable = True
        
    def draw(self, surface: Surface) -> None:
        surface.blit(self.label, self.rect)