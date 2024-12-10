from pygame.event import Event
from pygame.surface import Surface

class Scene:
    def render(self, screen: Surface) -> None:
        raise NotImplementedError("Every derived class of Scene should override this method")
    def update(self, deltaT: float, event: list[Event]):
        raise NotImplementedError("Every derived class of Scene should override this method")