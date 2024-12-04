import random
import pygame

class Snake():

    def __init__(self, pos=(0, 0), size=15, life=1000):
        self.pos = pos
        self.size = size
        self.color = pygame.Color(0, 255, 0)
        self.age = 0
        self.life = life
        self.dead = False
        #self.alpha = 255
        self.surface = self.update_surface()

    def update(self, dt):
        self.age += dt
        if self.age > self.life:
            self.dead = True
        #self.alpha = 255 * (1 -(self.age / self.life))
        
    def update_surface(self):
        surf = pygame.Surface((self.size, self.size))
        surf.fill(self.color)
        return surf
    
    def draw(self, surface):
        if self.dead:
            return
        self.surface.set_alpha(self.alpha)
        surface.blit(self.surface, self.pos)
        

class SnakeTrail():

    def __init__(self, pos, size, life):
        self.pos = pos
        self.size = size
        self.life = life
        self.particles = []

    def update(self, dt):
        particle = Snake(self.pos, size=self.size, life=self.life)
        self.particles.insert(0, particle)
        self._update_pos()

    def _update_pos(self):
        x, y = self.pos
        y += self.size
        self.pos = (x, y)

    #Insert method to find direction from button inputs
    

def main():
    pygame.init()
    pygame.display.set_caption("Snake Remake")
    clock = pygame.time.Clock()
    dt = 0
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    snake = Snake(life=1000)
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