import random
import pygame


direction = 0
tempo = 6
resolution = (800, 600)
start = (resolution[0]//2), (resolution[1]//2)
paused = False
in_motion = False

class Snake():

    def __init__(self, pos=(0, 0), size=15, life=1000):
        self.pos = pos
        self.size = size
        self.color = pygame.Color(0, 255, 0)
        self.age = 0
        self.life = life
        self.dead = False
        self.surface = self.update_surface()

    def update(self, dt):
        self.age += dt
        if self.age > self.life:
            self.dead = True
        
    def update_surface(self):
        surf = pygame.Surface((self.size*0.95, self.size*0.95))
        surf.fill(self.color)
        return surf
    
    def draw(self, surface):
        if self.dead:
            return
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
        if direction == 2:
            y -= self.size
        if direction == 3:
            x += self.size
        if direction == 4:
            x -= self.size
        self.pos = (x, y)

    def _update_particles(self, dt):
        for idx, particle in enumerate(self.particles):
            particle.update(dt)
            if paused == True:
                del self.particles[idx]
            if particle.dead:
                del self.particles[idx]

    def _grow_size(self):
        self.life += 1000//tempo
        for particle in self.particles:
            particle.life += 1000//tempo

    def draw(self, surface):
        for particle in self.particles:
            particle.draw(surface)


class Apple():

    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
        self.color = pygame.Color(255, 0, 0)
        self.dead = False
        self.surface = self.update_surface()

    def update(self, dt):
        if self.dead == True:
            self.dead == False

    def update_surface(self):
        surf = pygame.Surface((self.size*0.95, self.size*0.95))
        surf.fill(self.color)
        return surf
    
    def draw(self, surface):
        if self.dead:
            return
        surface.blit(self.surface, self.pos)

    
def direction_change(event):
    global direction
    if event.key == pygame.K_DOWN and direction != 2:
        direction = 1
    elif event.key == pygame.K_UP and direction != 1:
        direction = 2
    elif event.key == pygame.K_RIGHT and direction != 4:
        direction = 3
    elif event.key == pygame.K_LEFT and direction != 3:
        direction = 4

def game_reset():
    global direction
    global tempo
    global paused
    direction = 0
    tempo = 6
    paused = True
    reset_time = pygame.time.get_ticks()
    while paused == True:
        paused_time = pygame.time.get_ticks()
        if paused_time - reset_time >= 1000:
            paused_time = reset_time
            paused = False

def is_moving():
    global in_motion
    if direction > 0:
        in_motion = True
        return in_motion
    else:
        in_motion = False
        return in_motion

def has_collided():
    pass


def main():
    pygame.init()
    pygame.display.set_caption("Snake Remake")
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode(resolution)
    snake = SnakeTrail(start, size =20, life=(3100//tempo))
    apple = Apple((random.randrange(0, resolution[0], 20),
    random.randrange(0, resolution[1], 20)), size =20)
    running = True
    global in_motion
    while running:
        is_moving()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                direction_change(event)
                if event.key == pygame.K_SPACE:
                    snake._grow_size()
            if event.type == pygame.QUIT:
                running = False
        if snake.pos == apple.pos:
            snake._grow_size()
            apple.dead = True
        if (snake.pos[0] > resolution[0] or snake.pos[0] < 0 
        or snake.pos[1] > resolution[1] or snake.pos[1] < 0):
            game_reset()
            snake.pos = start
            snake.life = 3100//tempo
        snake.update(dt)
        black = pygame.Color(0, 0, 0)
        screen.fill(black)
        apple.draw(screen)
        snake.draw(screen)
        pygame.display.flip()
        dt = clock.tick(tempo)
    pygame.quit()


if __name__ == "__main__":
    main()