import pygame as pg

class Button(pg.sprite.Sprite):
    def __init__(self, x, y, image, single_click):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.single_click = single_click

    def draw(self, surface):
        # Define an action
        action = False

        # Get mouse position
        mouse_position = pg.mouse.get_pos()

        # Check if mouse is hovering over button
        if self.rect.collidepoint(mouse_position):
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                # If button is a single click type button, then set clicked to True
                if self.single_click:
                  self.clicked = True
            if pg.mouse.get_pressed()[0] == 0:
                self.clicked = False

        # Draw button on screen
        surface.blit(self.image, self.rect)

        return action