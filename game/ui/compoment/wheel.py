from random import randint

from pygame.rect import Rect
from pygame.surface import Surface
from pygame.font import Font, SysFont

from ...util import smooth, ease_in_out_back, ease_out_back

class Wheel:
    def __init__(self, x: float = 0, y: float = 0, inputStr: list[str] = ["食凡", "食凡媽媽", "姐妹火鍋"]):
        self.font: Font = SysFont("wt004", 128)
        self.stringRects: list[Rect] = []
        self.stringSurfaces: list[Surface] = []
        self.len: int = len(inputStr)
        
        for i in range(0, self.len):
            self.stringSurfaces.append(self.font.render(inputStr[i], 0, (0, 0, 0, 255)))
            stringRect = self.stringSurfaces[i].get_rect().move(0, self.stringSurfaces[i].get_height() * i)
            stringRect.centerx = 320
            self.stringRects.append(stringRect)
        
        self.stringSurfaces.append(self.font.render(inputStr[0], 0, (0, 0, 0, 255)))
        stringRect = self.stringSurfaces[0].get_rect().move(0, self.stringSurfaces[0].get_height() * self.len)
        stringRect.centerx = 320
        self.stringRects.append(stringRect)
        self.len += 1
            
        self.surface: Surface = Surface((640, self.stringSurfaces[0].get_height()))
        self.rect: Rect = self.surface.get_rect()
        self.rect.center = (x, y)
        
        self.windowRect: Rect = self.surface.get_rect().move(0, 0)
        self.isRotating: bool = False
        self.accumulator: int = 0
        self.targetDistance: int = self.rect.height * 300
        
        self.currentOffset = 0
        
    def update(self, deltaT: int):
        if not self.isRotating:
            return
        
        self.accumulator += deltaT
        ratio = ease_out_back(self.accumulator / 10000)
        self.windowRect.top = ratio * self.targetDistance + self.currentOffset
        self.windowRect.top %= self.stringRects[self.len - 1].top
        if self.accumulator / 10000 >= 1:
            self.isRotating = False
            self.currentOffset = self.windowRect.top
        
    def startRotating(self):
        self.isRotating = True
        self.accumulator = 0
        self.targetDistance = self.rect.height * (45 + randint(0, self.len - 2)) + self.currentOffset
        
        
    def draw(self, surface: Surface) -> None:
        self.surface.fill((255, 255, 255))
        
        for i in range(0, self.len):
            if self.windowRect.colliderect(self.stringRects[i]):
                self.surface.blit(self.stringSurfaces[i], (self.stringRects[i].left - self.windowRect.left, self.stringRects[i].top - self.windowRect.top))
        surface.blit(self.surface, self.rect)