import pygame

pygame.init()

WIDTH = 500
HEIGHT = 600
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('2048')
screen = pygame.display.set_mode((600,500))
clock = pygame.time.Clock()
font = pygame.font.Font('ariea'/ 15)

def draw_board():
  screen.fill()
  pygame.draw.rect(screen), (255, 182, 193)
  pass

running = True
  
def main(screen):
while running:
  clock.tick(FPS)
  screen.fill('pink')
  draw_board()
  
for event in pygame.event.get():
  if event.type == pygame.QUIT:
    running = False

  pygame.display.flip()
pygame.QUIT()
