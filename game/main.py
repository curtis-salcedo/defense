import pygame as pg
from enemy import Enemy
from world import World
from turret import Turret
from button import Button
import json

# Constant Imports
import constants as c

# Initialize pygame
pg.init()

# Create game clock
clock = pg.time.Clock()

# Create game window
screen = pg.display.set_mode((c.SCREEN_WIDTH + c.SIDE_PANEL, c.SCREEN_HEIGHT))

# Game Variables
placing_turret = False

# Set the title of the game window
pg.display.set_caption("Defense")

## Load images
# Map image
map_image = pg.image.load("levels/level1.png").convert_alpha()
# Turret Sprite Sheet

# Indiviual turret image
turret_image = pg.image.load("assets/images/turrets/turret.png").convert_alpha()
# Enemy image
enemy_image = pg.image.load("assets/images/enemies/character.png").convert_alpha()
buy_turret_image = pg.image.load("assets/images/buttons/buy_button.png").convert_alpha()
cancel_image = pg.image.load("assets/images/buttons/buy_button.png").convert_alpha()

# Load json data for level data
with open('levels/level1.tmj') as file:
  world_data = json.load(file)

# Function to create a turret
def create_turret(mouse_position):
  mouse_tile_x = mouse_position[0] // c.TILE_SIZE
  mouse_tile_y = mouse_position[1] // c.TILE_SIZE
  # Calculate teh sequential number of the tile
  mouse_tile_num = (mouse_tile_y * c.COL) + mouse_tile_x
  # Check if the tile is placeable
  if world.tile_map[mouse_tile_num] == 33:
    # Check if turret is already in that position (tile)
    space_is_free = True
    for turret in turret_group:
      if (mouse_tile_x, mouse_tile_y) == (turret.tile_x, turret.tile_y):
        space_is_free = False
    if space_is_free == True:
      new_turret = Turret(turret_image, mouse_position, mouse_tile_x, mouse_tile_y)
      turret_group.add(new_turret)

# Create the world instance
world = World(world_data, map_image)
world.process_data()

# Create enemy group
enemy_group = pg.sprite.Group()
turret_group = pg.sprite.Group()

# Create waypoints

# Create the enemy instance
enemy = Enemy(world.waypoints, enemy_image)
enemy_group.add(enemy)

# Create buttons
turret_button = Button(c.SCREEN_WIDTH + 50, 100, buy_turret_image, True)
cancel_button = Button(c.SCREEN_WIDTH + 50, 200, cancel_image, False)

# Game Loop - while loop to keep the game running
running = True
while running:
    # Update the game clock to 60 FPS
    clock.tick(c.FPS)

    ########################################
    # UPDATE SECTION
    ########################################
    # Fill the screen with white
    screen.fill("white")

    # Update enemy group
    enemy_group.update()



    ########################################
    # DRAWING SECTION
    ########################################
    # Draw buttons
    if turret_button.draw(screen):
      placing_turret = True
      # If placing turrets then show the cancel button
    if placing_turret == True:
      # cancel_button.draw(screen)
      # Show cursor turret when buy button is clicked
      cursor_rect = turret_image.get_rect()
      cursor_position = pg.mouse.get_pos()
      cursor_rect.center = cursor_position
      if cursor_position[0] <= c.SCREEN_WIDTH:
        screen.blit(turret_image, cursor_rect)
      if cancel_button.draw(screen):
        placing_turret = False

    # Draw the level (world)
    world.draw(screen)

    # Draw enemy path
    # pg.draw.lines(screen, "black", False, world.waypoints, 3)

    # Draw the groups, Sprite class contains a draw method
    enemy_group.draw(screen)
    turret_group.draw(screen)

    # Event handler to check for events
    for event in pg.event.get():
        # Check if the user clicked the close button
        if event.type == pg.QUIT:
            # Set running to false to exit the game loop
            running = False
        # Mouse Click Event
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            mouse_position = pg.mouse.get_pos()
            # Check mouse position for game board only
            if mouse_position[0] < c.SCREEN_WIDTH and mouse_position[1] < c.SCREEN_HEIGHT:
              if placing_turret == True:
                create_turret(mouse_position)
            

    # Update the display
    pg.display.flip()

pg.quit()