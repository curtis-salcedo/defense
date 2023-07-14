import pygame as pg
from pygame.math import Vector2
import math

# Enemy Class
# Pygame sprite class, similar to python classes
# This will inherit the enemy class from the pygame sprite class
class Enemy(pg.sprite.Sprite):
    def __init__(self, waypoints, image):
      pg.sprite.Sprite.__init__(self)
      self.waypoint = waypoints
      self.position = Vector2(self.waypoint[0])
      print(self.position)
      # first movement after waypoint[0] above
      self.target_waypoint = 1
      # Speed will change for different enemies
      self.speed = 2
      self.angle = 0
      self.original_image = image
      self.image = pg.transform.rotate(self.original_image, self.angle)
      self.rect = self.image.get_rect()
      self.rect.center = self.position

    def update(self):
      self.move()
      self.rotate_character()

    def move(self):
      # Check if the enemy has reached the end of the path defined by the waypoints
      if self.target_waypoint < len(self.waypoint):
      # define the target waypoint
        self.target = Vector2(self.waypoint[self.target_waypoint])
        self.movement = self.target - self.position
        # Check if the enemy has reached the end of the path defined by the waypoints
      else:
        self.kill()

      # Calculate the distance between the enemy and the target waypoint
      distance = self.movement.length()
      # Check if the remaining distance is greater than the distance to the next waypoint
      if distance >= self.speed:
        self.position += self.movement.normalize() * self.speed
      else:
        if distance != 0:
          self.position += self.movement.normalize() * distance
        self.target_waypoint += 1
      self.rect.center = self.position

    def rotate_character(self):
      # Calculate the distance to the next waypoint
      distance = self.target - self.position
      # Use disnatce to calculate the angle
      self.angle = math.degrees(math.atan2(-distance[1], distance[0]))
      # Rotate the image and update the rectangle
      self.image = pg.transform.rotate(self.original_image, self.angle)
      self.rect = self.image.get_rect()
      self.rect.center = self.position
