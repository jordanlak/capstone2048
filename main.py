import pygame

WIDTH = 500
HEIGHT = 600
fps = 60

pygame.init()
window = pygame.display.set_mode((width, height))
screen = pyagme.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('2048')


def main():
  clock = pygame.tick.Clock()
     run = True

while run:
  clock.tick(fps)

for event in pygame.event.get():
  if event.type == pygame.QUIT:
    run = False
    break
  
