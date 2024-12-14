from .Scene import Scene

from pygame.font import Font
from pygame.surface import Surface
from pygame.rect import Rect
from pygame.mouse import get_pos, get_pressed
from pygame.transform import scale
from pygame.image import load
from pygame.draw import rect

class ResultScene(Scene):
    def __init__(self, game, result: str):
        self.game = game
        self.result = result
        
        self.accumulator = 0
        self.font: Font = Font("assets/wt004.ttf", 64)
        
        self.background: Surface = load(f"assets/{result["type"]}.jpg")
        if result["type"] == "hell":
            color = (255, 255, 255, 255)
        else:
            color = (0, 0, 0, 255)
        
        self.foodImage: Surface = scale(load(f"assets/{result["name"]}.jpg"), (1920, 1080))
        self.foodRect: Rect = self.foodImage.get_rect()
        self.foodRect.centerx = (1920 / 2)
        
        
        self.leaveButton: Surface = self.font.render("Leave", 0, color)
        self.leaveButtonRect: Rect = self.leaveButton.get_rect()
        self.leaveButtonRect.center = (1920 / 2, 1080 / 8 * 7)
        

    def update(self, deltaT: int) -> None:
        if self.leaveButtonRect.collidepoint(get_pos()) and get_pressed()[0]:
            self.game.scene = self.game.rotateScene
    
    def render(self, screen) -> None:
        screen.blit(self.background, (0, 0))
        screen.blit(self.foodImage, self.foodRect)
        screen.blit(self.leaveButton, self.leaveButtonRect)