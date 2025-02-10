import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
BALL_SPEED = 5
PADDLE_SPEED = 7

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)


class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 100)

    def move(self, up_key, down_key):
        keys = pygame.key.get_pressed()
        if keys[up_key] and self.rect.top > 0:
            self.rect.y -= PADDLE_SPEED
        if keys[down_key] and self.rect.bottom < HEIGHT:
            self.rect.y += PADDLE_SPEED

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)


class Ball:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, 15, 15)
        self.vx = BALL_SPEED * random.choice([-1, 1])
        self.vy = BALL_SPEED * random.choice([-1, 1])

    def move(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.vy *= -1

    def draw(self):
        pygame.draw.ellipse(screen, WHITE, self.rect)


def check_collision(ball, paddle1, paddle2, scores):
    if ball.rect.colliderect(paddle1.rect) or ball.rect.colliderect(paddle2.rect):
        ball.vx *= -1
    if ball.rect.left <= 0:
        scores[1] += 1
        ball.__init__()
    if ball.rect.right >= WIDTH:
        scores[0] += 1
        ball.__init__()


def draw_scores(scores):
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"{scores[0]} - {scores[1]}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - 30, 20))


def main():
    running = True
    paddle1 = Paddle(20, HEIGHT // 2 - 50)
    paddle2 = Paddle(WIDTH - 30, HEIGHT // 2 - 50)
    ball = Ball()
    scores = [0, 0]

    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        paddle1.move(pygame.K_w, pygame.K_s)
        paddle2.move(pygame.K_UP, pygame.K_DOWN)
        ball.move()
        check_collision(ball, paddle1, paddle2, scores)

        paddle1.draw()
        paddle2.draw()
        ball.draw()
        draw_scores(scores)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()

