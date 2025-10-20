import pygame
import random
pygame.init()

WIDTH = 500
HEIGHT 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('2048')
screen = pygame.display.set_mode((600,500))
clock = pygame.time.Clock()
fps = 60
font = pygame.font.Font('ariea'/ 15)

running = True
  
while runnig:
  clock.tick(fps)
  screen.fill('pink')
  
for event in pygame.event.get():
  if event.type == pygame.QUIT:
    running = False

  pygame.display.flip()
pygame.QUIT()
