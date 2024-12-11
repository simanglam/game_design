import pygame as pg
from .scene.Scene import Scene
from .scene.RotateScene import RotateScene

pg.init()


class Game:
    def __init__(self):
        self.scene: Scene = RotateScene(self)
        self.screen: pg.Surface = pg.display.set_mode((1920, 1080), pg.FULLSCREEN, display = 0, vsync = 1)
        self.running: bool = True

    def run(self):
        clock = pg.time.Clock()
        while self.running:
            clock.tick(60)
            quitEvent = pg.event.get(pg.QUIT)
            if len(quitEvent) > 0:
                self.running = False
            keys = pg.key.get_pressed()
            if keys[pg.K_ESCAPE]:
                self.running = False
            
            pg.event.get()
            self.screen.fill((255,) * 3)
            self.scene.update(clock.get_time())
            self.scene.render(self.screen)
            pg.display.update()
        pg.quit()
        