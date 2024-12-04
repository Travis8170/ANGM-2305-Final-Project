import random
import pygame


direction = 0
tempo = 6

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
        #self.surface.set_alpha(self.alpha)
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
        self._update_particles(dt)
        self._update_pos()

    def _update_pos(self):
        global direction
        x, y = self.pos
        if direction == 1:
            y += self.size
        self.pos = (x, y)
    #Insert method to find direction from button inputs
    #if key press
    #y or x += self.size
    #else

    def _update_particles(self, dt):
        for particle in self.particles:
            particle.update(dt)

    def draw(self, surface):
        for particle in self.particles:
            particle.draw(surface)
    
def direction_change(event):
    global direction
    if event.key == pygame.K_DOWN:
        direction = 1
    elif event.key == pygame.K_UP:
        direction = 2
    elif event.key == pygame.K_RIGHT:
        direction = 3
    elif event.key == pygame.K_LEFT:
        direction = 4
    return direction


def main():
    pygame.init()
    pygame.display.set_caption("Snake Remake")
    clock = pygame.time.Clock()
    dt = 0
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    snake = SnakeTrail(((resolution[0]//2)-10, (resolution[1]//2)-10), size =20, life=(3100//tempo))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                direction_change(event)
            if event.type == pygame.QUIT:
                running = False
        snake.update(dt)
        black = pygame.Color(0, 0, 0)
        screen.fill(black)
        snake.draw(screen)
        pygame.display.flip()
        dt = clock.tick(tempo)
    pygame.quit()


if __name__ == "__main__":
    main()