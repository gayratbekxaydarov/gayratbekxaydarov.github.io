import pygame
import random

pygame.init()
Width, Height = 600, 400
screen = pygame.display.set_mode((Width, Height))
clock = pygame.time.Clock()

class Ball:
    def __init__(self):
        self.x = random.randint(20, Width - 20)
        self.y = random.randint(20, Height - 20)
        self.radius = 15
        self.color = self.random_color()
        self.dx = random.choice([-3, 3])
        self.dy = random.choice([-3, 3])

    def move(self):
        self.x += self.dx
        self.y += self.dy

        if self.x <= self.radius or self.x >= Width - self.radius:
            self.dx *= -1
        if self.y <= self.radius or self.y >= Height - self.radius:
            self.dy *= -1

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def random_color(self):
        return (random.randint(50,255), random.randint(50,255), random.randint(50,255))

    def collide(self, other):
        distance = ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
        return distance < self.radius + other.radius

balls = [Ball() for _ in range(10)]

running = True
while running:
    screen.fill((30, 30, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for ball in balls:
        ball.move()
        ball.draw()

    for i in range(len(balls)):
        for j in range(i+1, len(balls)):
            if balls[i].collide(balls[j]):
                balls[i].color = balls[i].random_color()
                balls[j].color = balls[j].random_color()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
