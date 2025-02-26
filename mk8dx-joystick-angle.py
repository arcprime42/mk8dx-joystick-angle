import pygame
import math

x = y = prev = 0

pygame.init()
pygame.joystick.init()
controller = pygame.joystick.Joystick(0)
controller.init()

while True:
  for event in pygame.event.get():
    if event.type == pygame.JOYAXISMOTION:
      if event.axis == 0: x = event.value
      if event.axis == 1: y = event.value
      angle = 0
      if not (x == 0 and y == 0):
        angle = math.acos(abs(x) / math.sqrt(x**2 + y**2)) * 180.0 / math.pi
      if angle != prev:
        print(angle)
      prev = angle
