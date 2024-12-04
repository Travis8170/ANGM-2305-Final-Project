import random
import pygame

class Snake():

    def __init__(self, pos=(0, 0), size=15):
        self.pos = pos
        self.size = size
        self.color = pygame.Color(0, 255, 0)
        self.age = 0
        self.alpha = 255
        self.surface = self.update_surface()

    def update(self, dt):
        self.age += dt
        
    def update_surface(self):
        surf = pygame.Surface((self.size, self.size))
        surf.fill(self.color)
        return surf
    
    def draw(self, surface):
        surface.blit(self.surface, self.pos)
        


def main():
    pygame.init()
    pygame.display.set_caption("Snake Remake")
    clock = pygame.time.Clock()
    dt = 0
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    snake = Snake()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        snake.update(dt)
        black = pygame.Color(0, 0, 0)
        screen.fill(black)
        snake.pos = (resolution[0]//2, resolution[1]//2)
        snake.draw(screen)
        pygame.display.flip()
        dt = clock.tick()
    pygame.quit()


if __name__ == "__main__":
    main()